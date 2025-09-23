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

## Problem 3: Script
Create a Python script called faang.py in the root of your repository. Copy the above functions into it and it so that whenever someone at the terminal types ./faang.py, the script runs, downloading the data and creating the plot. Note that this will require a shebang line and the script to be marked executable. Explain the steps you took in your notebook.

### Problem 4: Automation
Create a GitHub Actions workflow to run your script every Saturday morning. The script should be called faang.yml in a .github/workflows/ folder in the root of your repository. In your notebook, explain each of the individual lines in your workflow.
