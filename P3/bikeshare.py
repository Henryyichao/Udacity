import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december',"all"]
days = ['monday','tuesday','wensday','thursday','friday','saturday','sunday','all']


def input_check(v_list, input_message, error_message):
    v = input(input_message).lower()
    while v not in v_list:
        print(error_message)
        v = v.replace(v,input("try again.\n").lower())
    else:
        return v


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid input

    city = input_check(CITY_DATA.keys(),"Would you like to see data for Chicago,New York,or Washington?\n","please choose from the Chicago,New York and Washington.")
	
    # TO DO: get user input for month (all, january, february, ... , june)

    month = input_check(months,"which month would like to explore?input the month name.You can also input'all' to reach all data.\n","Sorry,please choose one month from January,February...December.Or type 'all'to reach all data.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input_check(days,"which day would like to explore?Monday,Tuesday..or you input'all' to reach all data. \n","Sorry,please choose day from Monday,Tuesday...Sunday.Or type 'all'to reach all data.")


    print('-'*40)
    return city, month, day

def load_data(city, month, day):
        # load data file into a dataframe

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] =  pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour']= df["Start Time"].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
        if day != 'all':
        # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = df['month'].mode()
    print("the most common month is :",common_month[0])

    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()
    print("the most common day is :",common_day[0])

    # TO DO: display the most common start hour

    common_hour = df['hour'].mode()
    print("the most common hour is :",common_hour[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    # TO DO: display most commonly used start station

    start_staition = df["Start Station"].mode()[0]
    s_counts = df["Start Station"].value_counts()
    print("the most common start staition is :",start_staition,"counts:",s_counts.max())
    # TO DO: display most commonly used end station
    end_staition = df["End Station"].mode()[0]
    e_counts = df["End Station"].value_counts()
    print("the most common end staition is :",end_staition,"counts:",e_counts.max())

    # TO DO: display most frequent combination of start station and end station trip
    top = df.groupby(['Start Station', 'End Station']).size().idxmax()
    #Series 中还有一对 ser.idxmax() 和 ser.idxmin() 方法，可以返回数组中最大（小）值的索引值，或者 .argmin()和 .argmax() 返回索引位置。当然这两类方法也是可以通过上面这种 ser[ser=ser.max()] 来替代实现的。
    print("The most frequent combination of start station and end station trip is {} to {}".format(top[0], top[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_tt = df['Trip Duration'].sum()
    print("the total trip duration is :",total_tt)

    # TO DO: display mean travel time
    mean_tt = df['Trip Duration'].mean()
    print("the average trip duration is :",mean_tt)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_up = df['User Type'].value_counts()
    #The dtype is a Series,use iloc or loc to extract data
    counts_subscriber = counts_up.loc[('Subscriber')]
    counts_customer = counts_up.loc[('Customer')]

    print("the number of subscribers is :",counts_subscriber)
    print("the number of customers is :",counts_customer)

    # TO DO: Display counts of gender
    counts_gender = df['Gender'].value_counts()
    counts_Male = counts_gender.loc[('Male')]
    counts_Female = counts_gender.loc[('Female')]

    print("the number of male users is :",counts_Male)
    print("the number of female users is :",counts_Female)

    # TO DO: Display earliest, most recent, and most common year of birth
    min_birthyear = int(df['Birth Year'].min())
    max_birthyear = int(df['Birth Year'].max())
    mode_birthyear = int(df['Birth Year'].mode())

    print("the oldest user's birth year is:",min_birthyear)
    print("the youngest user's birth year is:",max_birthyear)
    print("the most common user's birth year is :",mode_birthyear)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        print(month)
        df = load_data(city, month, day)
        print(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        try:
            user_stats(df)
        except KeyError:
            print("Sorry,the Gender data of this city is missed.")
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
