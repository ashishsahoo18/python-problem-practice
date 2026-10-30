# 7.Print this pattern
# 1
# 22
# 333
# 4444
# 55555

for i in range(1,6):
    print(str(i )*i)

# Right-aligned triangle
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

n= 5
for i in range(1,n+1):
    print("  "*(n-i)+"* "*i)