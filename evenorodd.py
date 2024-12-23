import json

# File to store grades
grades_file = 'grades.json'

def load_grades():
    """Load grades from the JSON file."""
    try:
        with open(grades_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Return empty structure if file doesn't exist or is empty
        return {"labs": [], "quiz": []}

def save_grades(grades):
    """Save grades to the JSON file."""
    with open(grades_file, 'w') as f:
        json.dump(grades, f, indent=4)

def calculate_averages(grades):
    """Calculate the averages for labs and quizzes."""
    lab_avg = sum(grade['score'] for grade in grades['labs']) / len(grades['labs']) if grades['labs'] else 0
    quiz_avg = sum(grade['score'] for grade in grades['quiz']) / len(grades['quiz']) if grades['quiz'] else 0
    weighted_avg = (lab_avg * 0.4) + (quiz_avg * 0.6)
    return lab_avg, quiz_avg, weighted_avg

def display_averages(lab_avg, quiz_avg, weighted_avg):
    """Display the averages."""
    print(f"\nLab Average: {lab_avg:.2f}")
    print(f"Quiz Average: {quiz_avg:.2f}")
    print(f"Weighted Average: {weighted_avg:.2f}")

def view_grades(grades):
    """Display all grades with their names."""
    print("\n--- Current Grades ---")
    print("\nLabs:")
    for item in grades['labs']:
        print(f"Assignment: {item['name']} | Grade: {item['score']}")
    print("\nQuizzes:")
    for item in grades['quiz']:
        print(f"Assignment: {item['name']} | Grade: {item['score']}")

def main():
    # Load existing grades
    grades = load_grades()

    while True:
        print("\n--- Grade Management ---")
        print("1. Add a grade")
        print("2. Remove a grade")
        print("3. View current grades")
        print("4. Display averages")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            category = input("Enter category (labs or quiz): ").strip().lower()
            if category in grades:
                name = input(f"Enter the assignment name for {category}: ").strip()
                try:
                    grade = float(input(f"Enter grade for '{name}': "))
                    grades[category].append({'name': name, 'score': grade})
                    save_grades(grades)
                    print(f"Grade for '{name}' added to {category}.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            else:
                print("Invalid category.")

        elif choice == '2':
            category = input("Enter category (labs or quiz): ").strip().lower()
            if category in grades:
                name = input(f"Enter the assignment name to remove from {category}: ").strip()
                found = False
                for item in grades[category]:
                    if item['name'] == name:
                        grades[category].remove(item)
                        save_grades(grades)
                        print(f"Grade for '{name}' removed from {category}.")
                        found = True
                        break
                if not found:
                    print(f"No assignment found with the name '{name}'.")
            else:
                print("Invalid category.")

        elif choice == '3':
            view_grades(grades)

        elif choice == '4':
            lab_avg, quiz_avg, weighted_avg = calculate_averages(grades)
            display_averages(lab_avg, quiz_avg, weighted_avg)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
