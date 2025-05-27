import argparse

parser = argparse.ArgumentParser(description="Calculate average of subject marks.")

parser.add_argument('--physics', type=int, required=True, help='Marks in Physics')
parser.add_argument('--chemistry', type=int, required=True, help='Marks in Chemistry')
parser.add_argument('--maths', type=int, required=True, help='Marks in Maths')

args = parser.parse_args()

average = (args.physics + args.chemistry + args.maths) / 3

print(f"Average Marks: {average:.2f}")
