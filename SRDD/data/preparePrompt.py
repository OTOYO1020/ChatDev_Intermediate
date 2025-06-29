import json

# Load the formatted_tasks.json file
with open('formatted_tasks.json', 'r', encoding='utf-8') as file:
    tasks = json.load(file)

# Create a text file to store commands
output_file = 'execute_tasks.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    for i, task in enumerate(tasks, start=1):
        task_details = task.get("task", "")
        subtask1 = task.get("subtask1", "")
        subtask2 = task.get("subtask2", "")
        subtask3 = task.get("subtask3", "")
        subtask4 = task.get("subtask4", "")
        subtask5 = task.get("subtask5", "")

        # Construct the full command
        command = (
            f"python3 run.py --config \"Agile\" --name \"{i}\" --task \"Please develop in Java. {task_details}\" "
            f"--subtask1 \"{subtask1}\" --subtask2 \"{subtask2}\" "
            f"--subtask3 \"{subtask3}\" --subtask4 \"{subtask4}\" "
            f"--subtask5 \"{subtask5}\""
        )

        # Write the command to the text file
        file.write(f"{command}\n")

print(f"Commands have been saved to {output_file}.")
