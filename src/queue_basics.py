import queue
from collections import deque
import threading


# ---------------------------------------------------------------------
# list
# Pythonのlistは内部的にはCの配列で実装されているため、この方法はおそい
# ---------------------------------------------------------------------

q = []

queue_len = 5

for i in range(queue_len):
    q.append(i + 1)

for i in range(queue_len):
    v = q.pop(0)
    print(f' value : {v}')


# ---------------------------------------------------------------------
# queue.Queue
# 同期キュークラス。スレッドセーフな実装
# put()とget()を利用
# スレッドセーフを実現するためにややオーバーヘッドがあるため、dequeよりは遅い
# ---------------------------------------------------------------------

q = queue.Queue()

queue_len = 5

for i in range(queue_len):
    q.put(i + 1)

for i in range(queue_len):
    v = q.get()
    print(f' value : {v}')


# --> next q.get() will be hanged ...



q = queue.Queue()

queue_len = 5

for i in range(queue_len):
    q.put(i + 1)

# キューからデータがなくなるまで取り出しを行う
while not q.empty():
    print(q.get())


# ---------------------------------------------------------------------
# collections.deque()
# deque は double-ended queueの略で、デックと読みます。
# append()とpopleft()でキューを実現します。
# 両端が終端のため、キューとしてもスタックとしても使えて便利、高速。
# ただし、スレッドセーフではありません。
# ---------------------------------------------------------------------

q = deque()

queue_len = 5

for i in range(queue_len):
    q.append(i + 1)

for i in range(queue_len):
    v = q.popleft()
    print(f' value : {v}')
