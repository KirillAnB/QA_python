import sys, argparse

params = argparse.ArgumentParser()

params.add_argument('--type', action='store', default='42', help='The Ultimate answer')

my_args = params.parse_args()
print(my_args)
