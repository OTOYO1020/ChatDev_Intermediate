import json

# Load the original task.json file
with open('task2.json', 'r', encoding='utf-8') as file:
    tasks = json.load(file)

# Prepare the output structure
formatted_tasks = []

for task in tasks:
    original_prompt = task.get("original_prompt", "")
    formatted_chunks = task.get("formatted_chunks", "")
    
    # Extract subtask details
    subtasks = formatted_chunks.split('\n')
    subtasks_dict = {f"subtask{i + 1}": subtask.split(": ", 1)[1] if ": " in subtask else "" for i, subtask in enumerate(subtasks)}

    # Construct the new task format
    formatted_task = {
        "task": original_prompt,
        **subtasks_dict
    }

    formatted_tasks.append(formatted_task)

# Save the output to a new JSON file
output_file = 'formatted_tasks2.json'
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(formatted_tasks, file, ensure_ascii=False, indent=4)

print(f"Formatted tasks have been saved to {output_file}.")
