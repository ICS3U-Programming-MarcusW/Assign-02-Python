#!/usr/bin/env python3

# Created by: Marcus Wehbi
# Created on: Oct 2nd, 2022
# This program calculates the surface area and volume of an ellipsoid
# import the math module
import math


def main():
    # declare the variables
    # initialize volume to 0
    volume = 0
    # initialize surface area to 0
    surface_area = 0
    # get the units calculated from user
    user_input_units = str(input("Enter the units that you would like to calculate: "))

    # input
    # get the user input for the first axis length, as a float
    first_axis_length = float(
        input(
            "Enter the first axis length of the ellipsoid in ("
            + (user_input_units)
            + "): "
        )
    )
    # get the user input for the second axis length, as a float
    second_axis_length = float(
        input(
            "Enter the second axis length of the ellipsoid in ("
            + (user_input_units)
            + "): "
        )
    )
    # get the user input for the third axis length, as a float
    third_axis_length = float(
        input(
            "Enter the third axis length of the ellipsoid in ("
            + (user_input_units)
            + "): "
        )
    )

    # process
    # calculate the volume of the ellipsoid with the given three axis lengths
    volume = (
        4 / 3 * math.pi * first_axis_length * second_axis_length * third_axis_length
    )
    # calculate the surface area of the ellipsoid with the given three axis lengths
    surface_area = (
        4
        * math.pi
        * (
            (
                (((first_axis_length) * (second_axis_length)) ** 1.6)
                + (((first_axis_length) * (third_axis_length)) ** 1.6)
                + (((second_axis_length) * (third_axis_length)) ** 1.6)
            )
            / 3
        )
        ** 0.625
    )

    # output
    # print blank line
    print("")
    # print the volume of the ellipsoid, rounded to two decimal places adn cubed
    print(
        "The volume of an ellipsoid with axis lengths "
        + str(first_axis_length)
        + str(user_input_units)
        + ", "
        + str(second_axis_length)
        + str(user_input_units)
        + ", and "
        + str(third_axis_length)
        + str(user_input_units)
        + " is = {:,.2f}".format(volume)
        + user_input_units
        + "^3"
    )
    # print a blank line
    print("")
    # print the surface area of the ellipsoid, rounded to two decimal places and squared
    print(
        "The surface area of an ellipsoid with axis lengths "
        + str(first_axis_length)
        + str(user_input_units)
        + ", "
        + str(second_axis_length)
        + str(user_input_units)
        + ", and "
        + str(third_axis_length)
        + str(user_input_units)
        + " is = {:,.2f}".format(surface_area)
        + user_input_units
        + "^2"
    )


# run function (main)
if __name__ == "__main__":
    main()
