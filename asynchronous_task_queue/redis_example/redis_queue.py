import uuid
import pickle


class SimpleQueue(object):
    def __init__(self, conn, name):
        self.conn = conn    # act as a queue
        self.name = name    # act as a key in Redis?

    def enqueue(self, func, *args):
        task = SimpleTask(func, *args)
        serialized_task = pickle.dumps(task, protocol=pickle.HIGHEST_PROTOCOL)
        self.conn.lpush(self.name, serialized_task)     #.lpush(): prepend elements to a list
        return task.id

    def dequeue(self):
        _, serialized_task = self.conn.brpop(self.name) # .brpop(): blocks the connection until a value exists to be popped.
        task = pickle.loads(serialized_task)
        task.process_task()
        return task

    def get_length(self):   # get length of a queue
        return self.conn.llen(self.name)


class SimpleTask(object):
    def __init__(self, func, *args):
        self.id = str(uuid.uuid4())
        self.func = func
        self.args = args

    def process_task(self):
        self.func(*self.args)
