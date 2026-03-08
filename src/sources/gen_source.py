import random

from src.core.models import Task
from src.setup_logger import logger

class GeneratorSource:
    def __init__(self, task_cnt: int):
        self.task_cnt = task_cnt

    def get_tasks(self) -> list[Task]:
        print("Генерация случайных задач...")
        try:
            tasks = [Task(id=random.randint(100, 1000),
                     payload=f'Payload {i}') for i in range(self.task_cnt)]
            logger.info(f'Сгенерировано {self.task_cnt} задач')
            return tasks
        except Exception as e:
            logger.error(f'Ошибка генерации задач: {e}')
            return []

    def __repr__(self) -> str:
        return 'Генератор'
