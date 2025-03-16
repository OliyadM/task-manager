from task_manager import TaskManager
def test_overdue_tasks():
    tm = TaskManager()
    tm.add_task("Old Task", "2020-01-01")
    overdue = tm.get_overdue_tasks()
    assert len(overdue) == 1 

def test_invalid_date():
    tm = TaskManager()
    tm.add_task("Invalid Task", "Oct 31, 2023")  
    assert len(tm.tasks) == 0  