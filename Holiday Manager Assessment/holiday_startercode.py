from dataclasses import dataclass, field
from bs4 import BeautifulSoup
import requests
from datetime import date, datetime, timedelta
import json
import os.path
from isoweek import Week


# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------
@dataclass
class Holiday:
    name: str
    date: datetime

    def __str__(self):
        #Margaret Thatcher Day (2020-01-10)
        output = f"{self.name} ({self.date.strftime('%Y-%m-%d')})"
        return output
        
          
           
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
class HolidayList:
    def __init__(self):
       self.innerHolidays = []
       self.US_verbose_format = '%b %d %Y'
       self.Int_format = '%Y-%m-%d'
   
    def addHoliday(self, aholiday):
       if(isinstance(aholiday, Holiday)):
           self.innerHolidays.append(aholiday)
                    
    def addHolidayStr(self, holidayname, holiday_datestr, date_format):
        holiday_date = datetime.strptime(holiday_datestr, date_format)
        aholiday = Holiday(holidayname, holiday_date)
        self.addHoliday(aholiday)
    
    #file io, #read json    
    def start_up(self):
        f = open('allholidays.json')
        data = json.load(f)
        f.close()
        
        f2 = open('holidays.json')
        original_holidays = json.load(f2)
        f2.close()
    
        length2020 = len(data['2020'])
        length2021 = len(data['2021'])
        length2022 = len(data['2022'])
        length2023 = len(data['2023'])
        length2024 = len(data['2024'])
        lengthoriginal = len(original_holidays["holidays"])
        TotalLength = length2020 + length2021 + length2022 + length2023 + length2024 + lengthoriginal

        for year_int in range(2020, 2024):
            for holiday_dict in data[str(year_int)]:
                self.addHolidayStr(holiday_dict['name'],holiday_dict['date'], self.US_verbose_format)
        
        
        for holiday_dict in original_holidays['holidays']:
            self.addHolidayStr(holiday_dict['name'],holiday_dict['date'], self.Int_format)
            print("line 72")
        
        
        print(type(original_holidays["holidays"]))
        print("Holiday Management")
        print("==================")
        print("There are " + str(TotalLength) + " holidays stored in the system")

    #Web scrape,  #load json, 
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



# for holiday in hl.innerHolidays:
    # print(holiday) 




   
#     # def addHoliday(holidayObj):
        
        
        
#         # Make sure holidayObj is an Holiday Object by checking the type
#         # Use innerHolidays.append(holidayObj) to add holiday
#         # print to the user that you added a holiday

#     def findHoliday(HolidayName, Date):
#         # Find Holiday in innerHolidays
#         # Return Holiday

#     def removeHoliday(HolidayName, Date):
#         # Find Holiday in innerHolidays by searching the name and date combination.
#         # remove the Holiday from innerHolidays
#         # inform user you deleted the holiday

#     def read_json(filelocation):
#         # Read in things from json file location
#         # Use addHoliday function to add holidays to inner list.

#     def save_to_json(filelocation):
#         # Write out json file to selected file.
        
#     def scrapeHolidays():
#         # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
#         # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
#         # Check to see if name and date of holiday is in innerHolidays array
#         # Add non-duplicates to innerHolidays
#         # Handle any exceptions.     

#     def numHolidays():
#         # Return the total number of holidays in innerHolidays
    
#     def filter_holidays_by_week(year, week_number):
#         # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
#         # Week number is part of the the Datetime object
#         # Cast filter results as list
#         # return your holidays

#     def displayHolidaysInWeek(holidayList):
#         # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
#         # Output formated holidays in the week. 
#         # * Remember to use the holiday __str__ method.

#     def getWeather(weekNum):
#         # Convert weekNum to range between two days
#         # Use Try / Except to catch problems
#         # Query API for weather in that week range
#         # Format weather information and return weather string.

#     def viewCurrentWeek():
#         # Use the Datetime Module to look up current week and year
#         # Use your filter_holidays_by_week function to get the list of holidays 
#         # for the current week/year
#         # Use your displayHolidaysInWeek function to display the holidays in the week
#         # Ask user if they want to get the weather
#         # If yes, use your getWeather function and display results



# def main():
#     # Large Pseudo Code steps
#     # -------------------------------------
#     # 1. Initialize HolidayList Object
#     # 2. Load JSON file via HolidayList read_json function
#     # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
#     # 3. Create while loop for user to keep adding or working with the Calender
#     # 4. Display User Menu (Print the menu)
#     # 5. Take user input for their action based on Menu and check the user input for errors
#     # 6. Run appropriate method from the HolidayList object depending on what the user input is
#     # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 



def main_menu():
    hl = HolidayList()
    print("Holiday Menu")
    print("============")
    print("1. Add a Holiday")
    print("2. Remove a Holiday")
    print("3. Save Holiday List")
    print("4. View Holidays")
    print("5. Exit")
    userinput = input("What would you like to do? Please input a number 1-5 ")

    if userinput == '1':
        print("Add a Holiday")
        print("=============")
        holidaynameinput = input("Holiday : ")
        datestr = input("Date in format 'YYYY-MM-DD for " + holidaynameinput + " : ")
        hl.addHolidayStr(holidaynameinput,datestr,hl.Int_format)
    elif userinput == '2':
        print("remove holiday")
        #removeaholiday()
    elif userinput == '3':
        print("Save changes after adding or removing a holiday")
        #main_menu()
    elif userinput == '4':
        print("remove holiday")

        #viewholidays()
    elif userinput == '5':
        #print("Exiting program")
        exit()  
    else:
        #print("Choose a number 1 - 5: ")
        main_menu()




if __name__ == "__main__":
    main();


# # Additional Hints:
# # ---------------------------------------------
# # You may need additional helper functions both in and out of the classes, add functions as you need to.
# #
# # No one function should be more then 50 lines of code, if you need more then 50 lines of code
# # excluding comments, break the function into multiple functions.
# #
# # You can store your raw menu text, and other blocks of texts as raw text files 
# # and use placeholder values with the format option.
# # Example:
# # In the file test.txt is "My name is {fname}, I'm {age}"
# # Then you later can read the file into a string "filetxt"
# # and substitute the placeholders 
# # for example: filetxt.format(fname = "John", age = 36)
# # This will make your code far more readable, by seperating text from code.





