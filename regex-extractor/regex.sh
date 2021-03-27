REGEX=$1
shift

for s in "$@"; do
  printf "$s" | sed -E "s/$REGEX/\\1/"
done
