import csv
import json
#change1

with open("employees.csv","r") as foo:
    readers = csv.DictReader(foo)

    for item in readers:
        if(int(item["SALARY"]) > int(9000)):
            json_data = {
                "Name": item["FIRST_NAME"] + item["LAST_NAME"].replace("" "",""    ""),
                "Email": item["EMAIL"],
                "Phone Number": item["PHONE_NUMBER"].replace(".","")
            }
            print(json_data)















