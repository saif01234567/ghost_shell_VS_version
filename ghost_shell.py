import os
from commands.file_ops import list_files, change_dir, make_dir, read_file, create_file
from commands.system_info import get_time, get_date, get_system_info
from commands.explain_module import explain

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def help_menu():
    print("""
Available Commands:
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
  clear                  Clear terminal
  exit                   Quit Ghost Shell
""")

def main():
    clear()
    print("👻 Ghost Shell v1.0 — OS Project")
    print("Type 'help' for commands.\n")

    while True:
        command = input("ghost> ").strip()

        if command == "help":
            help_menu()

        elif command == "ls":
            print(list_files())

        elif command.startswith("cd "):
            path = command.split(" ", 1)[1]
            print(change_dir(path))

        elif command.startswith("mkdir "):
            name = command.split(" ", 1)[1]
            print(make_dir(name))

        elif command.startswith("touch "):
            name = command.split(" ", 1)[1]
            print(create_file(name))

        elif command.startswith("read "):
            name = command.split(" ", 1)[1]
            print(read_file(name))

        elif command == "pwd":
            print(os.getcwd())

        elif command == "time":
            print(get_time())

        elif command == "date":
            print(get_date())

        elif command == "sysinfo":
            print(get_system_info())

        elif command.startswith("explain"):
            parts = command.split(" ", 1)
            if len(parts) == 2:
                print(explain(parts[1]))
            else:
                print("Usage: explain <topic>")

        elif command == "clear":
            clear()

        elif command == "exit":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Unknown command. Type 'help'.")

if __name__ == "__main__":
    main()
