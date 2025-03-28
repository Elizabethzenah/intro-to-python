import csv

# Open the CSV file
with open("data.csv", newline='r') as csvfile:
       reader = csv.reader(csvfile)
       for row in reader:
          print(row)

#pip install --upgrade pip




