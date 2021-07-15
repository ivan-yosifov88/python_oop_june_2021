from to_do_list.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        filtered_tasks = [task for task in self.tasks if task.name == task_name]
        if not filtered_tasks:
            return f"Could not find task with the name {task_name}"

        current_task = filtered_tasks[0]
        current_task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        not_completed_tasks = [task for task in self.tasks if not task.completed]
        amount_of_removed_tasks = len([task for task in self.tasks if task.completed])
        self.tasks = not_completed_tasks
        return f"Cleared {amount_of_removed_tasks} tasks."

    def view_section(self):
        result = ""
        result += f"Section {self.name}:\n"
        for task in self.tasks:
            result += f"{task.details()}\n"

        return result


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
