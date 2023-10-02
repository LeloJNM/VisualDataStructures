class SequentialList:
    def __init__(self, limit):
        self.list = []  # Inicializa a lista
        self.limit = limit  # Define o limite de elementos na lista

    def insert(self, value):
        # Insere o valor na lista se for um dígito e a lista não estiver cheia
        if str(value).isdigit() and len(self.list) < self.limit:
            self.list.append(int(value))

    def insert_at_position(self, value, position):
        """ Insere o valor em uma posição específica se ambos forem dígitos, a posição for válida
        e a lista não estiver cheia """
        if str(value).isdigit() and str(position).isdigit() and int(position) <= len(self.list) and len(
                self.list) < self.limit:
            self.list.insert(int(position), int(value))

    def remove(self, value):
        # Remove o valor da lista se for um dígito e estiver na lista
        if str(value).isdigit() and int(value) in self.list:
            self.list.remove(int(value))

    def search(self, value):
        # Procura o valor na lista e retorna o índice se for um dígito e estiver na lista
        if str(value).isdigit() and int(value) in self.list:
            return self.list.index(int(value))
        return -1  # Retorna -1 se o valor não for encontrado

    def remove_by_index(self, index):
        # Remove o elemento em um índice específico se for um dígito e o índice for válido
        if str(index).isdigit() and int(index) < len(self.list):
            del self.list[int(index)]
