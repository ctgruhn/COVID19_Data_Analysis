from config import START_DATE, END_DATE
from request_data import *
from consolodate import *

if __name__ == "__main__":
    start = START_DATE
    if (start != END_DATE):
        getUSDaily(start)
        getStateDaily(start)
        getRaceData()

        consolodate(start)
    else:
        print("There are currently no updates available.")