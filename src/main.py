#from tasks.task_manager import TaskManager

# Initial list of tasks (students will enhance this later)
tasks = ["Buy groceries", "Finish project", "Call mom", "Send email", "Clean room"]

#task_manager = TaskManager(tasks)

#task_manager.display_tasks()
def display_tasks(task_list):
    print("\nCurrent To-Do List:")
    for index, task in enumerate(task_list, start=1):
        print(f"{index}. {task}")

# Filtering
def filter_tasks(task_list, keyword):
    filtered = [task for task in task_list if keyword.lower() in task.lower()]
    print(f"\nTasks matching '{keyword}':")
    display_tasks(filtered)

# Generators
def task_generator(task_list, keyword):
    return (task for task in task_list if keyword.lower() in task.lower())

display_tasks(tasks)

filter_tasks(tasks, "project")

project_tasks = task_generator(tasks, "project")
print(next(project_tasks))