# Configurable variables
nodeMessages = "NodeMessages_65987-2.txt"
nodeList = "KnownNodes-Sept23.txt"
listOfRecorders = ["DO", "D7", "DT", "DH", "1A", "DJ", "D6", "DN", "DM", "B7", "8J"]
numLocations = 6

# imports
from collections import namedtuple

# Global variable definitions
listOfNodes = []
lostNodeTupple = namedtuple('location', ['nodeID', 'time', 'lat', 'lon', 'alt'])
dictOfLostNodes = {}
# dictOfLostNodes['ZZ'] = lostNodeTupple("ZZ", "2000Z", "102N", "56W", "1200ft")
print(dictOfLostNodes)

with open(nodeList) as f:
    lines = f.readlines()
    for line in lines:
        listOfNodes.append(line.rstrip('\n'))

listOfKnownAssets = listOfNodes + listOfRecorders

print(listOfKnownAssets)

with open(nodeMessages) as f:  # read in base station log file
    messages = f.readlines()
    for message in reversed(messages):
        # print(message.split("ID:"))
        try:
            nodeID = message.split("ID:")[1].split(' ')[1]
        except:
            pass
        # print("EXCEPTION while reading node ID of below")
        # print(message)

        if nodeID not in listOfKnownAssets and ";G" in message:  # If contains node ID and GPS location
            if nodeID not in dictOfLostNodes.keys():
                time = []
                time.append(message.split("ID:")[0].split(' ')[0])
                gps = message.split("ID:")[1].split(' ')[3].split(';')[6].split(',')
                # print(time)

                lat = []
                # print(gps[0].replace('G','').find('.'))
                tempLat = gps[0].replace('G', '')
                lat.append(tempLat[:tempLat.find('.') - 2] + " " + tempLat[tempLat.find('.') - 2:] + "' " + gps[1])
                # print(lat)

                lon = []
                lon.append(gps[2][:gps[2].find('.') - 2] + " " + gps[2][gps[2].find('.') - 2:] + "' " + gps[3])
                # print(lon)

                alt = []
                try:
                    alt.append(gps[4] + " ft")
                except:
                    alt.append("NULL" + " ft")
                # print(alt)

                dictOfLostNodes[nodeID] = lostNodeTupple(nodeID, time, lat, lon, alt)
            else:
                if len(dictOfLostNodes[nodeID].time) < numLocations:
                    try:
                        dictOfLostNodes[nodeID].time.append(message.split("ID:")[0].split(' ')[0])
                        # print(gps)
                        gps = message.split("ID:")[1].split(' ')[3].split(';')[6].split(',')

                        tempLat = gps[0].replace('G', '')
                        dictOfLostNodes[nodeID].lat.append(
                            tempLat[:tempLat.find('.') - 2] + " " + tempLat[tempLat.find('.') - 2:] + "' " + gps[1])
                        # print(lat)

                        dictOfLostNodes[nodeID].lon.append(
                            gps[2][:gps[2].find('.') - 2] + " " + gps[2][gps[2].find('.') - 2:] + "' " + gps[3])
                        # print(lon)

                        try:
                            dictOfLostNodes[nodeID].alt.append(gps[4] + " ft")
                        except:
                            dictOfLostNodes[nodeID].alt.append("NULL" + " ft")
                    # print(alt)
                    # print(message)
                    except:
                        pass
print(dictOfLostNodes.keys())
print("name, desc, latitude, longitude, elevation")
for node in dictOfLostNodes:
    # print(dictOfLostNodes[node].nodeID)

    # print(len(dictOfLostNodes[node].time))
    # print( "name, desc, latitude, longitude, elevation")
    i = 0
    while i < len(dictOfLostNodes[node].time) - 1:
        print(dictOfLostNodes[node].nodeID + ", " + dictOfLostNodes[node].time[i] + ", " + dictOfLostNodes[node].lat[
            i] + ", " + dictOfLostNodes[node].lon[i] + ", " + dictOfLostNodes[node].alt[i])
        i += 1
# print('\n')
# print(dictOfLostNodes)

# print("name, desc, latitude, longitude, elevation")
# for node in dictOfLostNodes:
# print(dictOfLostNodes[node].nodeID + ", " + str(sum(float(dictOfLostNodes[node].time))/numLocations) + ", " + str(sum(float(dictOfLostNodes[node].lat))/numLocations) + ", " + str(sum(float(dictOfLostNodes[node].lon))/numLocations) + ", " + str(sum(float(statistics.mean(dictOfLostNodes[node].alt)))/numLocations))


