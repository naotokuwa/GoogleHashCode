from Input import Input
from Solver import Solver
from Score import Score

def main():
    INPUT_PATH = "/Users/naotokuwayama/PycharmProjects/GoggleHashCode/2014/dc.in"
    OUTPUT_PATH = "/Users/naotokuwayama/PycharmProjects/GoggleHashCode/2014/output.txt"

    input_file = Input(INPUT_PATH)
    solver = Solver(input_file)
    solver.output_to_file(OUTPUT_PATH)
    score = Score(OUTPUT_PATH, input_file)
    print(score.calculate_score())


if __name__ == '__main__':
    main()
