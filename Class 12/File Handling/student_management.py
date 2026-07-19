#!/usr/bin/env python3
"""
Student Record Management System
=================================

A small console application for maintaining student records (roll number,
name, marks) backed by a local pickle file.

Supported operations
---------------------
    1. Insert a student record
    2. Display all student records
    3. Search for a record by roll number
    4. Update the marks of an existing record
    5. Delete a record
    0. Exit

Design notes
------------
* Records are represented by the immutable-friendly :class:`Student`
  dataclass rather than raw dictionaries, giving us type safety and a
  single, well-defined record shape.
* All disk access goes through :class:`StudentRepository`, which is the
  only piece of code that knows about the on-disk file format. This keeps
  I/O concerns separate from the menu / presentation layer (separation of
  concerns, single responsibility).
* Every write is performed atomically: the repository writes a temporary
  file and then replaces the real data file with :func:`os.replace`, so a
  crash or power loss mid-write can never leave a half-written,
  corrupted database behind.
* All user input is validated in a small set of reusable helper
  functions, and *every* interactive prompt tolerates bad input,
  ``KeyboardInterrupt`` and ``EOFError`` without crashing the program.

A note on pickle
-----------------
``pickle`` is used here because it was part of the original design and
is convenient for storing arbitrary Python objects with zero boilerplate.
It is, however, **not safe to load pickle data from an untrusted source**
-- unpickling can execute arbitrary code. For a purely local,
single-user tool like this one that risk is minimal, but if this project
ever needs to accept data files from other users or over a network, it
should be migrated to a safe, language-neutral format such as JSON or a
proper embedded database (SQLite). See "Suggestions for future
enhancements" in the accompanying write-up for details.
"""

from __future__ import annotations

import os
import pickle
import sys
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Callable, TypeVar

# --------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------

DATA_FILE = Path("student.dat")
BACKUP_SUFFIX = ".bak"
TMP_SUFFIX = ".tmp"

MIN_ROLL_NO = 1
MAX_ROLL_NO = 1_000_000_000  # generous upper bound to reject "obviously wrong" input
MIN_MARKS = 0
MAX_MARKS = 1000  # adjust to match whatever grading scale is in use

T = TypeVar("T")


# --------------------------------------------------------------------------
# Data model
# --------------------------------------------------------------------------

@dataclass
class Student:
    """A single student record."""

    roll_no: int
    name: str
    marks: int

    def display(self) -> str:
        """Return a human-readable, one-record summary."""
        return f"Roll No: {self.roll_no:<10} Name: {self.name:<20} Marks: {self.marks}"


# --------------------------------------------------------------------------
# Custom exceptions
# --------------------------------------------------------------------------

class RepositoryError(Exception):
    """Base class for all repository (storage layer) failures."""


class CorruptedDataError(RepositoryError):
    """Raised when the data file exists but cannot be parsed as valid records."""


# --------------------------------------------------------------------------
# Repository (storage layer)
# --------------------------------------------------------------------------

