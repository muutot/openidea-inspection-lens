# Demo project

A throwaway project for the plugin's screenshots. Nothing here comes from a real
codebase; every problem is on purpose.

| Style | What produces it | Where |
| --- | --- | --- |
| `error` | an undefined name, from the Python language server | `app.py`, `print(row, label)` |
| `warning` | ruff `B006`: a mutable default argument | `app.py`, `def report(rows, extra=[], …)` |
| `weak` | ruff `F401` / `F841`: an unused import or variable (unnecessary) | `app.py`, `import json`, `unused_variable` |
| `info` | ruff `N801`: a class name that breaks the convention (style suggestion) | `app.py`, `class badName` |
| `typo` | the Spelling inspection | `app.py`, the comment; `notes.md` |
| `muted` | every annotation with **Use editor font** off | plugin settings |

Open this folder in OpenIDEA with the plugin installed. `ruff.toml` is what
turns on the lint rules; the Python language server (pyrefly) needs no config.
