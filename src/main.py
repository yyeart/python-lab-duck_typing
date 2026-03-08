import random

from src.receiver import TaskReceiver
from src.sources.api_source import ApiSource
from src.sources.file_source import FileSource
from src.sources.gen_source import GeneratorSource
from src.setup_logger import logger

def main() -> None:
    receiver = TaskReceiver()

    sources = [
        FileSource("src\\sources\\input.json"),
        GeneratorSource(random.randint(3, 10)),
        ApiSource()
    ]

    logger.info('Начало сбора задач...')
    receiver.receive_tasks(sources)
    result = receiver.get_received_tasks()
    logger.info(f'Сбор завершен. Всего задач: {len(result)}')

    print('Список задач:')
    for task in result:
        print(task)

if __name__ == '__main__':
    main()
