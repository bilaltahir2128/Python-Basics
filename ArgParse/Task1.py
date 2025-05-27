import argparse

parser = argparse.ArgumentParser(description="Take marks of three subjects as command line arguments.")

parser.add_argument('--physics', type=int, required=True, help='Marks in Physics')
parser.add_argument('--chemistry', type=int, required=True, help='Marks in Chemistry')
parser.add_argument('--maths', type=int, required=True, help='Marks in Maths')

args = parser.parse_args()

print("Physics Marks:", args.physics)
print("Chemistry Marks:", args.chemistry)
print("Maths Marks:", args.maths)
