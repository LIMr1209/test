import json

pos = {"data": [
    {"x": 0.029735, "y": 0.038610, "z": 0.094317},
    {"x": 0.039696, "y": 0.042117, "z": 0.088268},
    {"x": 0.030474, "y": 0.038146, "z": 0.095834},
    {"x": 0.020601, "y": 0.039115, "z": 0.096496},
    {"x": 0.011862, "y": 0.040909, "z": 0.094007},
    {"x": -0.025999, "y": 0.041058, "z": 0.092027},
    {"x": -0.035057, "y": 0.038791, "z": 0.093742},
    {"x": -0.044424, "y": 0.038339, "z": 0.090965},
    {"x": -0.053344, "y": 0.042629, "z": 0.084029},
    {"x": -0.034477, "y": 0.038675, "z": 0.092589},
    {"x": -0.044003, "y": 0.038192, "z": 0.090919},
]}

name = {"data": [
    "eye_l",
    "eye_l1",
    "eye_l2",
    "eye_l3",
    "eye_l4",
    "eye_l5",
    "eye_r",
    "eye_r1",
    "eye_r2",
    "eye_r3",
    "eye_r4",
    "eye_r5",
]}

data = []

for index, i in enumerate(name["data"]):
    data.append({
        "name": i,
        "world_position": pos["data"][index]
    })

print(json.dumps(data))

# def get_data(filename):
#     data = []
#     with open(filename, "r") as f:
#         for i in f:
#             t = i.split()
#             data.append({
#                 "name": t[0],
#                 "world_position": {"x": float(t[1]), "y": float(t[2]), "z": float(t[3])}
#             })
#     return data
#
# if __name__ == '__main__':
#     data = get_data("_out___/eye_close.txt")
#     print(data)
