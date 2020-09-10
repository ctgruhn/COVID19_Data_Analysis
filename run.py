from COVID19_Chart import app

if __name__ == '__main__':
      app.run(debug=True)

# from flask import Flask, jsonify, request, render_template, flash
# import csv
# import pandas as pd
# import numpy as np
# import datetime
# from data_collection.analytics import update_chart, initData
# from data_collection.config import START_DATE

# app = Flask(__name__)
# app.secret_key = "abc" 
# # all_data = initData()
# min_date = "2020-03-16"
# max_date = (START_DATE  - datetime.timedelta(1)).strftime("%Y-%m-%d")


# categories = {
#     'positive':'positive',
#     'negative':'negative',
#     'hospitalizedCurrently':'Currently Hospitalized',
#     'inIcuCurrently':'inIcuCurrently'
# }

# @app.route('/')
# def index():
#     return render_template("index.html",
#         title = 'Home',
#         categories=categories,
#         start_date = "2020-03-16",
#         min_date = "2020-03-16",
#         max_date=max_date,
#         end_date = max_date)

# @app.route('/updated', methods =["GET", "POST"]) 
# def updateData(): 
#     start_date = min_date
#     if request.method == 'POST':
#         raw_start_date = request.form.get('startDate')
#         start_date = raw_start_date.replace("-","")
#         raw_end_date = request.form.get('endDate')
#         end_date = raw_start_date.replace("-","")
#         flash(str(max_date))
#         update_chart(all_data, start_date, end_date)
#     return render_template("index.html",
#         title = 'Home',
#         categories=categories,
#         start_date = raw_start_date,
#         end_date = raw_end_date,
#         min_date = min_date,
#         max_date = max_date)
 
if __name__ == '__main__':
      app.run(debug=True)