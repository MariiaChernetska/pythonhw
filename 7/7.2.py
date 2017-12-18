import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")

args = parser.parse_args()
answer = args.square**2
print(answer)