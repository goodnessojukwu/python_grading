try:
    score = float(input("Enter student's score (0 - 100): "))

    if not 0 <= score <= 100:
        print("Invalid score: must be between 0 and 100")
    elif score >= 70:
        print("Grade: A")
    elif score >= 60:
        print("Grade: B")
    elif score >= 50:
        print("Grade: C")
    elif score >= 45:
        print("Grade: D")
    elif score >= 40:
        print("Grade: E")
    else:
        print("Grade: F")

except ValueError:
    print("Invalid input: please enter a numeric value.")
