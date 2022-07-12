from dataclasses import dataclass, field
from bs4 import BeautifulSoup
import requests
from datetime import date, datetime, timedelta
import json
import os.path
from isoweek import Week


@dataclass
class Holiday:
    name: str
    date: str

def getholidays():

    file_exists = os.path.exists('allholidays.json')

    if file_exists == False:

        holidayslist2020 = []
        holidayslist2021 = []
        holidayslist2022 = []
        holidayslist2023 = []
        holidayslist2024 = []

        for i in range(2020,2025):

            #format url to take the year (i) in {}

            url = 'https://www.timeanddate.com/holidays/us/{}?hol=33554809'
            url = url.format(i)
            response = requests.get(url)

            rawhtml = response.text

            soup = BeautifulSoup(rawhtml, 'html.parser')

            holidays_raw = soup.find_all('tr', attrs = {'class' : 'showrow'})
            for holiday in holidays_raw:

                # Getting the date for the holiday of said year (i)
                date_raw = holiday.find('th')
                holidaydate = date_raw.text + " " + str(i)

                # Attempted to convert it into a number but didn't work. Didn't print out hyphens, consult with professor
                # date_object = datetime.strptime(holidaydate, "%b %d %Y")
                # date = date_object.date()
            
                #Getting the name of the holiday of said year (i)
                name = holiday.find('a')
                holidayname = name.text

                #run the holiday through Holiday class
                holiday = Holiday(holidayname,holidaydate)

                #run the for loop for every year and add it to it's holiday list
                if i == 2020:
                    holidayslist2020.append(holiday)
                elif i == 2021:
                    holidayslist2021.append(holiday)
                elif i == 2022:
                    holidayslist2022.append(holiday)
                elif i == 2023:
                    holidayslist2023.append(holiday)
                elif i == 2024:
                    holidayslist2024.append(holiday)

        #turn list into a dictionary form to turn into json later
        modifiedholidayslist2020 = [Holiday.__dict__ for Holiday in holidayslist2020 ]
        modifiedholidayslist2021 = [Holiday.__dict__ for Holiday in holidayslist2021 ]
        modifiedholidayslist2022 = [Holiday.__dict__ for Holiday in holidayslist2022 ]
        modifiedholidayslist2023 = [Holiday.__dict__ for Holiday in holidayslist2023 ]
        modifiedholidayslist2024 = [Holiday.__dict__ for Holiday in holidayslist2024 ]

        #add every list into a final dictionary where the keys are the years
        FinalDictionary = {}
        FinalDictionary['2020'] = modifiedholidayslist2020
        FinalDictionary['2021'] = modifiedholidayslist2021
        FinalDictionary['2022'] = modifiedholidayslist2022
        FinalDictionary['2023'] = modifiedholidayslist2023
        FinalDictionary['2024'] = modifiedholidayslist2024

        #Create json file with all the holidays
        with open("allholidays.json", "w") as file:
            json.dump(FinalDictionary, file)

        start_up()

    else:
        start_up()

def start_up():

    f = open('allholidays.json')
    data = json.load(f)
    length2020 = len(data['2020'])
    length2021 = len(data['2021'])
    length2022 = len(data['2022'])
    length2023 = len(data['2023'])
    length2024 = len(data['2024'])
    f.close()
    TotalLength = length2020 + length2021 + length2022 + length2023 + length2024

    print("Holiday Management")
    print("==================")
    print("There are " + str(TotalLength) + " holidays stored in the system")

    main_menu()

def main_menu():

    print("Holiday Menu")
    print("============")
    print("1. Add a Holiday")
    print("2. Remove a Holiday")
    print("3. Save Holiday List")
    print("4. View Holidays")
    print("5. Exit")
    userinput = input("What would you like to do? Please input a number 1-5 ")

    if userinput == '1':
        addaholiday()
    elif userinput == '2':
        removeaholiday()
    elif userinput == '3':
        print("Save changes after adding or removing a holiday")
        main_menu()
    elif userinput == '4':
        viewholidays()
    elif userinput == '5':
        print("Exiting program")
        exit()  
    else:
        print("Choose a number 1 - 5: ")
        main_menu()

