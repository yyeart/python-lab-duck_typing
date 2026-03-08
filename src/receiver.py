from typing import Any

from src.core.models import Task
from src.core.contract import TaskSource
from src.setup_logger import logger

class TaskReceiver:
    def __init__(self):
        self._tasks: list[Task] = []

    def receive_tasks(self, sources: list[Any]) -> None:
        for src in sources:
            if isinstance(src, TaskSource):
                try:
                    new_tasks = src.get_tasks()
                    self._tasks.extend(new_tasks)
                    logger.info(f'Принято {len(new_tasks)} задач от <{src}>')
                except Exception as e:
                    logger.error(f'{src} вызвал исключение: {e}')
            else:
                logger.warning(f'Ошибка: {src} не соответствует контракту')

    def get_received_tasks(self) -> list[Task]:
        return self._tasks
