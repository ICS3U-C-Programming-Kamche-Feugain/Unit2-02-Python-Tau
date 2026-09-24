#!/usr/bin/env python3\
# Created By:Kamche
# Created on: September 24, 2026
# This program ask the user for the raduis of
# a circle in mm. It the calculates and displays
# the circumference using tau
import constants


def main():
    # get the raduis from the user
    radius = float(input("Enter the radius of the circle in mm: "))

    # calculate the circumference
    circumference = constants.TAU * radius

    # display the circumference
    print("")
    print(" circumference = {} mm".format(circumference))


if __name__ == "__main__":
    main()
