# ARGOSQueryTool.py
#
# Description: Parses a line of ARGOS tracking data 
#
# Created by: Emily C. Tucker (emily.tucker1@duke.edu)
# Created on: September 26, 2018

# Create a variable pointing to the file with no header
fileName = "SaraNoHeader.txt"

# Open the file as a read-only file object
fileObj = open(fileName, 'r')

# Read in all lines in the text file into a list variable
lineStrings = fileObj.readlines()
print("There are {} records in the file".format(len(lineStrings))) #create a dictionary, use the format command to tell it what to go in the dict

#close the file
fileObj.close()

#create empty dictionary
dateDict = {}
locationDict = {}

#Loop through everything using a while loop wite while followed by a condition
# this loop evaluates by goin to the next line, if the next line doesn't exist then the command is false and it will stop running
for lineString in lineStrings:
    # Use the split command to parse the items in lineString into a list object
    lineData = lineString.split("\t")

    # Assign variables to specfic items in the list
    recordID = lineData[0]              # ARGOS tracking record ID
    obsDateTime = lineData[2]           # Observation date and time (combined)
    obsDate = obsDateTime.split()[0]    # Observation date - first item in obsDateTime list object
    obsTime = obsDateTime.split()[1]    # Observation time - second item in obsDateTime list object
#object
    obsLC = lineData[3]                 # Observation Location Class
    obsLat = lineData[5]                # Observation Latitude
    obsLon = lineData[6]                # Observation Longitude

    #adds values to dictionaries
    dateDict[recordID] = obsDateTime
    locationDict[recordID] = (obsLon, obsLat)
    #indicate that script is finished
print("finished")

   