class StudentRepository:
    """
    Handles all reading from and writing to the on-disk student database.

    This is the only class that touches the filesystem or pickle directly;
    everything else in the program works with plain :class:`Student`
    objects.
    """

    def __init__(self, path: Path = DATA_FILE) -> None:
        self.path = path

    # -- reading -----------------------------------------------------------

    def load_all(self) -> list[Student]:
        """
        Load every record from the data file.

        Returns an empty list if the file does not exist yet (i.e. this is
        a brand-new database). Raises :class:`CorruptedDataError` if the
        file exists but its contents cannot be interpreted as student
        records.
        """
        if not self.path.exists():
            return []

        records: list[Student] = []
        try:
            with self.path.open("rb") as fh:
                while True:
                    try:
                        raw = pickle.load(fh)
                    except EOFError:
                        break
                    records.append(self._coerce_to_student(raw))
        except (pickle.UnpicklingError, EOFError, AttributeError, ImportError,
                IndexError) as exc:
            raise CorruptedDataError(
                f"The data file '{self.path}' appears to be corrupted "
                f"and could not be read: {exc}"
            ) from exc
        except PermissionError as exc:
            raise RepositoryError(
                f"Permission denied while reading '{self.path}'."
            ) from exc
        except OSError as exc:
            raise RepositoryError(
                f"Could not read '{self.path}': {exc}"
            ) from exc

        return records

    @staticmethod
    def _coerce_to_student(raw: object) -> Student:
        """Validate and convert a raw unpickled object into a Student."""
        if isinstance(raw, Student):
            return raw
        if isinstance(raw, dict):
            try:
                return Student(
                    roll_no=int(raw["Rollno"]),
                    name=str(raw["Name"]),
                    marks=int(raw["Marks"]),
                )
            except (KeyError, ValueError, TypeError) as exc:
                raise CorruptedDataError(
                    f"A record has an unexpected or missing field: {raw!r}"
                ) from exc
        raise CorruptedDataError(f"Unrecognized record format: {raw!r}")

    # -- writing -------------------------------------------------------------

    def save_all(self, records: list[Student]) -> None:
        """
        Persist the full list of records, replacing the current file.

        The write is atomic: records are first written to a temporary
        file, and only once that succeeds is the real data file replaced.
        This means a crash mid-write can never corrupt or erase existing
        data. A single ``.bak`` backup of the previous file is also kept.
        """
        tmp_path = self.path.with_suffix(self.path.suffix + TMP_SUFFIX)
        backup_path = self.path.with_suffix(self.path.suffix + BACKUP_SUFFIX)

        try:
            with tmp_path.open("wb") as fh:
                for student in records:
                    pickle.dump(student, fh)

            if self.path.exists():
                self.path.replace(backup_path)
            os.replace(tmp_path, self.path)

        except PermissionError as exc:
            raise RepositoryError(
                f"Permission denied while writing '{self.path}'."
            ) from exc
        except OSError as exc:
            raise RepositoryError(f"Could not write '{self.path}': {exc}") from exc
        finally:
            tmp_path.unlink(missing_ok=True)

    def append(self, student: Student) -> None:
        """Append a single new record to the data file."""
        try:
            with self.path.open("ab") as fh:
                pickle.dump(student, fh)
        except PermissionError as exc:
            raise RepositoryError(
                f"Permission denied while writing '{self.path}'."
            ) from exc
        except OSError as exc:
            raise RepositoryError(f"Could not write '{self.path}': {exc}") from exc

    # -- higher-level operations --------------------------------------------

    def find_by_roll_no(self, roll_no: int) -> list[Student]:
        """Return every record matching the given roll number (usually 0 or 1)."""
        return [s for s in self.load_all() if s.roll_no == roll_no]

    def roll_no_exists(self, roll_no: int) -> bool:
        return any(s.roll_no == roll_no for s in self.load_all())

    def update_marks(self, roll_no: int, new_marks: int) -> int:
        """
        Update marks for every record with the given roll number.

        Returns the number of records updated (0 if the roll number was
        not found).
        """
        records = self.load_all()
        updated = 0
        new_records = []
        for student in records:
            if student.roll_no == roll_no:
                student = replace(student, marks=new_marks)
                updated += 1
            new_records.append(student)

        if updated:
            self.save_all(new_records)
        return updated

    def delete(self, roll_no: int) -> int:
        """
        Delete every record with the given roll number.

        Returns the number of records deleted (0 if the roll number was
        not found). The database is only rewritten if something was
        actually deleted.
        """
        records = self.load_all()
        remaining = [s for s in records if s.roll_no != roll_no]
        deleted = len(records) - len(remaining)

        if deleted:
            self.save_all(remaining)
        return deleted


# --------------------------------------------------------------------------
# Input validation helpers (UI layer)
# --------------------------------------------------------------------------

def _prompt(prompt: str, converter: Callable[[str], T]) -> T | None:
    """
    Read one line of input and convert it, returning ``None`` on EOF or
    Ctrl-C so callers can treat "user wants to cancel" uniformly.
    """
    try:
        raw = input(prompt)
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled.")
        return None
    try:
        return converter(raw)
    except ValueError:
        return None


def get_int_in_range(
    prompt: str, minimum: int, maximum: int, *, allow_cancel: bool = False
) -> int | None:
    """
    Repeatedly prompt until the user enters an integer within
    ``[minimum, maximum]``. Returns ``None`` if the user cancels
    (Ctrl-C / Ctrl-D), otherwise always returns a valid int.
    """
    while True:
        raw = _prompt(prompt, str)
        if raw is None:
            return None
        text = raw.strip()
        if allow_cancel and text.lower() in {"c", "cancel"}:
            return None
        if not text:
            print("Input cannot be empty. Please try again.")
            continue
        try:
            value = int(text)
        except ValueError:
            print("That doesn't look like a whole number. Please try again.")
            continue
        if not (minimum <= value <= maximum):
            print(f"Please enter a number between {minimum} and {maximum}.")
            continue
        return value


def get_non_empty_text(prompt: str, *, max_length: int = 200) -> str | None:
    """Repeatedly prompt until a non-blank string (after stripping) is entered."""
    while True:
        raw = _prompt(prompt, str)
        if raw is None:
            return None
        text = raw.strip()
        if not text:
            print("Input cannot be empty or just spaces. Please try again.")
            continue
        if len(text) > max_length:
            print(f"Please keep input under {max_length} characters.")
            continue
        return text


def get_yes_no(prompt: str) -> bool | None:
    """Ask a yes/no question. Returns True/False, or None if cancelled."""
    while True:
        raw = _prompt(prompt, str)
        if raw is None:
            return None
        answer = raw.strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please answer 'y' or 'n'.")


def get_roll_no(prompt: str = "Enter roll number: ") -> int | None:
    return get_int_in_range(prompt, MIN_ROLL_NO, MAX_ROLL_NO)


def get_marks(prompt: str = "Enter marks: ") -> int | None:
    return get_int_in_range(prompt, MIN_MARKS, MAX_MARKS)


# --------------------------------------------------------------------------
# Menu actions (UI layer) - one function per menu option
# --------------------------------------------------------------------------

