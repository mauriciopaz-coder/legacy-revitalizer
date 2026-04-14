# Legacy Revitalizer

Refactoring a spaghetti code script using GitHub Copilot to follow SOLID principles, add documentation, and improve error handling.

## Repository

```bash
git clone https://github.com/mauriciopaz-coder/legacy-revitalizer.git
cd legacy-revitalizer
```

## Project Description

This project takes an intentionally messy Python script (`process_data.py`) and modernizes it using GitHub Copilot without breaking the underlying logic.

### Before (Original Spaghetti Code)

- Global variables (`l`, `d`)
- Cryptic function and variable names (`fn`, `a`, `b`)
- Mixed responsibilities in a single function
- No error handling
- File manipulation without context managers
- Dead code (`calculate_something_else`)
- No documentation

### After (Refactored Code)

- **DataStore class** — Handles storage, retrieval, and persistence of items (SRP)
- **Authenticator class** — Handles user authentication (SRP)
- **Application class** — Orchestrates the flow with dependency injection (DIP)
- Context managers (`with open(...)`) and `try/except` for file operations
- Input validation for empty values
- Comprehensive docstrings on all classes and methods
- Dead code removed
- JSON output instead of raw `str()` dump

## How to Run

```bash
python process_data.py
```

The application will prompt for credentials:
```
User: admin
Pass: 12345
Welcome!
What to do? (add/show/save/exit):
```

## Commit History

| Commit | Description |
|---|---|
| `Add original spaghetti code` | The "Before" — original messy code |
| `Refactor process_data.py following SOLID principles` | The "After" — clean, modular version |
| `Add LOG.md with top 3 Copilot prompts` | Documentation of the Copilot-assisted process |

## Copilot Prompts Used

See [LOG.md](LOG.md) for the top 3 prompts that yielded the best results during the refactoring process.

## Technologies

- Python 3.x
- GitHub Copilot
- VS Code
