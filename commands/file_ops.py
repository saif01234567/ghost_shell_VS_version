import os

def list_files():
    return "\n".join(os.listdir())

def change_dir(path):
    try:
        os.chdir(path)
        return ""
    except:
        return "❌ Invalid directory."

def make_dir(name):
    try:
        os.mkdir(name)
        return f"📁 Folder created: {name}"
    except:
        return "❌ Could not create folder."

def read_file(name):
    try:
        with open(name, "r") as f:
            return f.read()
    except:
        return "❌ File not found."

def create_file(name, content=""):
    try:
        with open(name, "w") as f:
            f.write(content)
        return f"📝 File created: {name}"
    except:
        return "❌ Could not create file."
