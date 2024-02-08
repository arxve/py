def find_number_of_solutions(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        return "Two real solutions"
    elif discriminant == 0:
        return "One real solution (repeated root)"
    else:
        return "No real solutions (two complex conjugate solutions)"

if __name__ == "__main__":
    # Input coefficients a, b, and c
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the coefficient c: "))

    # Call the function and print the result
    result = find_number_of_solutions(a, b, c)
    print(result)
