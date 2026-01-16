# Print a multiplication table

rows = int(input())
cols = int(input())
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(i * j, end="\t")
    print()
