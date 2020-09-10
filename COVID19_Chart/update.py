from COVID19_Chart.config import START_DATE, END_DATE
from COVID19_Chart.request_data import getUSDaily, getStateDaily, getRaceData
from COVID19_Chart.consolodate import consolodate

if __name__ == "__main__":
    start = START_DATE
    if (start < END_DATE):
        getUSDaily(start)
        getStateDaily(start)
        getRaceData()

        consolodate(start)
    else:
        print("There are currently no updates available.")