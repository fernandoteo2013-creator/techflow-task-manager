from typing import List, Optional
from uuid import UUID
from .models import Task, TaskStatus

class TaskStore:
    def __init__(self):
        self.tasks: dict[UUID, Task] = {}

    def list_tasks(self, status: Optional[TaskStatus] = None) -> List[Task]:
        if status:
            return [t for t in self.tasks.values() if t.status == status]
        return list(self.tasks.values())

    def get_task(self, id: UUID) -> Optional[Task]:
        return self.tasks.get(id)

    def create_task(self, task: Task) -> Task:
        self.tasks[task.id] = task
        return task

    def update_status(self, id: UUID, status: TaskStatus) -> Optional[Task]:
        if id in self.tasks:
            self.tasks[id].status = status
            return self.tasks[id]
        return None

    def delete_task(self, id: UUID) -> bool:
        if id in self.tasks:
            del self.tasks[id]
            return True
        return False

# Instancia global para usar en la API
task_store = TaskStore()
