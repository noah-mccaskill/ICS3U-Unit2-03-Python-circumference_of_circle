#!/usr/bin/env python3

# Created by: Noah McCaskill
# Created on: March 2022
# This program calculates the circumference of a circle

import constants


def main():
    # this function calculates the circumference of a circle

    # Input
    user_radius = int(input("Enter radius:"))

    # Process
    circumference = user_radius * constants.TAU

    # Output
    print("Circumference is {} mm².".format(circumference))
    print("\nDone.")


if __name__ == "__main__":
    main()
