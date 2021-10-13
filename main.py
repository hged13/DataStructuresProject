# Name: Hannah Gedlaman
# Student ID: 001362181
import csv
import datetime

from Address import Address
from hashmap import HashMap
from Package import Package

# 2D array to hold distance data
distancedata = [[]]
# instance of hashmap
h = HashMap()
# packagedata array to pass in to hashmap add function
packagedata = []

# store string address with integer representing row in distance array
wgu = Address("4001 South 700 East", 1)
peace_garden = Address("1060 Dalton Ave S", 2)
sugar = Address("1330 2100 S", 3)
city_gov_off = Address("1488 4800 S", 4)
health_services = Address("177 W Price Ave", 5)
public_works = Address("195 W Oakland Ave", 6)
sanitation = Address("2010 W 500 S", 7)
lake = Address("2300 Parkway Blvd", 8)
ottinger = Address("233 Canyon Rd", 9)
library = Address("2530 S 500 E", 10)
city_hall = Address("2600 Taylorsville Blvd", 11)
police = Address("2835 Main St", 12)
council_hall = Address("300 State St", 13)
redwood = Address("3060 Lester St", 14)
mental_health = Address("3148 S 1100 W", 15)
police_dept = Address("3365 S 900 W", 16)
bus_loop = Address("3575 W Valley Central Station bus Loop", 17)
housing_auth = Address("3595 Main St", 18)
dmv = Address("380 W 2880 S", 19)
juvenile_court = Address("410 S State St", 20)
cottonwood_softball = Address("4300 S 1300 E", 21)
holiday_city_office = Address("4580 S 2300 E", 22)
museum = Address("5025 State St", 23)
valley_softball = Address("5100 South 2700 West", 24)
rock_springs = Address("5383 South 900 East #104", 25)
pavillion_park = Address("600 E 900 South", 26)
farm = Address("6351 South 900 East", 27)

# create hashmap by parsing csv data
#Space time complexity: O(N)
with open('WGUPS Package File copy.csv') as csvfile:
    readcsv = csv.reader(csvfile)

    for data_row in readcsv:
        package_ID = data_row[0]
        package_Address = data_row[1]
        # createpackageobject
        package = Package()
        package.id = data_row[0]
        package.address = data_row[1]
        package.city = data_row[2]
        package.state = data_row[3]
        package.zip = data_row[4]
        package.deadline = data_row[5]
        package.weight = data_row[6]
        package.notes = data_row[7]
        package.timestamp = 'At Hub '
        package.status = ' '

        packagedata = [package.id, package.address, package.city, package.state, package.zip, package.deadline,
                       package.weight, package.notes, package.timestamp, package.status]
        # addpackagetohashmap
        h.insert(package_ID, packagedata)

