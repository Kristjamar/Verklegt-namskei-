import csv



with open("Crew.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        for i in row:
            print("|  {:25} | ".format(i))
            #print("# 1.{:24} #".format(""))
        print("##############################")