x = [[1, 2],
     [4, 5],
     [7, 8]]

result = [[0, 0, 0],
          [0, 0, 0]]

# iterate through rows
for i in range(len(x)):
    for j in range(len(x[0])):
        result[j][i] = x[i][j]

for r in result:
    print(r)
