from COVID19_Chart import app
from flask import Flask, jsonify, request, render_template, flash
# from COVID19_Chart.request_data import initData
# from COVID19_Chart.analytics import update_chart#, initData
from COVID19_Chart.analytics import update_chart
from COVID19_Chart.tables import table
from COVID19_Chart.config import LATEST_UPDATE

@app.route('/')
def index():
    return render_template("index.html",
        title = 'Home',
        start_date = "2020-03-16",
        min_date = "2020-03-16",
        max_date=max_date,
        end_date = max_date)

# import datetime


# all_data = initData() # Would be imporved by using database instead of files
min_date = "2020-03-16"
max_date = "2020-08-16"
max_date = (LATEST_UPDATE  - datetime.timedelta(1)).strftime("%Y-%m-%d")

@app.route('/schema')
def schema():
    return render_template("schema.html", title = 'About Data',table=table)

@app.route('/updateData', methods =["GET", "POST"]) 
def updateData(): 
    start_date = min_date
    if request.method == 'POST':
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