# populate distance data array
# 27 x 27 array that contains distances from each location to every other location
distancedata = [
    ['4001 South 700 East', '0.0', '7.2', '3.8', '11.0', '2.2', '3.5', '10.9', '8.6', '7.6', '2.8', '6.4', '3.2', '7.6',
     '5.2', '4.4', '3.7', '7.6', '2.0', '3.6', '6.5', '1.9', '3.4', '2.4', '6.4', '2.4', '5.0', '3.6'],
    ['1060 Dalton Ave S', '7.2', '0.0', '7.1', '6.4', '6.0', '4.8', '1.6', '2.8', '4.8', '6.3', '7.3', '5.3', '4.8',
     '3.0', '4.6', '4.5', '7.4', '6.0', '5.0', '4.8', '9.5', '10.9', '8.3', '6.9', '10.0', '4.4', '13.0'],
    ['1330 2100 S', '3.8', '7.1', '0.0', '9.2', '4.4', '2.8', '8.6', '6.3', '5.3', '1.6', '10.4', '3.0', '5.3', '6.5',
     '5.6', '5.8', '5.7', '4.1', '3.6', '4.3', '3.3', '5.0', '6.1', '9.7', '6.1', '2.8', '7.4'],
    ['1488 4800 S', '11.0', '6.4', '9.2', '0.0', '5.6', '6.9', '8.6', '4.0', '11.1', '7.3', '1.0', '6.4', '11.1', '3.9',
     '4.3', '4.4', '7.2', '5.3', '6.0', '10.6', '5.9', '7.4', '4.7', '0.6', '6.4', '10.1', '10.1'],
    ['177 W Price Ave', '2.2', '6.0', '4.4', '5.6', '0.0', '1.9', '7.9', '5.1', '7.5', '2.6', '6.5', '1.5', '7.5',
     '3.2', '2.4', '2.7', '1.4', '0.5', '1.7', '6.5', '3.2', '5.2', '2.5', '6.0', '4.2', '5.4', '5.5'],
    ['195 W Oakland Ave', '3.5', '4.8', '2.8', '6.9', '1.9', '0.0', '6.3', '4.3', '4.5', '1.5', '8.7', '0.8', '4.5',
     '3.9', '3.0', '3.8', '5.7', '1.9', '1.1', '3.5', '4.9', '6.9', '4.2', '9.0', '5.9', '3.5', '7.2'],
    ['2010 W 500 S', '10.9', '1.6', '8.6', '8.6', '7.9', '6.3', '0.0', '4.0', '4.2', '8.0', '8.6', '6.9', '4.2', '4.2',
     '8.0', '5.8', '7.2', '7.7', '6.6', '3.2', '11.2', '12.7', '10.0', '8.2', '11.7', '5.1', '14.2'],
    ['2300 Parkway Blvd', '8.6', '2.8', '6.3', '4.0', '5.1', '4.3', '4.0', '0.0', '7.7', '9.3', '4.6', '4.8', '7.7',
     '1.6', '3.3', '3.4', '3.1', '5.1', '4.6', '6.7', '8.1', '10.4', '7.8', '4.2', '9.5', '6.2', '10.7'],
    ['233 Canyon Rd', '7.6', '4.8', '5.3', '11.1', '7.5', '4.5', '4.2', '7.7', '0.0', '4.8', '11.9', '4.7', '0.6',
     '7.6', '7.8', '6.6', '7.2', '5.9', '5.4', '1.0', '8.5', '10.3', '7.8', '11.5', '9.5', '2.8', '14.1'],
    ['2530 S 500 E', '2.8', '6.3', '1.6', '7.3', '2.6', '1.5', '8.0', '9.3', '4.8', '0.0', '9.4', '1.1', '5.1', '4.6',
     '3.7', '4.0', '6.7', '2.3', '1.8', '4.1', '3.8', '5.8', '4.3', '7.8', '4.8', '3.2', '6.0'],
    ['2600 Taylorsville Blvd', '6.4', '7.3', '10.4', '1.0', '6.5', '8.7', '8.6', '4.6', '11.9', '9.4', '0.0', '7.3',
     '12.0', '4.9', '5.2', '5.4', '8.1', '6.2', '6.9', '11.5', '6.9', '8.3', '4.1', '0.4', '4.9', '11.0', '6.8'],
    ['2835 Main St', '3.2', '5.3', '3.0', '6.4', '1.5', '0.8', '6.9', '4.8', '4.7', '1.1', '7.3', '0.0', '4.7', '3.5',
     '2.6', '2.9', '6.3', '1.2', '1.0', '3.7', '4.1', '6.2', '3.4', '6.9', '5.2', '3.7', '6.4'],
    ['300 State St', '7.6', '4.8', '5.3', '11.1', '7.5', '4.5', '4.2', '7.7', '0.6', '5.1', '12.0', '4.7', '0.0', '7.3',
     '7.8', '6.6', '7.2', '5.9', '5.4', '1.0', '8.5', '10.3', '7.8', '11.5', '9.5', '2.8', '14.1'],
    ['3060 Lester St', '5.2', '3.0', '6.5', '3.9', '3.2', '3.9', '4.2', '1.6', '7.6', '4.6', '4.9', '3.5', '7.3',
     '0.0', '1.3', '1.5', '4.0', '3.2', '3.0', '6.9', '6.2', '8.2', '5.5', '4.4', '7.2', '6.4', '10.5'],
    ['3148 S 1100 W', '4.4', '4.6', '5.6', '4.3', '2.4', '3.0', '8.0', '3.3', '7.8', '3.7', '5.2', '2.6', '7.8', '1.3',
     '0.0', '0.6', '6.4', '2.4', '2.2', '6.8', '5.3', '7.4', '4.6', '4.8', '6.3', '6.5', '8.8'],
    ['3365 S 900 W', '3.7', '4.5', '5.8', '4.4', '2.7', '3.8', '5.8', '3.4', '6.6', '4.0', '5.4', '2.9', '6.6', '1.5',
     '0.6', '0.0', '5.6', '1.6', '1.7', '6.4', '4.9', '6.9', '4.2', '5.6', '5.9', '5.7', '8.4'],
    ['3575 W Valley Central Station bus Loop', '7.6', '7.4', '5.7', '7,2', '1.4', '5.7', '7.2', '3.1', '7.2', '6.7',
     '8.1', '6.3', '7.2', '4.0', '6.4', '5.6', '0.0', '7.1', '6.1', '7.2', '10.6', '12.0', '9.4', '7.5', '11.1', '6.2',
     '13.6'],
    ['3595 Main St', '2.0', '6.0', '4.1', '5.3', '0.5', '1.9', '7.7', '5.1', '5.9', '2.3', '6.2', '1.2', '5.9', '3.2',
     '2.4', '1.6', '7.1', '0.0', '1.6', '4.9', '3.0', '5.0', '2.3', '5.5', '4.0', '5.1', '5.2'],
    ['380 W 2880 S', '3.6', '5.0', '3.6', '6.0', '1.7', '1.1', '6.6', '4.6', '5.4', '1.8', '6.9', '1.0', '5.4', '3.0',
     '2.2', '1.7', '6.1', '1.6', '0.0', '4.4', '4.6', '6.6', '3.9', '6.5', '5.6', '4.3', '6.9'],
    ['410 S State St', '6.5', '4.8', '4.3', '10.6', '6.5', '3.5', '3.2', '6.7', '1.0', '4.1', '11.5', '3.7', '1.0',
     '6.9', '6.8', '6.4', '7.2', '4.9', '4.4', '0.0', '7.5', '9.3', '6.8', '11.4', '8.5', '1.8', '13.1'],
    ['4300 S 1300 E', '1.9', '9.5', '3.3', '5.9', '3.2', '4.9', '11.2', '8.1', '8.5', '3.8', '6.9', '4.1', '8.5',
     '6.2', '5.3', '4.9', '10.6', '3.0', '4.6', '7.5', '0.0', '2.0', '2.9', '6.4', '2.8', '6.0', '4.1'],
    ['4580 S 2300 E', '3.4', '10.9', '5.0', '7.4', '5.2', '6.9', '12.7', '10.4', '10.3', '5.8', '8.3', '6.2', '10.3',
     '8.2', '7.4', '6.9', '12.0', '5.0', '6.6', '9.3', '2.0', '0.0', '4.4', '7.9', '3.4', '7.9', '4.7'],
    ['5025 State St', '2.4', '8.3', '6.1', '4.7', '2.5', '4.2', '10.0', '7.8', '7.8', '4.3', '4.1', '3.4', '7.8',
     '5.5', '4.6', '4.2', '9.4', '2.3', '3.9', '6.8', '2.9', '4.4', '0.0', '4.5', '1.7', '6.8', '3.1'],
    ['5100 South 2700 West', '6.4', '6.9', '9.7', '0.6', '6.0', '9.0', '8.2', '4.2', '11.5', '7.8', '0.4', '6.9',
     '11.5', '4.4', '4.8', '5.6', '7.5', '5.5', '6.5', '11.4', '6.4', '7.9', '4.5', '0.0', '5.4', '10.6', '7.8'],
    ['5383 South 900 East #104', '2.4', '10.0', '6.1', '6.4', '4.2', '5.9', '11.7', '9.5', '9.5', '4.8', '4.9', '5.2',
     '9.5', '7.2', '6.3', '5.9', '11.1', '4.0', '5.6', '8.5', '2.8', '3.4', '1.7', '5.4', '0.0', '7.0', '1.3'],
    ['600 E 900 South', '5.0', '4.4', '2.8', '10.1', '5.4', '3.5', '5.1', '6.2', '2.8', '3.2', '11.0', '3.7', '2.8',
     '6.4', '6.5', '5.7', '6.2', '5.1', '4.3', '1.8', '6.0', '7.9', '6.8', '10.6', '7.0', '0.0', '8.3'],
    ['6351 South 900 East', '3.6', '13.0', '7.4', '10.1', '5.5', '7.2', '14.2', '10.7', '14.1', '6.0', '6.8', '6.4',
     '14.1', '10.5', '8.8', '8.4', '13.6', '5.2', '6.9', '13.1', '4.1', '4.7', '3.1', '7.8', '1.3', '8.3', '0.0']

]


