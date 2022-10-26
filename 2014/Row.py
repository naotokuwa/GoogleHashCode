class Row:
    def __init__(self):
        # Each row contains a server
        self.servers = []

    def add_server(self, server):
        self.servers.append(server)

    def sum_of_capacity_by_pool(self, pool_index):
        sum_of_capacity = 0
        for server in self.servers:
            if server.is_pool() and server.pool_index == pool_index:
                sum_of_capacity += server.capacity

        return sum_of_capacity