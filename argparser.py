import argparse

parser = argparse.ArgumentParser()

parser.add_argument("first_number", type=int)
parser.add_argument("second_number", type=int)

args = parser.parse_args()
print("args: {}".format(args))
print("args: {}".format(args))
print("Sum: {}".format(args.first_number+args.second_number))