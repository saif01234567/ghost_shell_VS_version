explanations = {
    "cpu": """
CPU (Central Processing Unit):
- Executes instructions
- Fetch-Decode-Execute cycle
- Handles arithmetic/logic operations
""",

    "process": """
Process:
- Program in execution
- Has PID, memory space, PCB
""",

    "scheduling": """
CPU Scheduling:
- Decides which process runs next
Algorithms:
- FCFS
- SJF
- RR
- Priority Scheduling
""",

    "deadlock": """
Deadlock:
- Two or more processes waiting forever
Conditions:
- Mutual exclusion
- Hold and wait
- No preemption
- Circular wait
""",

    "os": """
Operating System:
- Manages hardware + software
- Responsible for memory, processes, I/O, file system
"""
}

def explain(topic):
    topic = topic.lower()
    return explanations.get(topic, "❌ Explanation not found.")
