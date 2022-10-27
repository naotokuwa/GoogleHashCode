from Server import Server
from Input import Input


class Solver:
    def __init__(self, input_info: Input):
        self.UNAVAILABLE = "x"
        self.AVAILABLE = "o"

        self.input = input_info
        self.rows = input_info.rows
        self.columns = input_info.columns
        self.unavailable_slots = input_info.number_of_unavailable_slots
        self.number_of_pools = input_info.number_of_pools
        self.numer_of_servers = input_info.number_of_servers
        self.servers = []
        self.grids = [[self.AVAILABLE] * self.columns for _ in range(self.rows)]
        self.put_unavailable_slots()
        self.extract_server_info()

    def put_unavailable_slots(self):
        for row, column in self.input.unavailable_slots:
            self.grids[row][column] = self.UNAVAILABLE

    def extract_server_info(self):
        for i in range(self.numer_of_servers):
            size, capacity = self.input.servers[i]
            server = Server(size, capacity)
            server.index = i
            self.servers.append(server)

    # What I want, find a server which I can put into a specific row
    def assign_servers(self):
        for _ in range(30):
            for row_index in range(self.rows):
                server_index, first_index = self.find_server_fit_with_row(row_index)

                if server_index >= 0:
                    self.servers[server_index].is_used = True
                    self.servers[server_index].row_index = row_index
                    self.servers[server_index].first_index = first_index
                    self.assign_server_to_row(server_index)

    def find_server_fit_with_row(self, row_index):
        for server_index, server in enumerate(self.servers):
            size, capacity, is_used = server.size, server.capacity, server.is_used
            if is_used:
                continue
            first_index = self.get_first_index_of_consecutive_true(row_index, size)

            if first_index >= 0:
                return server_index, first_index
        return -1, -1

    def assign_server_to_row(self, server_index):
        first_index = self.servers[server_index].first_index
        last_index = first_index + self.servers[server_index].size
        row_index = self.servers[server_index].row_index

        for column in range(first_index, last_index):
            self.grids[row_index][column] = server_index

    def get_first_index_of_consecutive_true(self, row_index, target_size):
        row = self.grids[row_index]
        start_index = -1
        consecutive_size = 0

        for i in range(self.columns):
            if row[i] == self.AVAILABLE:
                consecutive_size += 1

                if consecutive_size == target_size:
                    return start_index

                if start_index == -1:
                    start_index = i
            else:
                start_index = -1
                consecutive_size = 0
        return -1

    def assign_pool(self):
        pool_capacity = [[0] * self.number_of_pools for _ in range(self.rows)]

        for server_index, server in enumerate(self.servers):
            min_pool_index = self.get_min_pool_capacity(pool_capacity)
            self.servers[server_index].pool_index = min_pool_index

            for row_index in range(self.rows):
                if row_index == server.row_index:
                    continue
                pool_capacity[row_index][min_pool_index] += server.capacity

    # Get minimum pool and assign server to them
    def get_min_pool_capacity(self, pool_capacity):
        global_min = float("INF")
        min_pool_index = -1

        for remove_index in range(self.rows):
            for pool_index in range(self.number_of_pools):
                if global_min > pool_capacity[remove_index][pool_index]:
                    global_min = pool_capacity[remove_index][pool_index]
                    min_pool_index = pool_index
        return min_pool_index

    def print_grids(self):
        for row in self.grids:
            print(*row)

    def output_to_file(self, file_path):
        self.servers.sort(key=lambda x: x.capacity, reverse=True)
        self.assign_servers()
        self.assign_pool()
        self.servers.sort(key=lambda x: x.index, reverse=False)

        with open(file_path, "w") as f:
            for server in self.servers:
                if server.is_pool():
                    result = str(server.row_index) + " " + str(server.first_index) + " " + str(server.pool_index) + "\n"
                    f.writelines(result)
                else:
                    f.writelines("x\n")