# Source Control Practice with VS Code and Git

This guide helps you learn Git and VS Code Source Control using your current project.

## 1. Open the Source Control view

- Click the **Source Control** icon in the Activity Bar (left side).
- If Git is initialized, you will see changed files listed there.

## 2. Initialize Git (already done for you)

The workspace is now a Git repository. The repository tracks file changes and makes it easy to save progress.

## 3. What to do in Source Control

- Edited files appear under **Changes**.
- Click a file to view diff changes.
- Use the **+** button next to each file to stage it.
- Use the **✓ Commit** box to write a commit message.
- Press the **check mark** icon to commit your changes.

## 4. Practice tasks

1. Open `main.py` and change the text in one `print()` statement.
2. Save the file.
3. Go to Source Control and review the changed file.
4. Stage the change and commit it with a message like `Update greeting text`.
5. Now change `calculator.py` by adding a new function, for example:
   ```python
   def power(a, b):
       return a ** b
   ```
6. Save the file, stage it, and commit again.

## 5. Use the terminal too

You can also run Git from the terminal:

```bash
git status
git add .
git commit -m "Your commit message"
```

## 6. Helpful notes

- `git status` shows what changed.
- `git diff` shows the exact changes.
- A commit creates a saved checkpoint.
- `.gitignore` keeps unwanted files out of Git.

## 7. Next step

After committing, try the **Source Control** view again. You should see no changes if all edits are committed.

Then make one more edit and repeat the stage/commit process.
