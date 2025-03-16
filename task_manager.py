from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, due_date):
        due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        self.tasks.append({"name": name, "due_date": due_date, "status": "Pending"})

    def mark_complete(self, name):
        for task in self.tasks:
            if task["name"] == name:
                task["status"] = "Complete"

    def get_overdue_tasks(self):
        today = datetime.now().date()
        return [task for task in self.tasks if task["due_date"] > today and task["status"] == "Pending"]