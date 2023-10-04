class Node:
    def __init__(self, value):
        self.value = value  # Valor do nó
        self.next = None  # Próximo nó na lista

class LinkedList:
    def __init__(self):
        self.head = None  # Primeiro nó da lista
        self.tail = None  # Último nó da lista

    def insert(self, value):
        new_node = Node(value)  # Cria um novo nó
        if not self.head:  # Se a lista estiver vazia
            self.head = new_node  # O novo nó é a cabeça e a cauda da lista
            self.tail = new_node
        else:  # Se a lista não estiver vazia
            self.tail.next = new_node  # Adiciona o novo nó no final da lista
            self.tail = new_node  # Atualiza a cauda da lista

    def insert_at_position(self, value, position):
        new_node = Node(value)  # Cria um novo nó
        if position == 0:  # Se a posição for 0
            new_node.next = self.head  # O novo nó aponta para a antiga cabeça da lista
            self.head = new_node  # A nova cabeça da lista é o novo nó
            if self.tail is None:
                self.tail = new_node  # Se a lista estava vazia, atualiza a cauda
        else:
            current = self.head  # Começa na cabeça da lista
            for _ in range(position - 1):  # Percorre a lista até a posição desejada
                if current is None:  # Se a posição não existir, retorna False
                    return False
                current = current.next  # Avança para o próximo nó
            if current is None:  # Se a posição não existir, retorna False
                return False
            new_node.next = current.next  # O novo nó aponta para o próximo nó da posição atual
            current.next = new_node  # O nó atual aponta para o novo nó
            if new_node.next is None:  # Se o novo nó for o último, atualiza a cauda
                self.tail = new_node

    def remove(self, value):
        if self.head is None:  # Se a lista estiver vazia, retorna
            return
        if self.head.value == value:  # Se o valor estiver na cabeça da lista
            self.head = self.head.next  # Remove o nó da cabeça
            if self.head is None or self.head.next is None:  # Atualiza a cauda se necessário
                self.tail = self.head
            return
        current = self.head
        while current.next and current.next.value != value:  # Percorre a lista até encontrar o valor
            current = current.next
        if current.next is not None:  # Se encontrou o valor
            current.next = current.next.next  # Remove o nó com o valor
            if current.next is None:  # Atualiza a cauda se necessário
                self.tail = current

    def remove_at_position(self, position):
        if position == 0 and self.head is not None:  # Se a posição for 0 e a lista não estiver vazia
            removed_value = self.head.value  # Armazena o valor do nó a ser removido
            self.head = self.head.next  # Remove o nó da cabeça
            if self.head is None or self.head.next is None:  # Atualiza a cauda se necessário
                self.tail = self.head
            return removed_value  # Retorna o valor removido
        else:  # Se a posição não for 0
            current = self.head  # Começa na cabeça da lista
            for _ in range(position - 1):  # Percorre a lista até a posição desejada
                if current is None:  # Se a posição não existir, retorna None
                    return None
                current = current.next  # Avança para o próximo nó
            if current is None or current.next is None:  # Se a posição não existir, retorna None
                return None
            removed_value = current.next.value  # Armazena o valor do nó a ser removido
            current.next = current.next.next  # Remove o nó na posição desejada
            if current.next is None:  # Atualiza a cauda se necessário
                self.tail = current

    def search(self, value):
        current = self.head  # Começa na cabeça da lista
        position = 0  # Inicializa a posição como 0
        while current:  # Percorre a lista até encontrar o valor ou chegar ao final da lista
            if current.value == value:  # Se encontrou o valor, retorna a posição atual
                return position
            position += 1  # Incrementa a posição
            current = current.next  # Avança para o próximo nó
        return -1  # Se não encontrou o valor, retorna -1

