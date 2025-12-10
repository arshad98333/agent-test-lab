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
            for task in list(self.tasks):
                if task["run_time"] <= now:
                    print(f"Running task: {task['name']} at {now}")
                    self.tasks.remove(task)
            time.sleep(0.2)


if __name__ == "__main__":
    scheduler = TaskScheduler()
    scheduler.add_task("backup", 1)
    scheduler.add_task("cleanup", 2)
    scheduler.add_task("email", 3)
    scheduler.run()
