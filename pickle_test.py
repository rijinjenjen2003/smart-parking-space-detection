import pickle

names = [
    "Rijin",
    "OpenCV",
    "Parking"
]

with open("data.pkl", "wb") as file:

    pickle.dump(names, file)

print("Saved!")