def action_insert(repo: StudentRepository) -> None:
    """Prompt for a new record and store it, rejecting duplicate roll numbers."""
    roll_no = get_roll_no()
    if roll_no is None:
        return

    if repo.roll_no_exists(roll_no):
        print(f"A student with roll number {roll_no} already exists. "
              f"Use 'update' instead, or choose a different roll number.")
        return

    name = get_non_empty_text("Enter name: ")
    if name is None:
        return

    marks = get_marks()
    if marks is None:
        return

    student = Student(roll_no=roll_no, name=name, marks=marks)
    try:
        repo.append(student)
    except RepositoryError as exc:
        print(f"Could not save the record: {exc}")
        return

    print(f"Record added successfully: {student.display()}")


def action_display_all(repo: StudentRepository) -> None:
    """Display every record currently stored."""
    try:
        records = repo.load_all()
    except RepositoryError as exc:
        print(f"Could not read records: {exc}")
        return

    if not records:
        print("No records found. The database is empty.")
        return

    print(f"\n{len(records)} record(s) found:")
    for student in records:
        print(f"  {student.display()}")


def action_search(repo: StudentRepository) -> None:
    """Search for and display records matching a roll number."""
    roll_no = get_roll_no("Enter a roll number to search: ")
    if roll_no is None:
        return

    try:
        matches = repo.find_by_roll_no(roll_no)
    except RepositoryError as exc:
        print(f"Could not search records: {exc}")
        return

    if not matches:
        print("No record found for that roll number.")
        return

    if len(matches) > 1:
        print(f"Warning: {len(matches)} records share this roll number "
              f"(duplicate data detected):")
    for student in matches:
        print(f"  {student.display()}")


def action_update(repo: StudentRepository) -> None:
    """Update the marks of an existing record, after confirmation."""
    roll_no = get_roll_no("Enter the roll number to update: ")
    if roll_no is None:
        return

    try:
        matches = repo.find_by_roll_no(roll_no)
    except RepositoryError as exc:
        print(f"Could not read records: {exc}")
        return

    if not matches:
        print("No student found with that roll number.")
        return

    print("Current record(s):")
    for student in matches:
        print(f"  {student.display()}")

    new_marks = get_marks("Enter new marks: ")
    if new_marks is None:
        return

    confirmed = get_yes_no(f"Update marks to {new_marks} for roll number "
                            f"{roll_no}? (y/n): ")
    if not confirmed:
        print("Update cancelled.")
        return

    try:
        updated = repo.update_marks(roll_no, new_marks)
    except RepositoryError as exc:
        print(f"Could not update the record: {exc}")
        return

    if updated:
        print(f"Successfully updated {updated} record(s).")
    else:
        print("No matching record was found to update.")


def action_delete(repo: StudentRepository) -> None:
    """Delete a record after confirming with the user."""
    roll_no = get_roll_no("Enter the roll number to delete: ")
    if roll_no is None:
        return

    try:
        matches = repo.find_by_roll_no(roll_no)
    except RepositoryError as exc:
        print(f"Could not read records: {exc}")
        return

    if not matches:
        print("No student found with that roll number. Nothing was deleted.")
        return

    print("The following record(s) will be deleted:")
    for student in matches:
        print(f"  {student.display()}")

    confirmed = get_yes_no("Are you sure you want to delete this record? (y/n): ")
    if not confirmed:
        print("Deletion cancelled.")
        return

    try:
        deleted = repo.delete(roll_no)
    except RepositoryError as exc:
        print(f"Could not delete the record: {exc}")
        return

    if deleted:
        print(f"Successfully deleted {deleted} record(s).")
    else:
        print("No matching record was found to delete.")


# --------------------------------------------------------------------------
# Menu loop
# --------------------------------------------------------------------------

MENU_TEXT = """
=========================================
   Student Record Management System
=========================================
 1. Insert a new record
 2. Display all records
 3. Search for a record by roll number
 4. Update marks for a record
 5. Delete a record
 0. Exit
-----------------------------------------
"""

MENU_ACTIONS: dict[int, Callable[[StudentRepository], None]] = {
    1: action_insert,
    2: action_display_all,
    3: action_search,
    4: action_update,
    5: action_delete,
}


def run_menu(repo: StudentRepository) -> None:
    """Run the main interactive menu loop until the user exits."""
    while True:
        print(MENU_TEXT)
        choice = get_int_in_range(
            "Enter your choice (0-5): ", 0, max(MENU_ACTIONS), allow_cancel=False
        )

        if choice is None:
            # EOF / Ctrl-C while choosing: exit gracefully rather than looping forever.
            print("\nExiting.")
            return

        if choice == 0:
            print("Goodbye!")
            return

        action = MENU_ACTIONS[choice]
        action(repo)


def main() -> int:
    """Program entry point."""
    repo = StudentRepository(DATA_FILE)
    try:
        run_menu(repo)
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
    except CorruptedDataError as exc:
        print(f"\nFatal: {exc}")
        print(f"You may need to restore from the backup file "
              f"'{DATA_FILE}{BACKUP_SUFFIX}' if one exists.")
        return 1
    except RepositoryError as exc:
        print(f"\nFatal storage error: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
