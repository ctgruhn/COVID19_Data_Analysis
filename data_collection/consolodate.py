import csv, os.path, datetime
from data_collection.config import SUMMARY_FILE_PATH, FILE_TYPE, FILE_LOCATION, STATES, START_DATE, END_DATE

def dateRange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

def setSummary(file_type, file_location, target_file=SUMMARY_FILE_PATH, start_date = START_DATE, end_date = END_DATE):
    for single_date in dateRange(start_date, end_date):
        fullFilePath = "{}{}.{}".format(file_location, single_date.strftime("%Y%m%d"), file_type)
        if os.path.isfile(fullFilePath):    # Skips redownloading files
            myfile = csv.reader(open(fullFilePath))
            with open(target_file,'a') as f:
                w = csv.writer(f)
                next(myfile)
                for row in myfile:
                    w.writerow(row)
            print("{} SUCCESSFULLY ADDED TO SUMMARY".format(fullFilePath))
        else:
            print("{} DOES NOT EXIST".format(fullFilePath))
def consolodate(start_date=START_DATE, end_date=END_DATE):
    for state in STATES:
        file_path = "{}{}/".format(FILE_LOCATION["statesDaily"], state)
        setSummary(FILE_TYPE,file_path)
