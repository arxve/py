def has_duplicate_letters(input_string):
    # Create a set to keep track of seen letters
    seen_letters = set()

    for letter in input_string:
        # Check if the letter is already in the set
        if letter in seen_letters:
            return True
        else:
            seen_letters.add(letter)

    # If no duplicates are found, return False
    return False

if __name__ == "__main__":
    # Input the string you want to check for duplicate letters
    input_string = input("Enter a string: ")

    # Call the function and print the result
    if has_duplicate_letters(input_string):
        print("The string has duplicate letters.")
    else:
        print("No duplicate letters found in the string.")
