from Input import Input
from Solver import Solver


def main():
    input_file = Input("/Users/naotokuwayama/PycharmProjects/GoggleHashCode/2014/easy.in")
    print(input_file.servers)
    solver = Solver(input_file)
    solver.output_to_file("/Users/naotokuwayama/PycharmProjects/GoggleHashCode/2014/output.txt")
    solver.print_grids()

if __name__ == '__main__':
    main()
