x = {}
def add_to_dict(x):
    key = input("Key: ")
    value = input("Value: ")
    if key in x:
        print("Error. Key already exists.")
        return x
    else:
        x[key] = value
        return x

add_to_dict(x)
print(x)