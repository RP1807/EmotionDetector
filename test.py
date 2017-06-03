import csv
f_obj = open("DS3.csv", "rb")
reader = csv.DictReader(f_obj)
for row in reader:
    print row["Tweet"]
