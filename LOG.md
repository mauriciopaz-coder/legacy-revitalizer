# Copilot Refactoring Log

## Top 3 Prompts That Yielded the Best Results

### Prompt 1 — SOLID Principles Plan
**Prompt:**
```
@workspace how can I refactor process_data.py to follow SOLID principles and remove global variables?
```
**Why it was effective:**
This prompt gave Copilot full context of the workspace and asked for a high-level refactoring plan. Copilot responded with a clear strategy: encapsulate data and logic into classes (`DataStore`, `Authenticator`, `Application`), remove global variables (`l`, `d`), split responsibilities (SRP), improve error handling, and eliminate dead code. This served as the roadmap for all subsequent refactoring steps.

---

### Prompt 2 — Extract Data Persistence Class
**Prompt:**
```
Can you extract the data persistence logic into a separate class?
```
**Why it was effective:**
Copilot generated a complete `DataStore` class with `add_item`, `list_items`, `save`, and `load` methods, replacing the global list `l` and the monolithic `fn()` function. It also applied the context manager pattern (`with open(...)`) for file handling, directly addressing the Single Responsibility Principle. The generated diff showed +64 -42 lines changed, which was the most impactful single transformation.

---

### Prompt 3 — Error Handling
**Prompt:**
```
Identify points of failure in the file saving logic and suggest try-except blocks
```
**Why it was effective:**
Copilot identified three specific failure points in the original save logic: `open()` (file not found or permission denied), `f.write()` (disk full or invalid handle), and `f.close()` (filesystem instability). It suggested wrapping the operation in a `try/except (IOError, OSError)` block and recommended using a context manager as the preferred approach. This prompt was effective because it asked Copilot to analyze specific vulnerabilities rather than giving a generic "fix this" request.
