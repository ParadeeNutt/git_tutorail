class MidtermChatBot:
    def __init__(self):
        self.subject_name = "AI for robot system"
        self.student_id_to_year = {
            6010502616: 7, 
        }

    def showSubjectName(self):
        print(f"Subject Name: {self.subject_name}")

    def showStudentYear(self, student_id):
        if student_id in self.student_id_to_year:
            print(f"Student {student_id} is in year {self.student_id_to_year[student_id]}")
        else:
            print(f"Student {student_id} is not found.")

    def calculator(self, operator, num1, num2):
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        else:
            result = None
        return result

    def main(self):
        while True:
            command = input("Enter a command ('subject', 'year', 'calc', or 'exit' to quit): ")
            if command == "exit":
                break
            elif command == "subject":
                self.showSubjectName()
            elif command == "year":
                student_id = int(input("Enter the student ID: "))
                self.showStudentYear(student_id)
            elif command == "calc":
                operator = input("Enter the operator (+, -, *, /): ")
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = self.calculator(operator, num1, num2)
                if result is not None:
                    print(f"Result: {result}")
                else:
                    print("Invalid operator. Please use +, -, *, or /.")

# Create an instance of the MidtermChatBot class
chatbot = MidtermChatBot()
chatbot.main()

