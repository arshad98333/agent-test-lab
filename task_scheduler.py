import asyncio
import heapq
from datetime import datetime, timedelta

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, run_after_seconds):
        run_time = datetime.now() + timedelta(seconds=run_after_seconds)
        # Use heapq to store tasks sorted by run_time efficiently
        heapq.heappush(self.tasks, (run_time, name))

    async def run(self):
        while self.tasks:
            # Peek at the earliest task without removing it yet
            run_time, name = self.tasks[0]
            now = datetime.now()
            
            wait_seconds = (run_time - now).total_seconds()
            
            if wait_seconds > 0:
                # Use asyncio.sleep for non-blocking wait
                await asyncio.sleep(wait_seconds)
            
            # Remove the task from the heap and execute
            heapq.heappop(self.tasks)
            print(f"Running task: {name} at {datetime.now()}")

async def main():
    scheduler = TaskScheduler()
    scheduler.add_task("backup", 1)
    scheduler.add_task("cleanup", 2)
    scheduler.add_task("email", 3)
    await scheduler.run()

if __name__ == "__main__":
    asyncio.run(main())