

## About Py-Shell

Py-Shell is a Python-powered terminal shell designed to be the "anti-bash." Instead of forcing users to memorize cryptic flags and manual pages, Py-Shell allows you to use plain, natural English to interact with your operating system. Whether you are creating folders, managing files, or checking system health, you simply type what you want to do.

---

## How to Install

1. **Copy and paste in bash terminal**
   ```bash
   git clone https://github.com/cpu-gpu-ram/Py-Shell
   cd Py-Shell
   chmod +x Py-Shell
   ./Py-Shell
## Our Evolution: From Prototype to Power

Py-Shell has evolved from a simple command translator into a robust, dictionary-based environment.

* **The Early Days (Prototype, v0.2-v0.3):** Started with basic `if/elif` chain structures to test command translation for core tasks like listing files and directory navigation.
* **The Consolidation Phase (v1.0-v1.1):** Transitioned to a more stable structure, refining the command dispatcher and improving how the shell interacted with the native operating system.
* **The Modern Era (v2.0-v2.3):** A major architectural overhaul introduced a clean dictionary-based routing system. This improved speed, added support for advanced tools like archive management (`zip`/`unzip`), and integrated custom system diagnostic tools like `fff` (Fake Fast Fetch).

---

## How to Use & Help

Py-Shell is designed to be intuitive. If you are ever unsure of what to do, you can use these built-in commands:

* **Help:** Type `help`, `sos`, or `save me` to see available commands.
* **Passthrough:** If you need to use a native system command, use `raw`, `bash`, `shell`, or `terminal` followed by your command.
* **File Management:** Use phrases like `make folder`, `destroy file`, `copy`, or `move`.
* **System Info:** Use `fff` for system diagnostics or `disk`/`space` to check your storage.

---

## Philosophy

Most shells were built for engineers in the 1970s. Py-Shell is built for everyone else.

* **Human-Readable:** If you can say it, you can execute it.
* **Ownership:** You are the owner of your files and system processes.
* **Transparency:** No hidden flags—just your intent and our translation.

---

with open("README.md", "w") as f:
f.write(readme_content)
