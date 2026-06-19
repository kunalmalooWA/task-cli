# task-cli
https://roadmap.sh/projects/task-tracker
A sleek, lightweight Command Line Interface (CLI) application built in Python to help you manage your daily tasks directly from your terminal.

---

## 📋 System Requirements

To run `task-cli`, your system must meet the following minimum requirements:

- **Operating System:** Cross-platform (Windows, macOS, Linux/Unix).
- **Runtime Environment:** **Python 3.8** or higher installed.
- **Dependencies:** Built entirely using Python's native standard library. No external `pip` packages (like Click or Typer) are required, making it lightweight and secure.
  - `sys` & `argparse` (for CLI argument handling)
  - `json` (for local file state management)
  - `datetime` (for creating and updating task timestamps)

---

## 🛠️ Installation

To install `task-cli` locally in **editable mode** (so that any changes you make to the code are applied instantly without reinstalling), run the following command in your project's root directory:

```bash
pip install -e .
```
