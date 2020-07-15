import datetime

# CONSTANTS
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

BASE_FILE_LOCATION = "CovidTrackingProject/"
FILE_LOCATION = {
    "statesDaily": "{}Daily/State/".format(BASE_FILE_LOCATION),
    "usDaily": "{}Daily/US/".format(BASE_FILE_LOCATION),
    "raceCombined": "{}Race/".format(BASE_FILE_LOCATION),
    "raceSeparate": "{}Race/".format(BASE_FILE_LOCATION)
}
RACE_FILES = {"combined": "states-combined", "separate": "states-separate"}
FILE_TYPE = "csv"

START_DATE = datetime.date(2020, 1, 22)
END_DATE = datetime.date.today()