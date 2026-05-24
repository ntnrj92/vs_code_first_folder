# Learn VS Code with this Python Project

This guide helps you learn the most useful VS Code features while working on the small Python project in this folder.

## 1. Open files and move around

- Use the **Explorer** on the left to open files.
- Click `main.py`, `calculator.py`, or `hello_world.py` to view them.
- Use **Ctrl+P** / **Cmd+P** to quickly open a file by typing its name.

## 2. Run Python code

- Open `main.py` in the editor.
- Open the terminal with `View > Terminal` or `Ctrl+` `` ` `` / `Cmd+` `` ` ``.
- Type:
  ```bash
  python main.py
  ```
- If the terminal is running a Python REPL or another process, switch to the `zsh` terminal tab.

## 3. Use the editor features

- Save changes with `Ctrl+S` / `Cmd+S`.
- Use **Ctrl+F** / **Cmd+F** to search text inside the current file.
- Use **Ctrl+Shift+F** / `Cmd+Shift+F` to search across all files in the workspace.
- Use **Alt+Click** or `Cmd+\` to split the editor and view two files side by side.

## 4. Work with the terminal tabs

- The bottom panel can show multiple terminal tabs.
- `zsh` is your normal command shell.
- `Python` is a Python process or REPL session.
- Click a tab to switch sessions, or click `+` to create a new one.

## 5. Use the Command Palette

- Press `Ctrl+Shift+P` / `Cmd+Shift+P`.
- Type commands like:
  - `Python: Select Interpreter`
  - `Terminal: Create New Integrated Terminal`
  - `View: Toggle Panel`

## 6. Debugging basics

- Open `main.py`.
- Press `F5` to start debugging.
- Use the debug panel to:
  - Step over lines
  - Inspect variables
  - See the call stack

## 7. Learn from the code

- `hello_world.py` shows a simple `print()`.
- `calculator.py` defines functions:
  - `add(a, b)`
  - `subtract(a, b)`
  - `multiply(a, b)`
  - `divide(a, b)`
- `main.py` uses those functions and asks the user for input.

## 8. Try these practice tasks

1. Change the greeting in `hello_world.py` and run it.
2. Add a new function to `calculator.py` like `power(a, b)`.
3. Update `main.py` so option `6` computes `a` to the power of `b`.
4. Use the terminal and run `python main.py` after each edit.
5. If you see an error, read the `Problems` panel or terminal messages.

## 9. About `__pycache__`

- Python creates `__pycache__` automatically when it runs code.
- It stores compiled versions of your files.
- You can ignore it while learning.

## 10. Helpful next step

As you learn, use this workflow:

1. open a file
2. edit the code
3. save it
4. run it in the terminal
5. fix any errors

That is the easiest way to learn VS Code and Python together.
