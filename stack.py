class Stack:
    def __init__(self):
        self.stack = []
        self.max_size = 10  # Adicionado aqui

    def push(self, value):
        if len(self.stack) < self.max_size:  # Adicionado aqui
            self.stack.append(value)
            return f"Valor {int(value)} empilhado com sucesso!"
        else:
            return "A pilha está cheia, não é possível empilhar mais valores."  # Adicionado aqui

    def pop(self):
        if not self.is_empty():
            return f"Valor desempilhado: {self.stack.pop()}."
        else:
            return "A pilha está vazia, não há valores para desempilhar."

    def peek(self):
        if not self.is_empty():
            return f"Valor no topo da pilha: {self.stack[-1]}."
        else:
            return "A pilha está vazia, não há valores no topo."

    def is_empty(self):
        return len(self.stack) == 0
