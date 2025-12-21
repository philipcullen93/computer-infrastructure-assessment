# Computer Infrastructure Assessment
Assessment for Computer Infrastructure Module

## Initial Thoughts
Key to this project will be making sure my code and the method I use to solve problems line up with the 4 learning outcomes.
The learning outcomes are:
1. Use, configure, and script in a command line interface environment.
2. Manipulate and move data and code using the command line.
3. Compare commonly available software infrastructures and architectures.
4. Select appropriate infrastructure for a given computational task.

## Overview
This repository contains the solution to a multi-part Python assignment focused on downloading, visualising, and automating financial market data for major technology stocks using yfinance, pandas, and GitHub Actions. 

The purpose of the project is not only to produce correct outputs, but to demonstrate:

1. Clear problem decomposition and solution design

2. Research-driven use of third-party libraries

3. Reproducible and automated data workflows

4. Professional repository organisation and documentation

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

└── README.md # Project documentation

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

### Tools and Technologies
The following tools and technologies were used for this project:
- Python 3 was the core programming language
- yfinance was used to access historical financial data directly from Yahoo Finance using its public API [1] [2] [3].
- pandas were used to manipulate and export the downloaded data into a .csv (comma-separated values) file [4].
- datetime creates a timestamp for the file. This allows the file to be created with the required YYYYMMDD-HHmmss.csv format [5]. 
- os check the repository to see if the data/ folder exists and create it if necessary [5].
- matplotlib was used for financial data visualisation [6].
- GitHub Actions was used for workflow automation and scheduling [7].
- Jupyter Notebook was used for narrative explanation, analysis, and reflection [8].

These tools were selected based on their widespread use in industry and strong documentation support, making the project both practical and academically grounded.

### Assumptions and Design Decisions
- Hourly data was selected to balance data granularity with file size and API reliability.
- The most recent CSV file is determined using file timestamps rather than filenames alone to ensure robustness.
- All directories (data/, plots/) are created dynamically to allow the repository to run cleanly in new environments, including GitHub Actions.
- The script is designed to be idempotent, meaning it can be run multiple times without overwriting previous outputs.

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

### Error Handling and Limitations
- If Yahoo Finance is temporarily unavailable, the script may fail during data download.
- No retry or backoff mechanism is currently implemented.
- Market holidays may result in fewer data points than expected for a given five-day window.
- The workflow assumes GitHub-hosted runners with Python preinstalled.

# References
The following references were used in the README.md file.

1. yFinance Background Information:  
   https://www.geeksforgeeks.org/machine-learning/what-is-yfinance-library/

2. Yahoo Finance (Data Source):  
   https://finance.yahoo.com/

3. yfinance Documentation:  
   https://pypi.org/project/yfinance/

4. pandas Official Documentation:  
   https://pandas.pydata.org/docs/

5. Python Standard Library Documentation (datetime, os):  
   https://docs.python.org/3/library/

6. matplotlib Documentation:  
   https://matplotlib.org/stable/users/index.html

7. GitHub Actions Documentation:  
   https://docs.github.com/en/actions

8. Jupyter Notebook Documentation:  
   https://docs.jupyter.org/en/latest/

# References (Code)
The following references were used in writing the programs:

1. yfinance Documentation: https://pypi.org/project/yfinance/

2. pandas Official Documents: https://pandas.pydata.org/docs/

3. Python Standard Library (datetime & os): https://docs.python.org/3/library/

4. Yahoo Finance (data source): https://finance.yahoo.com/

5. GNU Core Utilities – File Permissions and chmod: https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html

6. Python Documentation – __main__ and Program Structure: https://docs.python.org/3/library/__main__.html

7. Python Documentation – Shebang Lines and Executable Scripts: https://docs.python.org/3/using/unix.html#executable-python-scripts

8. Python Documentation – datetime Module: https://docs.python.org/3/library/datetime.html

9. GitHub Actions Documentation: https://docs.github.com/en/actions

10. GitHub Actions – Events That Trigger Workflows: https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows

11. GitHub Actions – GitHub-hosted Runners: https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners

12. actions/checkout Documentation: https://github.com/actions/checkout

13. actions/setup-python Documentation: https://github.com/actions/setup-python

14. Python Packaging User Guide – pip: https://packaging.python.org/en/latest/tutorials/installing-packages/

15. actions/upload-artifact Documentation: https://github.com/actions/upload-artifact1. yfinance Documentation: https://pypi.org/project/yfinance/