# look up address function
# takes a string,
# calls lookup function from Address class
# returns integer of row and column to find address
#SpaceTime complexity: O(n)
def _look_up_(address):
    if address == "4001 South 700 East":
        return Address.lookupaddress(wgu)
    if address == "1060 Dalton Ave S":
        return Address.lookupaddress(peace_garden)
    if address == "1330 2100 S":
        return Address.lookupaddress(sugar)
    if address == "1488 4800 S":
        return Address.lookupaddress(city_gov_off)
    if address == "177 W Price Ave":
        return Address.lookupaddress(health_services)
    if address == "195 W Oakland Ave":
        return Address.lookupaddress(public_works)
    if address == "2010 W 500 S":
        return Address.lookupaddress(sanitation)
    if address == "2300 Parkway Blvd":
        return Address.lookupaddress(lake)
    if address == "233 Canyon Rd":
        return Address.lookupaddress(ottinger)
    if address == "2530 S 500 E":
        return Address.lookupaddress(library)
    if address == "2600 Taylorsville Blvd":
        return Address.lookupaddress(city_hall)
    if address == "2835 Main St":
        return Address.lookupaddress(police)
    if address == "300 State St":
        return Address.lookupaddress(council_hall)
    if address == "3060 Lester St":
        return Address.lookupaddress(redwood)
    if address == "3148 S 1100 W":
        return Address.lookupaddress(mental_health)
    if address == "3365 S 900 W":
        return Address.lookupaddress(police_dept)
    if address == "3575 W Valley Central Station bus Loop":
        return Address.lookupaddress(bus_loop)
    if address == "3595 Main St":
        return Address.lookupaddress(housing_auth)
    if address == "380 W 2880 S":
        return Address.lookupaddress(dmv)
    if address == "410 S State St":
        return Address.lookupaddress(juvenile_court)
    if address == "4300 S 1300 E":
        return Address.lookupaddress(cottonwood_softball)
    if address == "4580 S 2300 E":
        return Address.lookupaddress(holiday_city_office)
    if address == "5025 State St":
        return Address.lookupaddress(museum)
    if address == "5100 South 2700 West":
        return Address.lookupaddress(valley_softball)
    if address == "5383 South 900 East #104":
        return Address.lookupaddress(rock_springs)
    if address == "600 E 900 South":
        return Address.lookupaddress(pavillion_park)
    if address == "6351 South 900 East":
        return Address.lookupaddress(farm)
    else:
        return "invalid address"


