def calculate_average(numbers):
    total = sum(numbers)
    # Bug: This will crash if the list is empty
    return total / len(numbers) 

def main():
    print("Welcome to the Average Calculator")
    # This empty list will cause a crash
    scores = [] 
    result = calculate_average(scores)
    print(f"The average is: {result}")

if __name__ == "__main__":
    main()