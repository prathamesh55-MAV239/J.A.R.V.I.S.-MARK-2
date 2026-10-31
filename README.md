# J.A.R.V.I.S. MARK 2

A lightweight, Python-powered personal assistant inspired by the iconic J.A.R.V.I.S. interface from the Avengers universe.

This project is a simple starting point for an agent-style command system that can:
- respond to natural-language prompts
- manage simple daily tasks
- show system/status information
- produce structured assistant-style replies
- serve as the foundation for future voice, web, or AI integrations

## Features

- Command-based assistant loop
- Built-in help and status commands
- Simple task creation and tracking
- Context-aware responses for common assistant actions
- Clean terminal UI using `rich`
- Easy to extend with APIs, memory, or voice modules

## Project structure

```bash
J.A.R.V.I.S.-MARK-2/
├── README.md
├── requirements.txt
├── jarvis_mark2.py
├── .gitignore
└── .venv/
```

## Requirements

Python 3.10+

Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run the assistant

```bash
python jarvis_mark2.py
```

Example commands:

```text
hello
status
time
create_task Review security patch
tasks
help
exit
```

## Example interaction

```text
J.A.R.V.I.S. MARK 2
Type 'help' for commands or 'exit' to quit.

> hello
Hello, sir. Systems are online. How may I assist you today?

> status
Power: online
Core: stable
Memory: active
Assistant mode: command-ready

> create_task Review drone diagnostics
Task added: Review drone diagnostics

> tasks
1. Review drone diagnostics

> exit
System shutdown complete. Good night, sir.
```

## Roadmap

- Add voice command support
- Add web dashboard or API layer
- Connect to real models or tools
- Add memory and conversation history
- Add command execution for system tasks

## License

MIT
