from COVID19_Chart import app
from flask import Flask, jsonify, request, render_template, flash
# from COVID19_Chart.request_data import initData
# from COVID19_Chart.analytics import update_chart#, initData
from COVID19_Chart.analytics import update_chart
from COVID19_Chart.config import START_DATE

@app.route('/')
def index():
    return render_template("index.html",
        title = 'Home',
        # categories=categories,
        start_date = "2020-03-16",
        min_date = "2020-03-16",
        max_date=max_date,
        end_date = max_date)

# import datetime


# all_data = initData()
min_date = "2020-03-16"
max_date = "2020-08-16"
# max_date = (START_DATE  - datetime.timedelta(1)).strftime("%Y-%m-%d")

# categories = {
#     'positive':'positive',
#     'negative':'negative',
#     'hospitalizedCurrently':'Currently Hospitalized',
#     'inIcuCurrently':'inIcuCurrently'
# }

@app.route('/updateData', methods =["GET", "POST"]) 
def updateData(): 
    start_date = min_date
    if request.method == 'POST':
        # columns = request.form.getlist('cat')
        raw_start_date = request.form.get('startDate')
        start_date = raw_start_date.replace("-","")
        raw_end_date = request.form.get('endDate')
        end_date = raw_start_date.replace("-","")
        flash(str(max_date))
        update_chart(all_data, start_date, end_date)
    return render_template("index.html",
        title = 'Home',
        categories=categories,
        start_date = raw_start_date,
        end_date = raw_end_date,
        min_date = min_date,
        max_date = max_date)


def updateStart(): 
    start_date = min_date
    if request.method == 'POST':
        columns = request.form.getlist('cat')
        raw_start_date = request.form.get('startDate')
        start_date = raw_start_date.replace("-","")
        raw_end_date = request.form.get('endDate')
        end_date = raw_start_date.replace("-","")
        flash(str(max_date))
        update_chart(all_data, start_date, end_date)
    return render_template("index.html",
        title = 'Home',
        categories=categories,
        start_date = raw_start_date,
        end_date = raw_end_date,
        min_date = min_date,
        max_date = max_date)
    # return render_template("home.html")
# def calculate_percentage(val, total):
#     """Calculates the percentage of a value over a total"""
#     percent = np.divide(val, total)
    
#     return percent
# @app.route('/get_piechart_data')
# def get_piechart_data():

#     pieChartData = []

#     return jsonify(pieChartData)

# @app.route('/get_barchart_data')
# def get_barchart_data():

#     barChartData = []

    
#     return jsonify(barChartData)