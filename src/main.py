app='Hello Heroes'
print(app)

 
# grade_system.py

def rank(score):
    if score >= 90 and score <= 100:
        return 'A'
    elif score >= 80 and score < 90:
        return 'B'
    elif score >= 70 and score < 80:
        return 'C'
    elif score >= 60 and score < 70:
        return 'D'
    else:
        return 'F'

def main():
    print("Welcome to the Grade System")
    try:
        score = int(input('Enter your score: '))
        if score < 0 or score > 100:
            print("Invalid score. Please enter a number between 0 and 100.")
        else:
            grade = rank(score)
            print(f'Your grade is: {grade}')
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()