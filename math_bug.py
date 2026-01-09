def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    return total / len(numbers) 

def main():
    print("Welcome to the Average Calculator")
    scores = [] 
    result = calculate_average(scores)
    print(f"The average is: {result}")

if __name__ == "__main__":
    main()