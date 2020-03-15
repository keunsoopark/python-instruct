
1. redis_queue.py creates new queues and tasks via the SimpleQueue and SimpleTask classes, respectively.

2. redis_queue_client.py enqueues new tasks.

3. redis_queue_worker.py dequeues and processes tasks.

4. redis_queue_server.py spawns worker processes.

run redis_queue_server.py and redis_queue_client.py in separate terminal windows.   
(Turn on redis server first with `redis-server` command.)
