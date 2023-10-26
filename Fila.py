class Queue:
    def __init__(self):
        self.queue = []
        self.max_size = 10

    def enqueue_front(self, item):
        if len(self.queue) < self.max_size:
            self.queue.insert(0, item)
            return "Item adicionado no início!"
        else:
            return "A fila está cheia!"

    def enqueue_back(self, item):
        if len(self.queue) < self.max_size:
            self.queue.append(item)
            return "Item adicionado no final!"
        else:
            return "A fila está cheia!"

    def dequeue_front(self):
        if len(self.queue) > 0:
            return f"Item removido do início: {self.queue.pop(0)}."
        else:
            return "A fila está vazia!"

    def dequeue_back(self):
        if len(self.queue) > 0:
            return f"Item removido do final: {self.queue.pop()}."
        else:
            return "A fila está vazia!"

    def size(self):
        return len(self.queue)

    def first(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return "A fila está vazia!"

    def last(self):
        if len(self.queue) > 0:
            return self.queue[-1]
        else:
            return "A fila está vazia!"