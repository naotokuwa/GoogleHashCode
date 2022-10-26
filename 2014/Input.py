class Input:
    def __init__(self, input_file_path):
        with open(input_file_path) as f:
            file = f.readlines()

        # Input first line
        r, s, u, p, m = map(int, file[0].split())
        self.file = file[1:]

        self.rows = r
        self.columns = s
        self.number_of_unavailable_slots = u
        self.unavailable_slots = []
        self.number_of_pools = p
        self.number_of_servers = m
        self.servers = []
        self.get_unavailable_slots()
        self.get_servers()

    def get_unavailable_slots(self):
        for i in range(self.number_of_unavailable_slots):
            row = self.file[i]
            self.unavailable_slots.append(list(map(int, row.split())))
        self.file = self.file[self.number_of_unavailable_slots:]

    def get_servers(self):
        for i in range(self.number_of_servers):
            row = self.file[i]
            self.servers.append(list(map(int, row.split())))
        self.file = self.file[self.number_of_servers:]