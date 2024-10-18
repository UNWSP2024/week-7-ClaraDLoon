#Program #4: Coordinates
#Clara Riley
#Luke Snell
#10/18/24

import math

def distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2 + (coord2[2] - coord1[2])**2)

def main():
    try:
        x1 = float(input("For your first point in space enter x1: "))
        y1 = float(input("For your first point in space enter y1: "))
        z1 = float(input("For your first point in space enter z1: "))
        coord1 = (x1, y1, z1)

        x2 = float(input("For your second point in space enter x2: "))
        y2 = float(input("For your second point in space enter y2: "))
        z2 = float(input("For your second point in space enter z2: "))
        coord2 = (x2, y2, z2)

        dist = distance(coord1, coord2)

        print(f"The distance between {coord1} and {coord2} is {dist:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for the coordinates.")

if __name__ == '__main__':
    main()
