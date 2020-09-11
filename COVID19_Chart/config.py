# Find newest file to determine appropriate START_DATE
import datetime
import os.path

def getStartDate():
    path = FILE_LOCATION["usDaily"]
    files = os.listdir(path)
    newest_file = os.path.splitext(max(files))
    last_update = datetime.datetime.strptime(newest_file[0], '%Y%m%d')
    return last_update.date() + datetime.timedelta(1)

"""CONSTANTS"""
BASE_URL = "https://covidtracking.com/api/v1/"
API_URL = {
    "statesDaily": "{}states/".format(BASE_URL),
    "usDaily": "{}us/".format(BASE_URL),
    "raceCombined": "{}race/".format(BASE_URL),
    "raceSeparate": "{}race/".format(BASE_URL),
}
STATES = ["ak", "al", "ar", "as", "az", "ca", "co", "ct", "dc", "de", "fl", "ga", "gu", "hi", 
          "ia", "id", "il", "in", "ks", "ky", "la", "ma", "md", "me", "mi", "mn", "mo", "mp",
          "ms", "mt", "nc", "nd", "ne", "nh", "nj", "nm", "nv", "ny", "oh", "ok", "or", "pa", 
          "pr", "ri", "sc", "sd", "tn", "tx", "ut", "va", "vi", "vt", "wa", "wi", "wv", "wy"]

BASE_FILE_LOCATION = "Data/CovidTrackingProject/"
FILE_LOCATION = {
    "statesDaily": "{}Daily/State/".format(BASE_FILE_LOCATION),
    "usDaily": "{}Daily/US/".format(BASE_FILE_LOCATION),
    "raceCombined": "{}Race/".format(BASE_FILE_LOCATION),
    "raceSeparate": "{}Race/".format(BASE_FILE_LOCATION)
}
RACE_FILES = {"combined": "states-combined", "separate": "states-separate"}
FILE_TYPE = "csv"

SUMMARY_FILE_PATH = "{}summary.{}".format(BASE_FILE_LOCATION, FILE_TYPE)

INITIAL_DATE = '20200306'
LATEST_UPDATE = datetime.date.strftime(getStartDate(),'%Y%m%d')
TODAY = datetime.date.today()

#Manual Start/End Dates (For Testing Purposes)
# START_DATE = datetime.date(2020, 8, 4)
