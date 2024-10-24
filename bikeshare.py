import time
import pandas as pd
import numpy as np
from collections import Counter

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June']
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')


    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input("Enter a city (chicago, new york city, washington): ").lower()
        if city in cities:
            break
        print("Invalid input. Please try again.")

    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input("Enter a month (all, january, february, ..., june): ").lower()
        if month in months:
            break
        print("Invalid input. Please try again.")


    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input("Enter a day of the week (all, monday, tuesday, ..., sunday): ").lower()
        if day in days:
            break
        print("Invalid input. Please try again.")



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # TODO IMPLEMENT FILTERS
    formatted_city = city.replace(' ', '_')
    df = pd.read_csv(f'{formatted_city}.csv')

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday
    df['Start Hour'] = df['Start Time'].dt.hour
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    mcm = (df['Month'].mode()[0]) - 1
    print('Most common month of travel: ', MONTHS[mcm])

    # display the most common day of week
    mcd = (df['Day of Week'].mode()[0])
    print('Most common day of travel: ', DAYS[mcd])

    # display the most common start hour
    mch = (df['Start Hour'].mode()[0])
    print('Most common start hour: ', mch)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def most_common_station(df, station_type):
    stations = df[station_type].values
    counter = Counter(stations)
    sorted_stations = sorted(stations, key=lambda x: counter[x], reverse=True)

    return sorted_stations[0]

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most commonly used start station: ', most_common_station(df, 'Start Station'))

    # display most commonly used end station
    print('Most commonly used end station: ', most_common_station(df, 'End Station'))

    # display most frequent combination of start station and end station trip
    # TODO FINISH THIS^, and refactor first two data statements

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Approimate total travel time of all passengers, in minutes: ', round(df['Trip Duration'].sum() / 60))

    # display mean travel time
    print('Approximate average travel time for all passengers, in minutes: ', round(df['Trip Duration'].mean() / 60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].unique()
    for ut in user_types:
        print(f'Total {ut} type users: ', df['User Type'].value_counts()[ut])


    # Display counts of gender
    df['Gender'] = df['Gender'].fillna('undisclosed gender')
    genders = df['Gender'].unique()
    for g in genders:
        print(f'Total {g} users: ', df['Gender'].value_counts()[g])

    # Display earliest, most recent, and most common year of birth
    print('Earliest user DOB: ', df['Birth Year'].min())
    print('Most recent user DOB: ', df['Birth Year'].max())
    print('Most common user DOB: ', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.info())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
