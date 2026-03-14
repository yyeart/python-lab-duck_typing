from src.constants import SOURCES
from src.receiver import TaskReceiver
from src.logger.setup_logger import logger

def main() -> None:
    """
    Главный модуль запуска приложения.

    :returns: Ничего не возвращает.
    """
    receiver = TaskReceiver()

    logger.info('Начало сбора задач...')
    receiver.receive_tasks(SOURCES)
    result = receiver.get_received_tasks()
    logger.info(f'Сбор завершен. Всего задач: {len(result)}')

    print('Список задач:')
    for task in result:
        print(task)

if __name__ == '__main__':
    main()
