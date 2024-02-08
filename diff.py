import difflib

def find_string_difference(string1, string2):
    # Create a Differ object
    differ = difflib.Differ()

    # Compare the two strings
    diff = differ.compare(string1, string2)

    # Join the differences to get a human-readable output
    result = '\n'.join(diff)

    return result

if __name__ == "__main__":
    # Input the two strings you want to compare
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    # Call the function and print the result
    difference = find_string_difference(string1, string2)
    print("\nString Difference:")
    print(difference)