# The trucks are loaded with the packages
# packages hand sorted to meet priority and special note requirements
truck1 = [13, 14, 15, 16, 17, 19, 20, 21, 34, 39, 27, 35, 30]
truck2 = [3, 18, 36, 38, 31, 32, 1, 6, 37, 25, 26, 4, 40, 28, 12, 29]
truck3 = [9, 2, 33, 10, 5, 11, 22, 23, 24, 7, 8]



# arrays for the sorting
# after sorting function is ran, these arrays will be used for the delivery
newtruck = []
newtruck2 = []
newtruck3 = []
# arrays to hold the distances
# stores distances of deliveries to easily calculate time later
truck1distances = []
truck2distances = []
truck3distances = []

# WGU address becuase the truck leaves from the Hub
currentaddress = "4001 South 700 East"

# find initial shortest distance -- TRUCK 1 --

# variable representing the column to find distance data.
# this variable starts at 1 as that is the correct column for distances from the hub.
distancecolumn = 1
# variable for while loop, starts at 1, ends when it reaches the length of the end variable.
n = 1
# end variable for truck 1.
end = int(len(truck1))
# end variable for truck 2.
end2 = int(len(truck2))
# end variable for truck 3.
end3 = int(len(truck3))

# total distance counter to keep track of mileage
totaldistance = 0

