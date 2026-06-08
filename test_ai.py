from ai_processor import extract_tasks

tasks = extract_tasks(
    "Call Ram tomorrow and finish dashboard testing"
)

for task in tasks:
    print(task)