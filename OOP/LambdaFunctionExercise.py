import csv
import functools
from operator import itemgetter 
import json

#Globals
police_data = []
header_list = []
neighborhood_data = {}

def readfile():

    global police_data

    #getting data into a list of dictionaries

    with open('Detroit911Calls.csv', 'r') as f:
        reader = csv.reader(f, delimiter = ',')
        header_list = next(reader)
        for row in reader:
            adictionary = dict()
            for index, value in enumerate(row):
                adictionary[header_list[index]] = value
            police_data.append(adictionary)

    datafiltered()


def datafiltered():

    global police_data

    #Filter for zip codes
    police_data = list(filter(lambda x: x['zip_code'] != '0', police_data))
    police_data = list(filter(lambda x: x['zip_code'] != None, police_data))
    police_data = list(filter(lambda x: x['zip_code'] != '', police_data))

    # Filter for neighborhoods
    police_data = list(filter(lambda x: x['neighborhood'] != '0', police_data))
    police_data = list(filter(lambda x: x['neighborhood'] != None, police_data))
    police_data = list(filter(lambda x: x['neighborhood'] != '', police_data))

    stats()
    
def stats():

    #Average total response time
    averageresponsetimelist = list(map(itemgetter('totalresponsetime'), police_data))
    averageresponsetimelist = [x for x in averageresponsetimelist if x != '0']
    averageresponsetimelist = [x for x in averageresponsetimelist if x != '']
    
    totalresponsetime = functools.reduce(lambda x1, x2: float(x1) + float(x2), averageresponsetimelist)
    averageresponsetime = totalresponsetime / len(averageresponsetimelist)
    
    print("The average response time is " + str(averageresponsetime) + " minutes.")

    #Average dispatch time

    averagedispatchtimelist = list(map(itemgetter('dispatchtime'), police_data))
    averagedispatchtimelist = [x for x in averagedispatchtimelist if x != '0']
    averagedispatchtimelist = [x for x in averagedispatchtimelist if x != '']
    
    totaldispatchtime = functools.reduce(lambda x1, x2: float(x1) + float(x2), averagedispatchtimelist)
    averagedispatchtime = totaldispatchtime / len(averagedispatchtimelist)
    
    print("The average dispatch time is " + str(averagedispatchtime) + " minutes.")

    #Average total time

    averagetotallist = list(map(itemgetter('totaltime'), police_data))
    averagetotallist = [x for x in averagetotallist if x != '0']
    averagetotallist = [x for x in averagetotallist if x != '']
    
    totaltime = functools.reduce(lambda x1, x2: float(x1) + float(x2), averagetotallist)
    averagetotaltime = totaltime / len(averagetotallist)
    
    print("The average total time is " + str(averagetotaltime) + " minutes.")

    neighborhood()

def neighborhood(): 

    global neighborhooddata
    

    #getting unique neighborhoods
    neighborhoods = []
    for x in police_data:
        if (x['neighborhood'] not in neighborhoods):
            neighborhoods.append(x['neighborhood'])
    
    # adding the neighborhoods as keys to neighborhood_data
    for x in neighborhoods:
        neighborhood_data[x] = []
    
    # adding police_data values to neighborhood_data per neighborhood
    for row in police_data:
        neighborhood_data[row['neighborhood']].append(row)

    neighborhooddata()

def neighborhooddata():

    global neighborhood_data
    neighborhood_data_summary = dict()
    # Average response time
    for key in neighborhood_data:
        print(key)
        responsetime = []
        neighborhood_data_summary[key] = {}
        neighborhood_data_summary[key]['Average Response Time'] = ''
        for x in neighborhood_data[key]:
            if(x['totalresponsetime'] != ''):
                responsetime.append(x['totalresponsetime'].replace(',',''))
        AVT = float(functools.reduce(lambda x1, x2: float(x1) + float(x2), responsetime))
        ResponseTimeLength = float(len(responsetime))
        AVT = round(AVT / ResponseTimeLength,2)
        neighborhood_data_summary[key]['Average Response Time'] = AVT
        print("Average response time is: " + str(AVT))

  
    # Average dispatch time

        dispatchtime = []
        neighborhood_data_summary[key]['Average Dispatch Time'] = ''
        for x in neighborhood_data[key]:
            if(x['dispatchtime'] != ''):
                dispatchtime.append(x['dispatchtime'].replace(',',''))
        ADT = float(functools.reduce(lambda x1, x2: float(x1) + float(x2), dispatchtime))
        DispatchTimeLength = float(len(dispatchtime))
        ADT = round(ADT / DispatchTimeLength,2)
        neighborhood_data_summary[key]['Average Dispatch Time'] = ADT
        print("Average dispatch time is: " + str(ADT))

       # Average total time

        totaltime = []
        neighborhood_data_summary[key]['Average Total Time'] = ''
        for x in neighborhood_data[key]:
            if(x['totaltime'] != ''):
                totaltime.append(x['totaltime'].replace(',',''))
        ATT = float(functools.reduce(lambda x1, x2: float(x1) + float(x2), totaltime))
        TotalTimeLength = float(len(totaltime))
        ATT = round(ATT / TotalTimeLength,2)
        neighborhood_data_summary[key]['Average Total Time'] = ATT
        print("Average total time is: " + str(ATT))

    print(neighborhood_data_summary)

    jsonobject()

def jsonobject():
    
    print("Creating JSON")

    global police_data

    final = json.dumps(police_data)

    with open("policedata.json", "w") as f:
        for line in final:
            print(line,file=f)
    

readfile()