# iterates once for every element in truck 1
#space time complexity: O(n)
while n <= end:
    distance = 20
    # loops through all items that are currently in the truck 1 array
    for element in truck1:
        # the address of the element
        result = HashMap.getaddress(h, element)
        # if the address is the same as the last element's address, distance is zero and all variables are set.
        if result == currentaddress:
            id = int(element)
            distance = 0
            address = currentaddress
            int1 = int(_look_up_(address))

        else:
            # loops through each row in distance array
            for row in distancedata:
                # finds the row corresponding to the element
                if row[0].__contains__(result):
                    # checks to see if this element's distance is shorter than the last element checked
                    if float(distance) > float(row[distancecolumn]):
                        id = int(element)
                        # grabs distance data from the column corresponding to the last address
                        distance = float(row[distancecolumn])
                        address = HashMap.getaddress(h, id)
                        # returns new integer for the column of the new address
                        int1 = int(_look_up_(address))

    #after all elements have been checked, updates variables to the one that had the least difference
    distancecolumn = int1
    totaldistance += distance
    truck1distances.append(distance)
    newtruck.append(id)
    truck1.remove(id)
    currentaddress = HashMap.getaddress(h, id)

    n = n + 1

# returns truck1 to hub
#space time complexity: O(n)
for row in distancedata:
    if row[0].__contains__(currentaddress):
        distanceback = float(row[1])
        totaldistance += distanceback
# TRUCK 2
real = 1
currentaddress = "4001 South 700 East"

# Sorting algorithm TRUCK 2
#space time complexity: O(n)

n = 1
while n <= end2:
    distance = 20
    for element in truck2:

        result = HashMap.getaddress(h, element)
        if result == currentaddress:
            id = int(element)
            distance = 0
            address = currentaddress
            int1 = int(_look_up_(address))

        else:
            for row in distancedata:
                if row[0].__contains__(result):
                    if float(distance) > float(row[real]):
                        id = int(element)
                        distance = float(row[real])
                        address = row[0]
                        int1 = int(_look_up_(address))

    real = int1
    totaldistance += distance
    truck2distances.append(distance)
    newtruck2.append(id)
    truck2.remove(id)
    currentaddress = HashMap.getaddress(h, id)

    n = n + 1
# Sends truck 2 back to the hub
#space time complexity: O(n)

for row in distancedata:
    if row[0].__contains__(currentaddress):
        distanceback = float(row[1])
        totaldistance += distanceback

# Send packages on Truck 1 out for delivery
# Truck leaves at 8 AM
hourcount = 8
time = 0
# counter to access truck id, array starts at 0
n = 0
dt = str(datetime.timedelta(hours=8, minutes=0))

# uses distance data to calculate time
#space time complexity: O(n)

for element in truck1distances:

    if element != 0:
        time2 = int(element) * 3.333
        time += time2
        if time >= 60:
            hourcount += 1
            time = time - 60
        # updates time to old time + passed time
        dt = str(datetime.timedelta(hours=hourcount, minutes=time))
        # finds the id in the corresponding truck list
        id = newtruck[n]
        # adds timestamp to hashmap
        h.addtimestamp(id, dt)
    # adds same timestamp as last element if the distance is 0
    else:
        id = newtruck[n]
        h.addtimestamp(id, dt)
    n += 1

# send truck 2 out for delivery
#space time complexity: O(n)

hourcount2 = 9
timey = 5
n = 0
new = str(datetime.timedelta(hours=9, minutes=5))
for element in truck2distances:

    if element != 0:
        time2 = int(element) * 3.333
        timey += time2
        if timey >= 60:
            hourcount2 += 1
            timey = timey - 60

        new = str(datetime.timedelta(hours=hourcount2, minutes=timey))
        id = newtruck2[n]
        h.addtimestamp(id, new)
    else:
        id = newtruck2[n]
        h.addtimestamp(id, new)
    n += 1

# time is 10:20, update package
time3 = str(datetime.timedelta(hours=10, minutes=20))
#It is 10:20, updating address and leaving hub with truck 3
h.updateaddress(9, "410 S State St")
h.updatecity(9, "Salt Lake City")
h.updatestate(9, "UT")
h.updatezip(9, "84111")

# TRUCK 3 - SORT TRUCK 3 NOW THAT ADDRESS HAS BEEN CORRECTED -
#space time complexity: O(n)

