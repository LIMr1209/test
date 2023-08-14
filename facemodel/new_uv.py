data = []
with open("uvcoords.txt", "r") as f:
    for i in f:
        xy = i.split()
        data.append({"x": float(xy[0]), "y": float(xy[1])})


uv_data = []

for index1, i in enumerate(data):
    for index2, j in enumerate(data):
        if i == j and index1 != index2:
            uv_data.append((i, j))

print(uv_data)