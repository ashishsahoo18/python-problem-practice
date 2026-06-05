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