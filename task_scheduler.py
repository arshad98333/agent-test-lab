# task_scheduler.py

import time
from datetime import datetime, timedelta


class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, run_after_seconds):
        run_time = datetime.now() + timedelta(seconds=run_after_seconds)
        self.tasks.append({"name": name, "run_time": run_time})

    def run(self):
        while self.tasks:
            now = datetime.now()
            pending_tasks = []
            for task in self.tasks:
                if task["run_time"] <= now:
                    print(f"Running task: {task["name"]} at {now}")
                else:
                    pending_tasks.append(task)
            self.tasks = pending_tasks


if __name__ == "__main__":
    scheduler = TaskScheduler()
    scheduler.add_task("backup", 1)
    scheduler.add_task("cleanup", 2)
    scheduler.add_task("email", 3)
    scheduler.run()