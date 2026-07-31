# 1.Print this pyramid
#     *
#    ***
#   *****
#  *******

rows = 4
for i in range(rows):
    spaces = rows -i -1
    stars = 2*i+1
    print(" " * spaces + "*" * stars)

# 2.print this pattern
#  *******
#   *****
#    ***
#     *
rows = 5
for i in range(rows):
    spaces = i
    stars = 2*(rows-i)-1
    print(" "* spaces + "*"* stars)
