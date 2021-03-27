import re
import sys

REGEX = re.compile("")

def process_regex(regex, input_str):
  return regex.search(input_str).group(1).strip()

if __name__ == "__main__":
  if len(sys.argv) < 2:
    sys.exit(0)
  REGEX = re.compile(sys.argv[1])
  for s in sys.argv[2:]:
    print(process_regex(REGEX, s))
