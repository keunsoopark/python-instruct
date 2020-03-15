# Run task in parallel using them multiprocessing library

import time
import multiprocessing

from tasks import get_word_counts


PROCESSES = multiprocessing.cpu_count() - 1


def run():
    print(f'Running with {PROCESSES} processes!')
    start = time.time()
    with multiprocessing.Pool(PROCESSES) as p:
        p.map_async(get_word_counts, [
            'pride-and-prejudice.txt',
            'heart-of-darkness.txt',
            'frankenstein.txt',
            'dracula.txt'
        ])
        # cleanup -> Without .close() and .join(), garbage collection may not occur.
        p.close()   # .close() tells the pool not to accept any new task.
        p.join()    # .join() tells the pool to exit after task have completed.
    print(f'Time taken = {time.time() - start:.10f}')


if __name__ == "__main__":
    run()
