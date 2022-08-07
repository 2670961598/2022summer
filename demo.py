import random
# 6724  6889
row = 8
col = 8
with open("data.csv", "w") as f:
    f.write("\n")
    for i in range(row):
        for j in range(col):
            if j == col - 1:
                f.write("1")
            else:
                f.write("1,")
        f.write("\n")