import math

def pythagorean_theorem(a, b, have_hypotenuse=False):
    if have_hypotenuse:
        return math.sqrt(abs(a**2 - b**2))
    else:
        return math.sqrt(a**2 + b**2)

def find_angle(opposite, adjacent, hypotenuse, method):
    if method.lower() == "sin":
        return math.degrees(math.asin(opposite / hypotenuse))
    elif method.lower() == "cos":
        return math.degrees(math.acos(adjacent / hypotenuse))
    elif method.lower() == "tan":
        return math.degrees(math.atan(opposite / adjacent))
    else:
        print("Error: Invalid method. Please choose 'sin', 'cos', or 'tan'.")
        return None

def main():
    print("Triangle Calculator Menu:")
    print("1. Use Pythagorean Theorem")
    print("2. Find an Angle")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        have_hypotenuse = input("Do you have the hypotenuse? (y/n): ").lower()
        if have_hypotenuse == "y":
            side_a = float(input("Enter the length of side a: "))
            hypotenuse = float(input("Enter the length of the hypotenuse: "))
            side_b = pythagorean_theorem(hypotenuse, side_a, have_hypotenuse=True)
            print(f"The length of side b is: {side_b:.2f}")
        elif have_hypotenuse == "n":
            side_a = float(input("Enter the length of side a: "))
            side_b = float(input("Enter the length of side b: "))
            hypotenuse = pythagorean_theorem(side_a, side_b)
            print(f"The length of the hypotenuse is: {hypotenuse:.2f}")
        else:
            print("Error: Invalid choice. Please enter 'y' or 'n'.")
    elif choice == "2":
        side1 = float(input("Enter the length of the first side: "))
        side2 = float(input("Enter the length of the second side: "))
        method = input("Choose a method ('sin', 'cos', or 'tan'): ")
        angle = find_angle(side1, side2, pythagorean_theorem(side1, side2), method)
        if angle is not None:
            print(f"The angle is: {angle:.2f} degrees")
    else:
        print("Error: Invalid choice. Please enter either '1' or '2'.")

if __name__ == "__main__":
    main()
