def get_grade_and_message(marks):
    if marks >= 90:
        return "A", "Excellent work! You should be proud of yourself! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good job! You are doing well, keep improving! 😊"
    elif marks >= 60:
        return "D", "Nice effort! Keep practicing and you will get even better! 💪"
    else:
        return "F", "Don't give up. Every expert started as a beginner. Keep trying! ❤️"


def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid input. Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number only.")


def main():
    print("=== Student Grade Calculator ===")
    student_name = input("Enter student name: ").strip()

    while not student_name:
        print("Name cannot be empty. Please enter a valid name.")
        student_name = input("Enter student name: ").strip()

    marks = get_valid_marks()
    grade, message = get_grade_and_message(marks)

    print(f"\n📊 RESULT FOR {student_name.upper()}:")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")


if __name__ == "__main__":
    main()