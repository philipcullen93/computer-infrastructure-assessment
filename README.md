# Computer Infrastructure Assessment
Assessment for Computer Infrastructure Module

## Initial Thoughts
Key to this project will be making sure my code and the method I use to solve problems line up with the 4 learning outcomes.
The learning outcomes are:
1. Use, configure, and script in a command line interface environment.
2. Manipulate and move data and code using the command line.
3. Compare commonly available software infrastructures and architectures.
4. Select appropriate infrastructure for a given computational task.

## Problems
Below is a list of the 4 problems to complete with their descriptions.
### Problem 1: Data from yfinance
Using the yfinance Python package, write a function called get_data() that downloads all hourly data for the previous five days for the five FAANG stocks:

Facebook (META)
Apple (AAPL)
Amazon (AMZN)
Netflix (NFLX)
Google (GOOG)
The function should save the data into a folder called data in the root of your repository using a filename with the format YYYYMMDD-HHmmss.csv where YYYYMMDD is the four-digit year (e.g. 2025), followed by the two-digit month (e.g. 09 for September), followed by the two digit day, and HHmmss is hour, minutes, seconds. Create the data folder if you don't already have one.

### Problem 2: Plotting Data
Write a function called plot_data() that opens the latest data file in the data folder and, on one plot, plots the Close prices for each of the five stocks. The plot should include axis labels, a legend, and the date as a title. The function should save the plot into a plots folder in the root of your repository using a filename in the format YYYYMMDD-HHmmss.png. Create the plots folder if you don't already have one.

### Problem 3: Script
Create a Python script called faang.py in the root of your repository. Copy the above functions into it and it so that whenever someone at the terminal types ./faang.py, the script runs, downloading the data and creating the plot. Note that this will require a shebang line and the script to be marked executable. Explain the steps you took in your notebook.

### Problem 4: Automation
Create a GitHub Actions workflow to run your script every Saturday morning. The script should be called faang.yml in a .github/workflows/ folder in the root of your repository. In your notebook, explain each of the individual lines in your workflow.

## Overview
This repository contains the solution to a multi-part Python assignment focused on downloading, visualising, and automating financial market data for major technology stocks using yfinance, pandas, and GitHub Actions.

The project downloads recent hourly stock price data for the five FAANG companies, plots their closing prices, and automates the entire process to run weekly.

FAANG Stocks Used:

- Meta (META)

- Apple (AAPL)

- Amazon (AMZN)

- Netflix (NFLX)

- Google (GOOG)

All code, explanations, and outputs are contained within this repository.

### Repository Structure
.
├── data/ # CSV files containing downloaded stock data
├── plots/ # Generated price comparison plots
├── .github/
│ └── workflows/
│ └── faang.yml # GitHub Actions workflow for automation
├── faang.py # Executable script to download and plot data
├── problems.ipynb # Jupyter Notebook with solutions and explanations
└── README.md # Project documentation (this file)

## How to Run Locally

1. Clone the repository

2. Install dependencies:

  pip install yfinance pandas matplotlib

3. Make the script executable:

  chmod +x faang.py

4. Run the script:

  ./faang.py

#### yfinance
YFinance is a Python Library which allows access to financial data from Yahoo Finance. It can be used to download stock and company financial statements. Features of yfiancne include: Historical Market Financial Data, Corporate Actions, Financial Statements, Meta Data, and Multiple Tickers. [1, https://www.geeksforgeeks.org/machine-learning/what-is-yfinance-library]

It can be installed using _pip install yfinance_.

### Python Packages
The Python Packages required: 
- yfinance is used to access historical financial data directly from Yahoo Finance using its public API [2][3].
- pandas  are used to manipulate and export the downloaded data into a .csv (comma-separated values) file [4].
- datetime creates a timestamp for the file. This allows the file to be created with the required YYYYMMDD-HHmmss.csv format [5]. 
- os check the repository to see if the data/ folder exists and create it if necessary [5].

## Solving Problems
All solutions, code etc. can be found in the Jupyter Notebook [problems.ipynb](https://github.com/philipcullen93/computer-infrastructure-assessment/blob/main/problems.ipynb)

### Problem 1:
A function called get_data() was created to:

- Download hourly stock data for the previous five days

- Retrieve data for META, AAPL, AMZN, NFLX, and GOOG

- Create a data/ directory if it does not already exist

- Save the data as a CSV file using the format:

YYYYMMDD-HHmmss.csv

The timestamp ensures each dataset is uniquely identifiable.

### Problem 2: Plotting the Data

A function called plot_data() was implemented to:

- Load the most recent CSV file from the data/ directory

- Plot the Close prices for all five stocks on a single chart

  - Including:

    - X-axis and Y-axis labels

    - A legend

    - The date as the plot title

Save the plot to a plots/ directory using the format:

YYYYMMDD-HHmmss.png

The folder is automatically created if it does not exist.

### Problem 3: Executable Script

A Python script named faang.py was created in the root of the repository.

Features of the script:

- Contains both get_data() and plot_data() functions

- Includes a shebang line so it can be run directly from the terminal

Marked as executable using:

- chmod +x faang.py

The script is run by using ./faang.py in the terminal.

This command downloads the data and generates the plot in one step.

All setup steps and explanations are documented in problems.ipynb.

### Problem 4: Automation with GitHub Actions

A GitHub Actions workflow named faang.yml was created inside: .github/workflows/

The workflow:

- Runs automatically every Saturday morning

- Checks out the repository

- Installs required Python dependencies

- Executes faang.py

Each line of the workflow file is explained in detail in the Jupyter Notebook.

# References
1 - yFinance Background Information: (https://www.geeksforgeeks.org/machine-learning/what-is-yfinance-library)

2 - Yahoo Finance (data source): (https://finance.yahoo.com/)

3 - yfinance Documentation: (https://pypi.org/project/yfinance/)

4 - pandas Official Docs: (https://pandas.pydata.org/docs/)  

5 - Python Standard Library (datetime & os): (https://docs.python.org/3/library/)
