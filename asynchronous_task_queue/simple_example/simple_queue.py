# If you need more control over the queue or need to share data between multiple processes, use Queue, instead of Pool
# multiprocessing.Queue is similar with queue.Queue, but it is designed for interprocess communication.

import multiprocessing


def run():
    books = [
        'pride-and-prejudice.txt',
        'heart-of-darkness.txt',
        'frankenstein.txt',
        'dracula.txt'
    ]
    queue = multiprocessing.Queue()

    print('Enqueuing...')
    for book in books:
        print(book)
        queue.put(book)

    print('\nDequeueing...')
    while not queue.empty():
        print(queue.get())


if __name__ == "__main__":
    run()
