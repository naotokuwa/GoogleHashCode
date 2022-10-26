from Input import Input
from Row import Row
from Server import Server


class Score:
    def __init__(self, file_path, input_info: Input):

        with open(file_path) as f:
            self.file = f.readlines()

        self.rows = input_info.rows
        self.columns = input_info.columns
        self.number_of_unavailable_slots = input_info.number_of_unavailable_slots
        self.unavailable_slots = input_info.unavailable_slots
        self.number_of_pools = input_info.number_of_pools
        self.number_of_servers = input_info.number_of_servers
        self.servers = input_info.servers

        # Assign each server to a specified row from a file
        self.servers_by_row = [Row() for _ in range(self.rows)]

        self.convert_file_to_servers_by_row()

    def convert_file_to_servers_by_row(self):
        # When all servers are not covered
        if len(self.file) != len(self.servers):
            raise "Number of servers and number of servers in a file is different"

        for server_index, server_info in enumerate(self.file):
            server_info_list = server_info.split()

            if len(server_info_list) == 3:
                row_index, first_index, pool_index = map(int, server_info_list)
                server_info = self.servers[server_index]

                server = Server(server_info[0], server_info[1])
                server.pool_index = pool_index
                server.row_index = row_index
                server.first_index = first_index

                # Add a server to a row
                self.servers_by_row[row_index].add_server(server)

            elif len(server_info_list) == 1:
                continue
            else:
                raise "Number of columns in a file is wrong."

    def calculate_score(self):
        pool_capacity = [[0] * self.number_of_pools for _ in range(self.rows)]
        for remove_index in range(self.rows):
            for row_index in range(self.rows):
                if remove_index == row_index:
                    continue

                row = self.servers_by_row[row_index]
                for pool_index in range(self.number_of_pools):
                    pool_capacity[remove_index][pool_index] += row.sum_of_capacity_by_pool(pool_index)
        score = float("INF")
        for remove_index in range(self.rows):
            for pool_index in range(self.number_of_pools):
                score = min(pool_capacity[remove_index][pool_index], score)

        for row in pool_capacity:
            print(*row)
        return score

