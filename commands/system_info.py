import datetime
import platform

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def get_system_info():
    return f"""
💻 System Information
----------------------
OS: {platform.system()}
Version: {platform.version()}
Machine: {platform.machine()}
Processor: {platform.processor()}
"""
