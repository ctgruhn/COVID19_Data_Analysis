import csv
import requests
import datetime

def dateRange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)


def getDailyStateHistoricData(API_URL, file_type, file_location, start_date, end_date):
    for single_date in dateRange(start_date, end_date):        
        FILE_URL = "{}{}.{}".format(BASE_URL, single_date.strftime("%Y%m%d"), file_type)
        myfile = requests.get(FILE_URL)
        open("{}{}.{}".format(file_location, single_date.strftime("%Y%m%d"), file_type), 'wb').write(myfile.content)

def getAPIData(Base_URL, file_name, file_type, file_location):
    myfile = requests.get(BASE_URL)
    open("{}/{}.{}".format(file_location, file_name, file_type), "wb").write(myfile.content)

BASE_URL = "https://covidtracking.com/api/v1/"
API_URL = {
    "ohioDaily": "{}states/oh/".format(BASE_URL),
    "usDaily": "{}us/".format(BASE_URL),
    "raceCombined": "{}states-combined/".format(BASE_URL),
    "raceSeparate": "{}states-separate/".format(BASE_URL),
}
file_type = "csv"

BASE_FILE_LOCATION = "CovidTrackingProject/"
FILE_LOCATION = {
    "ohioDaily": "{}Daily/State/".format(BASE_FILE_LOCATION),
    "usDaily": "{}Daily/US/".format(BASE_FILE_LOCATION),
    "raceCombined": "{}Race/".format(BASE_FILE_LOCATION),
    "raceSeparate": "{}Race/".format(BASE_FILE_LOCATION)
}
start_date = datetime.date(2020, 3, 5)
end_date = datetime.date.today()

race_files = {"combined": "states-combined", "separate": "states-separate"}

getDailyStateHistoricData(API_URL["ohioDaily"], file_type, FILE_LOCATION["ohioDaily"], start_date, end_date)
getDailyStateHistoricData(API_URL["usDaily"], file_type, FILE_LOCATION["usDaily"], start_date, end_date)
getAPIData(API_URL["raceSeparate"],race_files["separate"],file_type, FILE_LOCATION["raceSeparate"] )
getAPIData(API_URL["raceCombined"],race_files["combined"],file_type, FILE_LOCATION["raceCombined"] )
