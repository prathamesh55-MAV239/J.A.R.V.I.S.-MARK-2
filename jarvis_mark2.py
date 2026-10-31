import asyncio
from datetime import datetime
from typing import List, Dict

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.prompt import Prompt
except ImportError:
    Console = None


class JarvisAgent:
    """A lightweight assistant inspired by J.A.R.V.I.S."""

    def __init__(self):
        self.tasks: List[str] = []
        self.system_status = {
            "power": "online",
            "core": "stable",
            "memory": "active",
            "assistant_mode": "command-ready",
        }

    def greet(self) -> str:
        return "Hello, sir. Systems are online. How may I assist you today?"

    def get_status(self) -> str:
        lines = [
            f"Power: {self.system_status['power']}",
            f"Core: {self.system_status['core']}",
            f"Memory: {self.system_status['memory']}",
            f"Assistant mode: {self.system_status['assistant_mode']}",
        ]
        return "\n".join(lines)

    def get_time(self) -> str:
        return f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    def add_task(self, task: str) -> str:
        if not task.strip():
            return "No task provided."
        self.tasks.append(task.strip())
        return f"Task added: {task.strip()}"

    def list_tasks(self) -> str:
        if not self.tasks:
            return "No active tasks."
        lines = [f"{i + 1}. {task}" for i, task in enumerate(self.tasks)]
        return "\n".join(lines)

    def help(self) -> str:
        commands = [
            "hello - greet the assistant",
            "status - show system status",
            "time - display current time",
            "create_task <task> - add a task",
            "tasks - list active tasks",
            "help - show available commands",
            "exit - shut down the assistant",
        ]
        return "\n".join(commands)

    def process(self, user_input: str) -> str:
        command = user_input.strip().lower()

        if not command:
            return "I am listening. Please provide a command."

        if command in {"hello", "hi", "hey"}:
            return self.greet()

        if command == "status":
            return self.get_status()

        if command == "time":
            return self.get_time()

        if command == "help":
            return self.help()

        if command == "tasks":
            return self.list_tasks()

        if command.startswith("create_task "):
            task = user_input[len("create_task ") :].strip()
            return self.add_task(task)

        if command in {"exit", "quit", "shutdown"}:
            raise SystemExit("System shutdown complete. Good night, sir.")

        return (
            "Command not recognized. "
            "Type 'help' to see available commands."
        )


def main() -> None:
    agent = JarvisAgent()

    if Console is not None:
        console = Console()
        console.print(Panel.fit("[bold cyan]J.A.R.V.I.S. MARK 2[/bold cyan]\n[italic]Voice-ready command assistant[/italic]",
                               title="System Online",
                               border_style="bright_blue"))
    else:
        print("J.A.R.V.I.S. MARK 2")
        print("Type 'help' for commands or 'exit' to quit.")

    while True:
        try:
            if Console is not None:
                user_input = Prompt.ask("[bold bright_magenta]>[/bold bright_magenta] ")
            else:
                user_input = input("> ")

            output = agent.process(user_input)
            if Console is not None:
                console.print(output)
            else:
                print(output)

        except SystemExit as exc:
            print(exc)
            break
        except KeyboardInterrupt:
            print("\nSystem shutdown interrupted. Safe mode engaged.")
            break


if __name__ == "__main__":
    asyncio.run(asyncio.sleep(0))
    main()
