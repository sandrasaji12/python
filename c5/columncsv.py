import csv
with open("csv3.csv", newline='') as csvfile:
    d = csv.DictReader(csvfile)
    print("ROLL NO STUDENT NAME")
    print("--------------------")
    for i in d:
        print(i['RollNo'], i['Name'])