import Busq_prof as b_p

class Queue:
    def __init__(self) -> None:
        self.items=[]
    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def alg_busq1():
    cola=Queue()
    