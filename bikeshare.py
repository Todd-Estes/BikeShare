import time
import pandas as pd
from collections import Counter

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city = input("Enter a city (Chicago, New York City, or Washington): ").lower()
        if city in CITY_DATA.keys():
            break
        print("Invalid input. Please try again.")

    while True:
        month = input("Enter a month (all, january, february, ..., june): ").lower()
        if month in MONTHS or month == 'all':
            break
        print("Invalid month input. Please try again.")

    while True:
        day = input("Enter a day of the week (all, monday, tuesday, ..., sunday): ").lower()
        if day in DAYS or day == 'all':
            break
        print("Invalid day input. Please try again.")



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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday
    df['Start Hour'] = df['Start Time'].dt.hour

    # Filter by month if specified
    if month != 'all':
        df = df[df['Start Time'].dt.month_name() == month.title()]

    # Filter by day if specified
    if day != 'all':
        df = df[df['Day of Week'] == DAYS.index(day)]
    
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


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df.groupby(['Start Station']).size().sort_values(ascending=False)
    print('Most commonly used start station: ', most_common_start_station.index[0])

    # display most commonly used end station
    most_common_end_station = df.groupby(['Start Station']).size().sort_values(ascending=False)
    print('Most commonly used end station: ', most_common_end_station.index[0])

    # display most frequent combination of start station and end station trip
    common_routes = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False)
    print(common_routes)
    print('Most common route:')
    print('From:', common_routes.index[0][0])  # Most common start station
    print('To:', common_routes.index[0][1])    # Most common end station  

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
    df['User Type'] = df['User Type'].fillna('unknown user')
    user_types = df['User Type'].unique()
    for ut in user_types:
        print(f'Total {ut} type users: ', df['User Type'].value_counts()[ut])

    # Display counts of gender
    if 'Gender' in df.columns:
      df['Gender'] = df['Gender'].fillna('undisclosed gender')
      genders = df['Gender'].unique()
      for g in genders:
          print(f'Total {g} users: ', df['Gender'].value_counts()[g])

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
      print('Earliest user DOB: ', df['Birth Year'].min())
      print('Most recent user DOB: ', df['Birth Year'].max())
      print('Most common user DOB: ', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def prompt_raw_data(df):
    """Asks if user wants to see raw data in 5-line increments"""

    print('You have the option to inspect individual lines of raw data from the data set you requested...')
    start_loc = 0
    while True:
        user_input = input("Would you like to see 5 more lines of data (yes or no): ").lower()
        if user_input in ['yes', 'y']:
            print(df[start_loc:start_loc+5])
            start_loc += 5
            if start_loc >= len(df):
                print("No more data to show!")
                break
        elif user_input in ['no', 'n']:
            break
        else:
            print("Invalid input. Please enter yes to see more data, or no to exit.")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        prompt_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
