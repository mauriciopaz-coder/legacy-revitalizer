"""Process Data — Refactored version following SOLID principles.

This module provides a simple CLI application for managing data items
with user authentication. Refactored from spaghetti code using GitHub
Copilot to follow clean code practices.
"""

import datetime
import json


class DataStore:
    """Handles storage, retrieval, and persistence of data items.

    Responsible only for data operations (Single Responsibility Principle).

    Attributes:
        filepath: Path to the file used for persistence.
        items: List of stored data items.
    """

    def __init__(self, filepath="data.json"):
        """Initialize the DataStore.

        Args:
            filepath: Path to the output file for saving data.
        """
        self.filepath = filepath
        self.items = []

    def add_item(self, value):
        """Add a new item with an auto-incremented ID and timestamp.

        Args:
            value: The value to store.

        Returns:
            The newly created item dictionary.

        Raises:
            ValueError: If value is empty or whitespace.
        """
        if not value or not value.strip():
            raise ValueError("Value cannot be empty.")

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        item = {
            "id": len(self.items) + 1,
            "value": value.strip(),
            "created_at": timestamp,
        }
        self.items.append(item)
        return item

    def list_items(self):
        """Return all stored items.

        Returns:
            A list of item dictionaries.
        """
        return self.items

    def save(self):
        """Persist all items to a JSON file.

        Uses a context manager to ensure the file is properly closed.

        Raises:
            IOError: If the file cannot be written.
        """
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(self.items, f, indent=2)
        except (IOError, OSError) as e:
            raise IOError(f"Error saving file: {e}") from e


class Authenticator:
    """Handles user authentication.

    Separates authentication logic from the rest of the application
    (Single Responsibility Principle).

    Attributes:
        username: The expected username.
        password: The expected password.
    """

    def __init__(self, username, password):
        """Initialize the Authenticator with credentials.

        Args:
            username: The valid username.
            password: The valid password.
        """
        self.username = username
        self.password = password

    def authenticate(self, username, password):
        """Verify if the provided credentials are valid.

        Args:
            username: The username to check.
            password: The password to check.

        Returns:
            True if credentials match, False otherwise.
        """
        return username == self.username and password == self.password


class Application:
    """Main application that coordinates authentication and data operations.

    Uses dependency injection to receive its dependencies
    (Dependency Inversion Principle).

    Attributes:
        store: DataStore instance for data operations.
        auth: Authenticator instance for authentication.
    """

    VALID_COMMANDS = ("add", "show", "save", "exit")

    def __init__(self, store, auth):
        """Initialize the Application.

        Args:
            store: A DataStore instance.
            auth: An Authenticator instance.
        """
        self.store = store
        self.auth = auth

    def run(self):
        """Start the application: authenticate then enter the command loop."""
        username = input("User: ")
        password = input("Pass: ")

        if not self.auth.authenticate(username, password):
            print("Authentication failed. Exiting.")
            return

        print("Welcome!")
        self._command_loop()

    def _command_loop(self):
        """Process user commands until 'exit' is entered."""
        while True:
            command = input("What to do? (add/show/save/exit): ").strip().lower()

            if command not in self.VALID_COMMANDS:
                print(f"Unknown command: '{command}'. Try: {', '.join(self.VALID_COMMANDS)}")
                continue

            if command == "exit":
                print("Goodbye!")
                break
            elif command == "add":
                self._handle_add()
            elif command == "show":
                self._handle_show()
            elif command == "save":
                self._handle_save()

    def _handle_add(self):
        """Prompt for a value and add it to the store."""
        value = input("Value: ")
        try:
            item = self.store.add_item(value)
            print(f"Added item #{item['id']}: '{item['value']}' at {item['created_at']}")
        except ValueError as e:
            print(f"Error: {e}")

    def _handle_show(self):
        """Display all stored items."""
        items = self.store.list_items()
        if not items:
            print("No items to display.")
            return
        for item in items:
            print(f"Item: {item['id']} - {item['value']} at {item['created_at']}")

    def _handle_save(self):
        """Save all items to a file."""
        try:
            self.store.save()
            print(f"Data saved to {self.store.filepath}")
        except IOError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    store = DataStore()
    auth = Authenticator(username="admin", password="12345")
    app = Application(store=store, auth=auth)
    app.run()
