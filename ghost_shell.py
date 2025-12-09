import os
import datetime

# =============== COLORS ===============
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# =============== ASCII BANNER ===============
BANNER = f"""
{CYAN}
   ██████   ██   ██   ██████  ███████ ████████ 
  ██        ██   ██  ██       ██         ██    
  ██   ███  ███████  ██   ███ █████      ██    
  ██    ██  ██   ██  ██    ██ ██         ██    
   ██████   ██   ██   ██████  ███████    ██    
        G H O S T   S H E L L   T E R M I N A L

{RESET}
"""

# =============== HISTORY ===============
history = []

# =============== PRO LOGGING SYSTEM ===============
def log_command(cmd, output):
    """Logs commands AND their output with timestamp."""
    os.makedirs("logs", exist_ok=True)
    path = "logs/commands.log"

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(path, "a") as log:
        log.write(f"[{timestamp}] COMMAND: {cmd}\n")
        if output:
            log.write(f"OUTPUT: {output}\n")
        log.write("-" * 45 + "\n")


def handle_history():
    if not history:
        return "No commands used yet."
    return "\n".join(history)

# =============== IMPORT MODULES ===============
from commands.file_ops import list_files, change_dir, make_dir, read_file, create_file
from commands.system_info import get_time, get_date, get_system_info
from commands.explain_module import explain


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# =============== HELP MENU ===============
def help_menu():
    print(f"""
{YELLOW}Available Commands:{RESET}
  help                   Show this menu
  ls                     List files
  cd <folder>            Change directory
  mkdir <name>           Create folder
  touch <file>           Create file
  read <file>            Read a file
  pwd                    Show current directory
  time                   Show current time
  date                   Show current date
  sysinfo                Show system info
  explain <topic>        Explain OS concept
  history                Show command history
  clear                  Clear terminal
  exit                   Quit Ghost Shell
""")


# =============== MAIN LOOP ===============
def main():
    clear()
    print(BANNER)
    print(f"{GREEN}👻 Ghost Shell v2.0 — Enhanced Edition{RESET}")
    print("Type 'help' for commands.\n")

    while True:
        command = input(f"{CYAN}ghost> {RESET}").strip()
        output = ""

        # Save to history (only if not empty)
        if command:
            history.append(command)

        # ========== COMMAND HANDLING ==========
        if command == "help":
            output = None
            help_menu()

        elif command == "ls":
            output = list_files()
            print(output)

        elif command.startswith("cd "):
            path = command.split(" ", 1)[1]
            output = change_dir(path)
            print(output)

        elif command.startswith("mkdir "):
            name = command.split(" ", 1)[1]
            output = make_dir(name)
            print(output)

        elif command.startswith("touch "):
            name = command.split(" ", 1)[1]
            output = create_file(name)
            print(output)

        elif command.startswith("read "):
            name = command.split(" ", 1)[1]
            output = read_file(name)
            print(output)

        elif command == "pwd":
            output = os.getcwd()
            print(output)

        elif command == "time":
            output = get_time()
            print(output)

        elif command == "date":
            output = get_date()
            print(output)

        elif command == "sysinfo":
            output = get_system_info()
            print(output)

        elif command.startswith("explain"):
            parts = command.split(" ", 1)
            if len(parts) == 2:
                output = explain(parts[1])
                print(output)
            else:
                output = "Usage: explain <topic>"
                print(output)

        elif command == "history":
            output = handle_history()
            print(output)

        elif command == "clear":
            clear()
            continue  # Don't log screen clear

        elif command == "exit":
            print("👋 Goodbye!")
            break

        else:
            output = "❌ Unknown command. Type 'help'."
            print(output)

        # ========== LOG COMMAND + OUTPUT ==========
        log_command(command, output)


if __name__ == "__main__":
    main()
