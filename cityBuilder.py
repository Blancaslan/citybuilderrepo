import json
import random
import time
import os
import threading

# stopwatch running on another thread that brings in taxes every 30 seconds
def stopwatch():
    timePassed = 0
    while(True):
        time.sleep(1)
        if timePassed == 60:
            timePassed = 0
            counter = 0
            while (counter <= 24):
                jsonfile = open("CityData.json").read()
                cityData = json.loads(jsonfile)
                govCurrency = cityData["cityVal"][0]["governmentcash"]
                buildfile = open("cityBuildings.json").read()
                buildingdata = json.loads(buildfile)
                buildinglist = buildingdata["citybuildings"]
                housenum = buildinglist[counter]
                houseoccupied = housenum["occupied"]
                housetype = housenum["type"]
                housepopulation = housenum["tier"]
                housetier = housenum["population"]
                counter = counter + 1
                if houseoccupied == True:
                    if housetype == "house":
                        tax = govCurrency + 100 * housepopulation * housetier
                        cityData["cityVal"][0]["governmentcash"] = govCurrency + 100 * housepopulation * housetier
                        taxes = json.dumps(cityData)
                        with open("CityData.json", "w") as handler:
                            handler.write(taxes)
                    elif housetype == "office":
                        tax = govCurrency + 200 * housepopulation * housetier
                        cityData["cityVal"][0]["governmentcash"] = govCurrency + 200 * housepopulation * housetier
                        taxes = json.dumps(cityData)
                        with open("CityData.json", "w") as handler:
                            handler.write(taxes)
            print(f"\nTaxes were paid\nMoney: {tax}")
        timePassed = timePassed + 1
timer = threading.Timer(1.0, stopwatch)
timer.start()

# Building class that is responsible for creating and editing all the houses in cityBuildings.json

class Building():

    def __init__(self, occupied, type, tier, population, education, location):
        self.occupied = occupied
        self.type = type
        self.tier = tier
        self.population = population
        self.education = education
        self.location = location

    def printObject(self):
        print(self.type, self.tier, self.population, self.education, self.location)

    def toJSON(self):
        return {
            "occupied": self.occupied,
            "type": self.type,
            "tier": self.tier,
            "population": self.population,
            "education": self.education,
            "location": self.location
        }

# Function used to create building objects for Buildings class, this also automatically stores them in cityBuildings.json based on location

def createObject():
    buildfile = open("cityBuildings.json").read()
    buildingdata = json.loads(buildfile)
    buildinglist = buildingdata["citybuildings"]

    a1 = buildinglist[0]["type"][0]
    b1 = buildinglist[1]["type"][0]
    c1 = buildinglist[2]["type"][0]
    d1 = buildinglist[3]["type"][0]
    e1 = buildinglist[4]["type"][0]
    a2 = buildinglist[5]["type"][0]
    b2 = buildinglist[6]["type"][0]
    c2 = buildinglist[7]["type"][0]
    d2 = buildinglist[8]["type"][0]
    e2 = buildinglist[9]["type"][0]
    a3 = buildinglist[10]["type"][0]
    b3 = buildinglist[11]["type"][0]
    c3 = buildinglist[12]["type"][0]
    d3 = buildinglist[13]["type"][0]
    e3 = buildinglist[14]["type"][0]
    a4 = buildinglist[15]["type"][0]
    b4 = buildinglist[16]["type"][0]
    c4 = buildinglist[17]["type"][0]
    d4 = buildinglist[18]["type"][0]
    e4 = buildinglist[19]["type"][0]
    a5 = buildinglist[20]["type"][0]
    b5 = buildinglist[21]["type"][0]
    c5 = buildinglist[22]["type"][0]
    d5 = buildinglist[23]["type"][0]
    e5 = buildinglist[24]["type"][0]


    print(f"\n  1 2 3 4 5\na {a1} {a2} {a3} {a4} {a5}\nb {b1} {b2} {b3} {b4} {b5}\nc {c1} {c2} {c3} {c4} {c5}\nd {d1} {d2} {d3} {d4} {d5}\ne {e1} {e2} {e3} {e4} {e5}\n")

    found = False
    counter = 0
    population = random.randint(1, 10)
    type = str(input("enter type: ")).lower()
    location = str(input("enter location: ")).lower()
    newClass = Building(True, type, 1, population, 0, location)

    jsonfile = open("cityBuildings.json").read()
    jsonload = json.loads(jsonfile)
    citybuildings = jsonload["citybuildings"]
    housenum = citybuildings[0]


    while(found==False):
        searchHouseNum = citybuildings[counter]["location"]
        if location == searchHouseNum:
            jsondump = newClass.toJSON()
            jsonload["citybuildings"][counter] = jsondump
            writejson = json.dumps(jsonload)
            with open("cityBuildings.json", "w") as handler:
                handler.write(writejson)
            found = True
        else:
            counter = counter + 1

print(f"This is the city limits, you can decide where you want buildings to go.\n\nInput building LOCATION and building TYPE in the terminal to build a 'house' or 'office'.\n")
while(True):
    createObject()