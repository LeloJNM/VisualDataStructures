class SequentialList:
    def __init__(self, limit):
        self.list = []
        self.limit = limit

    def insert(self, value):
        if str(value).isdigit() and len(self.list) < self.limit:
            self.list.append(int(value))
   
    def insert_at_position(self, value, position):  
        if str(value).isdigit() and str(position).isdigit() and int(position) <= len(self.list) and len(self.list) < self.limit:
            self.list.insert(int(position), int(value))
   
    def remove(self, value):
        if str(value).isdigit() and int(value) in self.list:
            self.list.remove(int(value))

    def search(self, value):
        if str(value).isdigit() and int(value) in self.list:
            return self.list.index(int(value))
        return -1

    def remove_by_index(self, index):
        if str(index).isdigit() and int(index) < len(self.list):
            del self.list[int(index)]
