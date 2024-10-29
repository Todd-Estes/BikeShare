## BikeShare  🚲

This Python/Pandas application analyzes bike share data from three major US cities (Chicago, New York City, and Washington), allowing users to filter by month and day of the week to explore patterns in travel times, popular stations, trip durations, and rider demographics. The interactive program presents various statistics about bike usage and allows users to view the raw data in manageable chunks, making it easy to understand how bike sharing services are being utilized in these cities.


## Table of Contents
- [Prerequisites](#prerequisites)
- [Get Setup and Running](#get-setup-and-running)
- [Using the App](#using-the-app)


## Prerequisites
1. Have Python 3.x installed on your computer
2. Have Pandas library installed (you can install it using: pip install pandas)

## Get Setup and Running

1. Clone the repository:

    $`git clone git@github.com:Todd-Estes/EmployeePolls.git`

2. Start the app:

   1. Open your terminal/command prompt
   2. Navigate to the directory containing the script and data files
   3. Run the program by typing: python bikeshare.py
   
## Using the App

1. When prompted, enter one of these cities:
   - Chicago
   - New York City
   - Washington

2. Next, choose how to filter by month:
   - Type 'all' to analyze all months
   - Or enter a specific month (january through june)

3. Then choose how to filter by day:
   - Type 'all' to analyze all days
   - Or enter a specific day of the week (monday through sunday)

4. The program will display statistics about:
   - Most common times of travel
   - Popular stations and routes
   - Trip durations
   - User information

5. You'll have the option to view raw data in chunks of 5 rows
   - Enter 'yes' to see data
   - Enter 'no' to skip

6. After viewing all statistics, you can:
   - Enter 'yes' to restart and analyze different data
   - Enter 'no' to exit the program
