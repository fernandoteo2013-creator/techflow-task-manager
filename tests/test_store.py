from uuid import uuid4
from src.models import Task, TaskStatus, TaskPriority
from src.store import TaskStore

def test_create_task():
    store = TaskStore()
    task = Task(title="Test Task", description="Testing creation", priority=TaskPriority.HIGH, assignee="Fernanda")
    created = store.create_task(task)
    
    assert created.title == "Test Task"
    assert created.status == TaskStatus.TODO
    assert created.assignee == "Fernanda"  # Verificando o campo da Mudança de Escopo

def test_update_status():
    store = TaskStore()
    task = Task(title="Status Task", description="Testing status update")
    store.create_task(task)
    
    updated = store.update_status(task.id, TaskStatus.IN_PROGRESS)
    assert updated.status == TaskStatus.IN_PROGRESS

def test_delete_task():
    store = TaskStore()
    task = Task(title="Delete Task", description="Testing deletion")
    store.create_task(task)
    
    success = store.delete_task(task.id)
    assert success == True
    assert store.get_task(task.id) is None
