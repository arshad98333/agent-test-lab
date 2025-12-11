
def calculate_average(numbers):
    # This function is intended to calculate the average of a list of numbers.
    # However, it contains a bug where it incorrectly handles an empty list 
    # and also has an issue with integer division if all numbers are integers.
    if not numbers:
        return 0 # Bug: Should ideally raise an error or return None for an empty list
    total = sum(numbers)
    return total / len(numbers) # Bug: Integer division in some Python 2 environments, though less of an issue in Python 3

if __name__ == "__main__":
    test_numbers_1 = [10, 20, 30, 40, 50]
    print(f"Average of {test_numbers_1}: {calculate_average(test_numbers_1)}") # Expected: 30.0

    test_numbers_2 = [1, 2, 3]
    print(f"Average of {test_numbers_2}: {calculate_average(test_numbers_2)}") # Expected: 2.0

    test_numbers_3 = []
    print(f"Average of {test_numbers_3}: {calculate_average(test_numbers_3)}") # Expected: An error or None, but returns 0

    test_numbers_4 = [5, 2]
    print(f"Average of {test_numbers_4}: {calculate_average(test_numbers_4)}") # Expected: 3.5