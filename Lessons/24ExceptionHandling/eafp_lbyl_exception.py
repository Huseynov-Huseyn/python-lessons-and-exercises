# LBYL = Look Before You Leap
data = {"name": "Huseyn"}
if "name" in data:
    print(data["name"])
else:
    print("cannot find!")

# EAFP = Easier to Ask Forgiveness than Permission
# Used for checking and executing at the same time
try:
    print(data["name"])
except KeyError:
    print("cannot find!")
