<div align="center">

```
  ____             ____  _          _ _
 |  _ \ _   _     / ___|| |__   ___| | |
 | |_) | | | |____\___ \| '_ \ / _ \ | |
 |  __/| |_| |_____|__) | | | |  __/ | |
 |_|    \__, |    |____/|_| |_|\___|_|_|
        |____|
```

**The shell that speaks human.**

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Mac%20%7C%20Windows-lightgrey?style=flat-square)
![Status](https://img.shields.io/badge/Status-v1.0%20Stable-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

</div>

---

## What is PY-SHELL?

PY-SHELL is a Python-powered terminal shell built for humans — not cryptic flag memorizers.

Forget `rm -rf`, `chmod 755`, or whatever `tar -xzvf` is supposed to mean. PY-SHELL lets you just *say* what you want. Type `delete file`, `copy`, `where am i` — it gets it. Built from scratch on Fedora, designed to eventually boot as its own OS.

This is the **anti-bash**. Your shell. Your rules.

---

## Features

- **Plain English commands** — every command has multiple natural aliases
- **No permission nannying** — you're the owner, you decide
- **Cross-platform** — runs on Linux, Mac, and Windows
- **Offline** — pure Python standard library, no dependencies
- **System info** — built-in `fetch` command (yes, like neofetch)
- **Command history** — tracks everything you've typed this session
- **File tools** — copy, move, rename, peek inside files, get file info
- **Ping** — works with both IPs and domain names

---

## Getting Started

```bash
git clone https://github.com/cpu-gpu-ram/Py-Shell.git
cd py-shell
python Py-Shell.py
```

That's it. No installs. No dependencies. Just Python.

---

## Commands

| Command | Aliases | What it does |
|---|---|---|
| `ls` | `list files`, `files` | List files in current directory |
| `cd` | `go to`, `change directory` | Change directory |
| `mkdir` | `new folder`, `create directory` | Make a directory |
| `rmdir` | `delete folder`, `remove directory` | Remove a directory |
| `cp` | `copy`, `duplicate` | Copy a file |
| `mv` | `move`, `rename` | Move or rename a file |
| `rm` | `delete`, `delete file` | Delete a file |
| `tree` | `file tree`, `directory tree` | Show file tree |
| `peek` | `cat`, `read`, `show file` | Show file contents |
| `file info` | `file details` | File size, dates, name |
| `search` | `find file`, `search files` | Search files by keyword |
| `fetch` | `sysinfo`, `fff` | System info (like neofetch) |
| `df` | `disk usage`, `disk space` | Show disk usage |
| `programs` | `list programs` | Show installed programs |
| `pwd` | `where am i`, `current directory` | Show current directory |
| `whoami` | `who am i`, `user` | Show current user |
| `date` | `time`, `current date` | Show date and time |
| `clear` | `cls`, `blank` | Clear the screen |
| `history` | `log`, `show history` | Show command history |
| `ping` | `connect` | Ping an IP or domain |
| `help` | `save me please` | Show all commands |
| `exit` | — | Quit PY-SHELL |

---

## Roadmap

- [x] v1.0 — Core shell with 20+ commands
- [ ] v1.1 — Dictionary-based command dispatcher (replacing elif chains)
- [ ] v1.1 — GitHub wiki documentation
- [ ] v2.0 — Bootable image, kernel in C, Python bundled in `/system/`
- [ ] v2.0 — Ephemeral virtual framebuffer for GUI apps
- [ ] v2.0 — Container support for foreign Linux/Windows software

---

## Philosophy

Most shells were built for engineers in the 1970s. PY-SHELL is built for everyone else.

- Commands should be readable
- The user is the owner — no hand-holding
- Simple beats clever
- If bash needs a man page, PY-SHELL shouldn't

---

## Built By

**BostonKing69**

> *"The best tool is the one you actually understand."*

---

<div align="center">
⭐ Star the repo if you believe the terminal should speak your language.
</div>
