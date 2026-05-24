import argparse

parse = argparse.ArgumentParser(description="Cat will Meow")
parse.add_argument("-n",default=1,type=int,help="number of times to Meow.")
args = parse.parse_args()

for _ in range(args.n):
    print("Meow")