# COVID Data Visualization

This project aims to consolidate and display current data on COVID 19 in the United States.

## Requirements
This project utilized frontend and backend development, which required two sets of packages.

### Backend
The data was collected using Python Requests and then processed with Pandas:
```bash
pip install requests
pip3 install pandas
```

### Frontend
The front end and backend are connected through Flask.
```bash
pip install flask
```

Start the server, type the following into the python terminal:
```python
python run.py
```

The chart is displayed using D3.js.

## Acknowledgments
To learn more about D3.js and parallel coordinates graphs click [here](https://observablehq.com/@d3/parallel-coordinates).
This project also utilizes the above example as well as Kai Chang's [example](http://bl.ocks.org/syntagmatic/3150059).