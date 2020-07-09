# import requests
# from contextlib import closing
# import csv
# import json

# url = "https://covidtracking.com/api/v1/states/ca/20200305.csv"
# print(r.status_code)

# r = requests.get(url)
# text = r.iter_lines()
# reader = csv.reader(text, delimiter=',')


import csv
import requests
import datetime

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)


def getHistoricData(BASE_URL, file_type, file_location, start_date, end_date):
    for single_date in daterange(start_date, end_date):
        
        print(single_date.strftime("%Y-%m-%d"))
        CSV_URL = "{}{}.{}".format(BASE_URL, single_date.strftime("%Y%m%d"), file_type)
        myfile = requests.get(CSV_URL)
        open("{}{}.csv".format(file_location, single_date.strftime("%Y%m%d")), 'wb').write(myfile.content)

BASE_URL = "https://covidtracking.com/api/v1/states/oh/"
file_type = "csv"
relative_file_location = "CovidTrackingProject/Daily/State/"
start_date = datetime.date(2020, 3, 5)
end_date = datetime.date.today()

getHistoricData(BASE_URL, file_type, relative_file_location, start_date, end_date)

# CSV_URL = "{}{}.csv".format(BASE_URL, FILE_NUM)

# ofile  = open('ttest.csv', "wb")
# writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

# myfile = requests.get(CSV_URL)
# open("{}.csv".format(FILE_NUM), 'wb').write(myfile.content)
# with requests.Session() as s:
#     download = s.get(CSV_URL)


#     decoded_content = download.content.decode('utf-8')

#     cr = csv.reader(decoded_content.splitlines(), delimiter=',')
#     my_list = list(cr)
#     for row in my_list:
#         # for row in my_list:
#         writer.writerow(row)
#         print(row)
 
# ofile.close()