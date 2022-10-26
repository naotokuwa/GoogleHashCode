class Server:
    def __init__(self, size, capacity):
        self.size = size
        self.capacity = capacity
        self.is_used = False
        self.row_index = -1
        self.first_index = -1
        self.pool_index = -1

    def is_pool(self):
        return self.pool_index >= 0