n = 1
real = 1
currentaddress = "4001 South 700 East"
while n <= end3:
    distance = 20
    for element in truck3:

        result = HashMap.getaddress(h, element)
        if result == currentaddress:
            id = int(element)
            distance = 0
            address = currentaddress
            int1 = int(_look_up_(address))



        else:
            for row in distancedata:
                if real < len(row):
                    if row[0].__contains__(result):

                        if float(distance) > float(row[real]):
                            id = int(element)
                            distance = float(row[real])
                            address = row[0]
                            int1 = int(_look_up_(address))

    real = int1
    truck3distances.append(distance)
    totaldistance += distance
    currentaddress = HashMap.getaddress(h, id)

    newtruck3.append(id)
    truck3.remove(id)
    n = n + 1
# returns truck3 to hub
#space time complexity: O(n)

for row in distancedata:
    if row[0].__contains__(currentaddress):
        distanceback = float(row[1])
        totaldistance += distanceback


# send truck 3 out for delivery
hourcount2 = 10
timey = 20
n = 0
new = str(datetime.timedelta(hours=10, minutes=20))
for element in truck3distances:

    if element != 0:
        time2 = int(element) * 3.333
        timey += time2
        if timey >= 60:
            hourcount2 += 1
            timey = timey - 60

        new = str(datetime.timedelta(hours=hourcount2, minutes=timey))
        id = newtruck3[n]
        h.addtimestamp(id, new )
    else:
        id = newtruck3[n]
        h.addtimestamp(id, new)
    n += 1

# accepts a string as input
# converts the string to a time
format1 = "%H:%M:%S"
Time = input("Enter the hour to check delivery status:" + "(Enter in military time. format ex: 10:00:00")
timestring = datetime.datetime.strptime(Time, format1)
realtimestring = timestring.time()
format = "%H:%M:%S.%f"

truck1timestring = datetime.datetime.strptime("8:00:00", format1)
time1 = truck1timestring.time()
time2timestring = datetime.datetime.strptime("9:05:00", format1)
time2 = time2timestring.time()
truck3timestring = datetime.datetime.strptime("10:20:00", format1)
time3 = truck3timestring.time()

print("Truck 1 Packages:", newtruck)
print("Truck 2 Packages:", newtruck2)
print("Truck 3 Packages:", newtruck3)
print("Status as of", realtimestring)

# runs through each package
#space time complexity: O(n)

for package in newtruck:
    #gets the delivery status and time as a string
    result = (h.gettimestamp(package))
    # converts the string back to a time
    time = datetime.datetime.strptime(result, format)
    realtime = time.time()
    # compares the time of delivery to the entered time and the time the truck left. Sets status accordingly

    if realtimestring < time1:
        h.updatestatus(package, "At Hub")
    if time1 <= realtimestring < realtime:
        h.updatestatus(package, "En-Route")
    if realtimestring >= realtime:
        h.updatestatus(package, "Delivered")

for package in newtruck2:
    # space time complexity: O(n)
    # gets the delivery status and time as a string
    result = (h.gettimestamp(package))
    # converts the string back to a time
    time = datetime.datetime.strptime(result, format)
    realtime = time.time()
    # compares the time of delivery to the entered time and the time the truck left. Sets status accordingly

    if realtimestring < time2:
        h.updatestatus(package, "At Hub")
    if time2 <= realtimestring < realtime:
        h.updatestatus(package, "En-Route")
    if realtimestring >= realtime:
        h.updatestatus(package, "Delivered")

for package in newtruck3:
    # space time complexity: O(n)
    # gets the delivery status and time as a string
    result = (h.gettimestamp(package))
    # converts the string back to a time
    time = datetime.datetime.strptime(result, format)
    realtime = time.time()
    # compares the time of delivery to the entered time and the time the truck left. Sets status accordingly

    if realtimestring < time3:
        h.updatestatus(package, "At Hub")
    if time3 <= realtimestring < realtime:
        h.updatestatus(package, "En-Route")
    if realtimestring >= realtime:
        h.updatestatus(package, "Delivered")

n = 1
while n<= 40:
   result =  h.getstatus(n)
  # print function including delivery time if it has been delivered
   if result == "Delivered":
      print("PackageID: ", n, "     ", "status: ", result, h.gettimestamp(n))
    #print function if it has not yet been delivered
   else:
      print("PackageID: ", n, "     ", "status: ", result)
   n+=1

print("TOTAL MILEAGE TRAVELED DURING TRUCK ROUTE: ", totaldistance)