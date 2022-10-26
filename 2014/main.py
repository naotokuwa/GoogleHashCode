from Server import Server


class GoogleHashCode:
    def __init__(self):
        self.UNAVAILABLE = "x"
        self.AVAILABLE = "o"

        with open("2014/dc.in") as f:
            file = f.readlines()

        # Input first line
        r, s, u, p, m = map(int, file[0].split())
        self.file = file[1:]

        self.rows = r
        self.columns = s
        self.unavailable_slots = u
        self.number_of_pools = p
        self.numer_of_servers = m
        self.servers = []
        self.grids = [[self.AVAILABLE] * s for _ in range(r)]
        self.put_unavailable_slots()
        self.extract_server_info()

    def put_unavailable_slots(self):
        for i in range(self.unavailable_slots):
            row, column = map(int, self.file[i].split())
            self.grids[row][column] = self.UNAVAILABLE

    def extract_server_info(self):
        for i in range(self.unavailable_slots, self.unavailable_slots + self.numer_of_servers):
            size, capacity = map(int, self.file[i].split())
            server = Server(size, capacity)
            self.servers.append(server)

    # What I want, find a server which I can put into a specific row
    def assign_servers(self):
        for _ in range(30):
            for row_index in range(self.rows):
                server_index, first_index = self.find_server_fit_with_row(row_index)

                if server_index >= 0:
                    self.assign_server_to_row(row_index, first_index, server_index)
                    self.servers[server_index].is_used = True
                    self.servers[server_index].row_index = row_index
                    self.servers[server_index].first_index = first_index

    def find_server_fit_with_row(self, row_index):
        for server_index in range(self.numer_of_servers):
            server = self.servers[server_index]
            size, capacity, is_used = server.size, server.capacity, server.is_used
            if is_used:
                continue
            first_index = self.get_first_index_of_consecutive_true(row_index, size)

            if first_index >= 0:
                return server_index, first_index
        return -1, -1

    def assign_server_to_row(self, row_index, first_index, server_index):
        for i in range(first_index, first_index + self.servers[server_index].size):
            self.grids[row_index][i] = server_index

    def get_first_index_of_consecutive_true(self, row_index, target_size):
        row = self.grids[row_index]
        start_index = -1
        consecutive_size = 0

        for i in range(len(row)):
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
        for server_index in range(len(self.servers)):
            if self.servers[server_index].row_index >= 0:
                server = self.servers[server_index]
                server.pool_index = server_index % self.number_of_pools

    def output(self):
        self.assign_servers()
        self.assign_pool()

        with open("output.txt", "w") as f:
            for server in self.servers:
                if server.pool_index >= 0:
                    result = str(server.row_index) + " " + str(server.first_index) + " " + str(server.pool_index) + "\n"
                    f.writelines(result)
                else:
                    f.writelines("x\n")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solver = GoogleHashCode()
    solver.output()

