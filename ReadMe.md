# COVID Data Visualization

This project aims to consolidate and display current data on COVID 19 in the United States. It achieves this by analyzing data from the COVID Tracking Project using Python and displaying that data with Flask and D3.JS.

## Setup

Install virtualenv:

```bash

pip install virtualenv

```

Create new environment:

```bash
virtualenv venv
```

Activate environment:

```bash
source venv/bin/activate
```

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Flaws

Ultimately, any data visualization is only as good as the data it analyzes. While the [COVID Tracking Project] (https://covidtracking.com) is a great resource, it relies on the state governments that are meant to collect this data, which can be lacking. This is unfortunately why some data points rapidly fall to 0.

## Next Steps

The main goal that should be addressed moving forward is accounting for the above flaws in the data. There are two ways I propose to address this: 1. Supplementing the COVID Tracking Project data with one or more similar datasets, and/or 2. Estimate the missing data based on what is currently available. The second option is only possible in certain situations. For example, if a state provides the current number of hospitalized individuals, but not cumulative number, the cumulative can be estimated by summing the increase in day to day hospitalizations. This would be an underestimation, however, so additional effort would be needed to increase accuracy. 

Beyond improvements to the data, there are a few improvements to the application itself that should be considered. The primary goal of this application is to provide flexibility to the user in the data they are analyzing. Therefore, functions will need to be developed to handle the users needs. Utilizing Pandas, actions such as searching ranges or summing data is quite simple, as they have builtin functions. Anything beyond this would need to be developed by the author.

Finally, some work can be done to make the chart easier to use and analyze. A table with the states and their data would be extremely helpful in understanding what is being shown. Additionally, the ability to reset the graph after excluding data will need to be incorporated.

## Acknowledgments

To learn more about D3.js and parallel coordinates graphs click [here](https://observablehq.com/@d3/parallel-coordinates).
This project also utilizes the above example as well as Kai Chang's [example](http://bl.ocks.org/syntagmatic/3150059).