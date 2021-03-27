#!/usr/bin/env python3

import argparse
import itertools

def permute_strings(elements, prefix, suffix):
  output = set()
  for i in range(1, len(elements)):
    for s in itertools.permutations(elements, i):
      output.add("".join(s))
  return output


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Generate permutations on a string')
  parser.add_argument('-p', '--prefix', type=str, help='prefix preceeding all strings', required=False, default='')
  parser.add_argument('-s', '--suffix', type=str, help='suffix terminating all strings', required=False, default='')
  parser.add_argument('elements', type=str, nargs='+', help='strings that a ordered together')
  
  args = parser.parse_args()
  for s in permute_strings(args.elements, args.prefix, args.suffix):
    print(s)
