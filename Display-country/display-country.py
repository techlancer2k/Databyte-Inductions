import csv
country_list = []
with open('data_csv.csv','r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        country_list.append(row)
country_code1 = input("Enter country code 1")
country_code2 = input("Enter country code 2")

sorted_list = sorted(country_list, key = lambda i: i['Name'])
display = 0
for country in sorted_list:

    if country['Code'] == country_code2:
        display = 0
    
    if(display):
        print(country['Name'])
    
    if country['Code'] == country_code1:
        display = 1
    if country['Code'] == country_code2:
        display = 0
    