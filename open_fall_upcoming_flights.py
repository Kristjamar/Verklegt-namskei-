def get_upcoming_flights():
    filename = "upcomingflights.csv"
    try:
        file_object = open(filename, "r")
        return file_object 
    except FileNotFoundError:
        print("Filename {} not found!".format(filename))

def make_list(file_object):
    listinn = []
    for line in file_object:
        listinn.append(line.split(","))
    return listinn

def print_list(listinn):
    for line in listinn:
        print(line)

def main():
    file_object = get_aircraft()
    listinn = make_list(file_object)
    print(listinn)
main()