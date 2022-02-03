'''
  * ***************************************************************
  *      Program: MATSim Data Adapter
  *      Type: Python
  *      Author: David Velasco Garcia @davidvelascogarcia
  * ***************************************************************
'''

# Libraries
import os
os.environ["OPENCV_IO_MAX_IMAGE_PIXELS"] = pow(2,40).__str__()

import argparse
import cv2
import datetime
from halo import Halo
import pandas as pd
import platform


class MATSimDataAdapter:

    # Function: Constructor
    def __init__(self):

        # Build Halo spinner
        self.systemResponse = Halo(spinner='dots')

        # Build parser element
        parser = argparse.ArgumentParser()
        parser.add_argument("--input", "-i", default="./resources/network.jpg", help="Input image network.")
        parser.add_argument("--output", "-o", default="./database_fix.csv", help="Database fixed output file.")
        parser.add_argument("--database", "-d", default="./resources/database.csv",
                            help="Input database file to adapt with network coordinates system reference.")

        # Parse arguments
        args = parser.parse_args()
        self.input = args.input
        self.output = args.output
        self.database = args.database

    # Function: getSystemPlatform
    def getSystemPlatform(self):

        # Get system configuration
        print("\nDetecting system and release version ...\n")
        systemPlatform = platform.system()
        systemRelease = platform.release()

        print("**************************************************************************")
        print("Configuration detected:")
        print("**************************************************************************")
        print("\nPlatform:")
        print(systemPlatform)
        print("Release:")
        print(systemRelease)

        return systemPlatform, systemRelease

    # Function: getDatabase
    def getDatabase(self):

        # Read from file
        database = pd.read_csv(str(self.database), sep=";")

        print("Original database:\n")
        print(database)

        return database

    # Function: getAdapterParams
    def getAdapterParams(self):

        # Get adapter params from input
        network = cv2.imread(str(self.input))
        height, width, channels = network.shape

        print("\nHeight: " + str(height) + ", Width: " + str(width))

        return height, width

    # Function: getDatabaseParams
    def getDatabaseParams(self, database):

        # Get max X and Y coordinate value
        max_X = 0
        max_Y = 0

        for coordinateX in database.X_INIT:
            if int(coordinateX) > max_X:
                max_X = int(coordinateX)

        for coordinateX in database.X_DEST:
            if int(coordinateX) > max_X:
                max_X = int(coordinateX)

        for coordinateY in database.Y_INIT:
            if int(coordinateY) > max_Y:
                max_Y = int(coordinateY)

        for coordinateY in database.Y_DEST:
            if int(coordinateY) > max_Y:
                max_Y = int(coordinateY)

        print("Max x: " + str(max_X) + ", Max Y: " + str(max_Y) + "\n")

        return max_X, max_Y

    # Function: interpolateCoordinate
    def interpolateCoordinates(self, height, width, database, max_X, max_Y):

        # Get database columns
        x_init = []
        y_init = []

        # Get x, y coordinate distance module
        x_end = []
        y_end = []

        # Modify x coordinates, interpolate with network width
        for (coordinate, pos) in zip(database.X_INIT, range(int(len(database.X_INIT)))):

            value = float(coordinate) * (float(width)/float(max_X))
            value = str(value)
            value = value[:6]
            x_init.append(value)

        for (coordinate, pos) in zip(database.X_DEST, range(int(len(database.X_DEST)))):

            value = float(coordinate) * (float(width)/float(max_X))
            value = str(value)
            value = value[:6]
            x_end.append(value)

        # Modify y coordinates, interpolate with network height
        for (coordinate, pos) in zip(database.Y_INIT, range(int(len(database.Y_INIT)))):

            value = float(coordinate) * (float(height)/float(max_Y))
            value = str(value)
            value = value[:6]
            y_init.append(value)

        for (coordinate, pos) in zip(database.Y_DEST, range(int(len(database.Y_DEST)))):

            value = float(coordinate) * (float(height)/float(max_Y))
            value = str(value)
            value = value[:6]
            y_end.append(value)

        # Get time init and end
        time_init = []
        time_end = []

        # Get travel time init
        for (element, i) in zip(database.TIME_INIT, range(int(len(database.TIME_INIT)))):

            element = str(element)
            time_init.append(element)

        # Get travel time end
        for (element, i) in zip(database.TIME_DEST, range(int(len(database.TIME_DEST)))):

            element = str(element)
            time_end.append(element)

        # Get time duration
        duration = []

        # Get time travel duration
        for (element, i) in zip(database.DURATION, range(int(len(database.DURATION)))):

            element = str(element)
            duration.append(element)

        # Generate database
        database = pd.DataFrame({'X_INIT': x_init, 'X_DEST': x_end, 'Y_INIT': y_init, 'Y_DEST': y_end, 'TIME_INIT': time_init, 'TIME_DEST': time_end, 'DURATION': duration})

        print("Adapted database:\n")
        print(database)

        return database

    # Function: saveDatabase
    def saveDatabase(self, database):

        # Save database adapted
        database.to_csv(str(self.output), sep=";", index_label=False)

    # Function: processRequests
    def processRequests(self, height, width, database, max_X, max_Y):

        print("\n**************************************************************************")
        print("Processing request:")
        print("**************************************************************************\n")

        try:
            # Get initial time
            initialTime = datetime.datetime.now()

            # Adapt database to network
            database = self.interpolateCoordinates(height, width, database, max_X, max_Y)

            # Save into file
            self.saveDatabase(database)

            systemResponseMessage = "\n[INFO] Request done correctly.\n"
            self.systemResponse.text_color = "green"
            self.systemResponse.succeed(systemResponseMessage)

            # Get end time
            endTime = datetime.datetime.now()

            # Compute elapsed time
            elapsedTime = endTime - initialTime

            systemResponseMessage = "\n[INFO] Elapsed time: " + str(elapsedTime) + ".\n"
            self.systemResponse.text_color = "blue"
            self.systemResponse.info(systemResponseMessage)

        except:
            systemResponseMessage = "\n[ERROR] Error, processing request.\n"
            self.systemResponse.text_color = "red"
            self.systemResponse.fail(systemResponseMessage)


# Function: main
def main():

    print("**************************************************************************")
    print("**************************************************************************")
    print("                     Program: MATSim Data Adapter                         ")
    print("                     Author: David Velasco Garcia                         ")
    print("                             @davidvelascogarcia                          ")
    print("**************************************************************************")
    print("**************************************************************************")

    print("\nLoading MATSim Data Adapter engine ...\n")

    # Build matsimDataAdapter object
    matsimDataAdapter = MATSimDataAdapter()

    # Get system platform
    systemPlatform, systemRelease = matsimDataAdapter.getSystemPlatform()

    # Read database
    database = matsimDataAdapter.getDatabase()

    # Get adapter params
    height, width = matsimDataAdapter.getAdapterParams()

    # Get database params
    max_X, max_Y = matsimDataAdapter.getDatabaseParams(database)

    # Process input requests
    matsimDataAdapter.processRequests(height, width, database, max_X, max_Y)

    print("**************************************************************************")
    print("Program finished")
    print("**************************************************************************")
    print("\nmatsimDataAdapter program finished correctly.\n")

    #userExit = input()


if __name__ == "__main__":

    # Call main function
    main()