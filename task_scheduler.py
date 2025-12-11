import datetime

class TaskScheduler:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 0

    def add_task(self, description, due_date=None):
        self.task_id_counter += 1
        task = {
            "id": self.task_id_counter,
            "description": description,
            "due_date": due_date,
            "status": "pending"
        }
        self.tasks.append(task)
        print(f"Task added: ID {task["id"]} - {task["description"]}")
        return task

    def list_tasks(self, status=None):
        if not self.tasks:
            print("No tasks scheduled.")
            return []

        filtered_tasks = []
        print("\n--- Scheduled Tasks ---")
        for task in self.tasks:
            if status is None or task["status"] == status:
                filtered_tasks.append(task)
                due_date_str = task["due_date"].strftime("%Y-%m-%d") if task["due_date"] else "N/A"
                print(f"ID: {task["id"]}, Description: {task["description"]}, Due: {due_date_str}, Status: {task["status"]}")
        print("----------------------")
        return filtered_tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "completed"
                print(f"Task ID {task_id} marked as completed.")
                return True
        print(f"Task ID {task_id} not found.")
        return False

if __name__ == "__main__":
    scheduler = TaskScheduler()

    # Add some tasks
    scheduler.add_task("Write initial code for math_bug.py", datetime.date(2025, 12, 12))
    scheduler.add_task("Review project requirements")
    scheduler.add_task("Implement task scheduler logic", datetime.date(2025, 12, 15))

    # List all tasks
    scheduler.list_tasks()

    # Complete a task
    scheduler.complete_task(1)

    # List pending tasks
    scheduler.list_tasks(status="pending")