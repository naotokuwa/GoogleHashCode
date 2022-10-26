class Score:
    def __init__(self, file_path, rows, columns, unavailable_slots, pools, servers):
        try:
            with open(file_path) as f:
                self.file = f.readlines()
        except RuntimeError as e:
            print("File is not found.")

        self.rows = rows
        self.columns = columns
        self.unavailable_slots = unavailable_slots
        self.number_of_pools = pools
        self.servers = servers
        self.convert_file_to_row()
        self.grids = []

    def convert_file(self):
        if len(self.file) != len(self.servers):
            raise "Number of servers and number of servers in a file is different"

        for server_info in self.file:
            server_info_list = server_info.split("")

            if len(server_info_list) == 3:
                try:
                    row_index, first_index, pool_index = map(int, server_info_list)
                except RuntimeError:
                    raise "A server info does contain integers."
            elif len(server_info_list) == 2:

            else:
                raise "Number of columns in a file is wrong."

