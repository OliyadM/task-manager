from datetime import datetime
from task_manager import TaskManager

def test_add_task():
    tm = TaskManager()
    tm.add_task("Homework", "2023-11-10")
    assert len(tm.tasks) == 1

def test_overdue_tasks():
    tm = TaskManager()
    tm.add_task("Old Task", "2020-01-01")  
    overdue = tm.get_overdue_tasks()
    assert len(overdue) == 0  