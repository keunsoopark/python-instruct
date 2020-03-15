# Logging with multiprocessing library
# Log to console only

import os
import time
import logging
import multiprocessing

from tasks import get_word_counts


PROCESSES = multiprocessing.cpu_count() - 1
NUMBER_OF_TASKS = 10


def process_tasks(task_queue):
    logger = multiprocessing.get_logger()
    proc = os.getpid()
    while not task_queue.empty():
        try:
            book = task_queue.get()
            get_word_counts(book)
        except Exception as e:
            logger.error(e)
        logger.info(f'Process {proc} completed successfully')
    return True


def add_tasks(task_queue, number_of_tasks):
    for num in range(number_of_tasks):
        task_queue.put('pride-and-prejudice.txt')
        task_queue.put('heart-of-darkness.txt')
        task_queue.put('frankenstein.txt')
        task_queue.put('drackla.txt')   # intentional error
    return task_queue


def run():
    empty_task_queue = multiprocessing.Queue()
    full_task_queue = add_tasks(empty_task_queue, NUMBER_OF_TASKS)
    processes = []
    print(f'Running with {PROCESSES} processes!')
    start = time.time()
    for n in range(PROCESSES):
        p = multiprocessing.Process(target=process_tasks,
                                    args=(full_task_queue,))
        processes.append(p)
        p.start()   # to start running the processes
    print(f'len(processes): {len(processes)}')  # 3 processors handles 40 tasks
    for p in processes:
        p.join()    # to complete the processes
    print(f'Time taken = {time.time() - start:.10f}')


if __name__ == "__main__":
    # multiprocessing.log_to_stderr(logging.ERROR)  # idk what this line is doing
    run()