def addaholiday():

    global holidaynameinput

    holidaylist = []

    print("Add a Holiday")
    print("=============")

    holidaynameinput = input("Holiday : ")

    def holidaydate():

        global holidaydateinputmodified
        global holidaydateinputyear

        years = ['2020','2021','2022','2023','2024']

        holidaydateinput = input("Date in format 'MMM/D/YYYY for " + holidaynameinput + " : ")
        holidaydateinput = holidaydateinput.capitalize()

        #Format the date needs to be in
        format = "%b/%d/%Y"

        #Confirm format is correct

        res = True
        
        try:
            res = bool(datetime.strptime(holidaydateinput, format))
        except ValueError:
            res = False
            print("Date inputted doesn't match format, try again")
            holidaydate()

        #Grab the year to confirm the year is in range

        holidaydateinputyear = holidaydateinput.split('/')
        holidaydateinputyear = holidaydateinputyear[2]
        if holidaydateinputyear not in years:
            print("Enter year between 2020 - 2024")
            holidaydate()
        else:
            #Format date to be in MMM D YYYY format (Jan 20 2021)
            holidaydateinputmodified = holidaydateinput.replace('/',' ')

    holidaydate()

    # pass the name and date of the holiday through holiday dataclass

    holiday = Holiday(holidaynameinput,holidaydateinputmodified)

    #add it to a list of holidays
    holidaylist.append(holiday)

    #modify to be able to turn into json
    modifiedholidaylist = [Holiday.__dict__ for Holiday in holidaylist]
    
    #open json file
    f = open('allholidays.json')
    data = json.load(f)
    year = data[holidaydateinputyear]

    #add all the holidays into the modified holiday list
    for i in year:
        modifiedholidaylist.append(i)
    
    #have the year key-value be the new list with the updated holiday
    data[holidaydateinputyear] = modifiedholidaylist

    #Have changes saved when holiday is added 
    def savechangesinaddaholiday(x):

        save = input("Save your changes in order to continue? Y/N ")
        save = save.upper()
        print(save)

        if save == 'Y':
            print("Success:")
            print(holidaynameinput + " (" + holidaydateinputmodified + ") has been added to the holiday list." )
            savechanges(data)
        elif save == 'N':
            print("Ok, going back to the main menu")
            main_menu()
        else:
            print("Enter Y/N")
            savechangesinaddaholiday(x)

    savechangesinaddaholiday(data)

def savechanges(x):

    with open("allholidays.json", "w") as file:
        json.dump(x, file)

    main_menu()

def removeaholiday():

    f = open('allholidays.json')
    data = json.load(f)

    years = ['2020','2021','2022','2023','2024']

    print("Remove a Holiday")
    print("=============")

    holiday = input("Holiday Name: ")
    year = input("For which year? ")

    while year not in years:
        year = input("Enter a year from 2020 - 2024: " )

    #Get the list of values for that year and put them into a list
    listofvalues = [value for elem in data[year] for value in elem.values()]

    #Confirm holiday is in list
    if holiday in listofvalues:
        print("Found " + holiday)
        print("removing from holiday list")
    else:
        print("Holiday wasn't in list")
        main_menu()

    #Grab the index of that holiday in the list
    holidayindex = next((index for (index, d) in enumerate(data[year]) if d["name"] == holiday))

    #Delete the holiday from that list
    deleteholiday = data[year].pop(holidayindex)

    print("Success! " + holiday + " has been removed from the holiday list." )

    #Save changes
    def savechangesinremoveaholiday(x):

        save = input("Save your changes in order to continue? Y/N ")
        save = save.upper()
        print(save)

        if save == 'Y':
            print("Success:")
            savechanges(data)
        elif save == 'N':
            print("Ok, going back to the main menu")
            main_menu()
        else:
            print("Enter Y/N")
            savechangesinremoveaholiday(x)

    savechangesinremoveaholiday(data)

def viewholidays():

    #create list for years supported in file
    yearlist = ['2020','2021','2022','2023','2024']
    print("View Holidays")
    print("=============")

    year = input("Which year? ")

    while year not in yearlist:

        year = input("Enter a year from 2020-2024: ")

    week = input("Which week? #[1-52, Leave blank for the current week]: ")

    if len(week) == 0:
        week = date.today()
        week = week.isocalendar()[1]
    elif int(week) not in range(1,53):
        print("Enter a number 1 - 52 ")
        viewholidays()
    else:
        #get the dates for that week 

        weekyear = Week(int(year),int(week))
        
        #get the sunday and monday in order to establish a range of dates
        monday = weekyear.monday()
        sunday = weekyear.sunday()
        
        delta = sunday - monday

        days = [monday + timedelta(days=i) for i in range (delta.days + 1)]

        #enter the range of dates into a list
        rangedates = []

        #add the dates to rangedates
        for day in days:
            day = day.strftime("%b %d %Y")
            rangedates.append(day)

        #open json containing all of the holidays
        f = open('allholidays.json')
        data = json.load(f)

        #create a list of values that show the values of the given year
        listofvalues = [value for elem in data[year] for value in elem.values()]

        #create a list that intersects all the dates that both lists have in common
        finallist = list(set(rangedates).intersection(listofvalues))

        #sort the dates
        finallist.sort(key=lambda date: datetime.strptime(date, "%b %d %Y"))

        #blank list to store what would be shown to user
        holidaylist = []


        print("These are the holidays for " + str(year) + " week #" + str(week) + ":")

        #get the index of the holiday for the given week in the json file 
        for i in range(len(finallist)):
            
            holidayindex = next((index for (index, d) in enumerate(data[year]) if d["date"] == finallist[i]))

            #append to holiday list 
            holidaylist.append((data[year][holidayindex]['name'] + " (" + data[year][holidayindex]['date'] + ")"))

        #print the holidays for the given week
        for i in holidaylist:
            print(i)
            
def weekofweather():

    #Attempted to try to get the weather to match it with the dates of the given week but to no avail.

    url = "https://community-open-weather-map.p.rapidapi.com/forecast"

    querystring = {"q":"san francisco,us"}

    headers = {
            "X-RapidAPI-Key": "d94eea29d0msh1d2caeed79b0029p120f71jsn5294d9f7b081",
            "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
 
if __name__ == "__main__":
    getholidays()


