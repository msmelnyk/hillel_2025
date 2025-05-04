"""
1. Application - Python
2. User - Teacher in the school
3. Interface - TUI (Terminal User Interface)


struct Student:
    id: int
    name: str
    marks: list[int]
    info: str
struct Teacher: no structure since authentication process
"""

storage: list[dict] = [
    {
        "id": 1,
        "name": "Alice Johnson",
        "marks": [7, 8, 9, 10, 6, 7, 8],
        "info": "Alice Johnson is 18 y.o. Interests: math",
    },
    {
        "id": 2,
        "name": "Michael Smith",
        "marks": [6, 5, 7, 8, 7, 9, 10],
        "info": "Michael Smith is 19 y.o. Interests: science",
    },
    {
        "id": 3,
        "name": "Emily Davis",
        "marks": [9, 8, 8, 7, 6, 7, 7],
        "info": "Emily Davis is 17 y.o. Interests: literature",
    },
    {
        "id": 4,
        "name": "James Wilson",
        "marks": [5, 6, 7, 8, 9, 10, 11],
        "info": "James Wilson is 20 y.o. Interests: sports",
    },
    {
        "id": 5,
        "name": "Olivia Martinez",
        "marks": [10, 9, 8, 7, 6, 5, 4],
        "info": "Olivia Martinez is 18 y.o. Interests: art",
    },
    {
        "id": 6,
        "name": "Emily Davis",
        "marks": [4, 5, 6, 7, 8, 9, 10],
        "info": "Daniel Brown is 19 y.o. Interests: music",
    },
    {
        "id": 7,
        "name": "Sophia Taylor",
        "marks": [11, 10, 9, 8, 7, 6, 5],
        "info": "Sophia Taylor is 20 y.o. Interests: physics",
    },
    {
        "id": 8,
        "name": "William Anderson",
        "marks": [7, 7, 7, 7, 7, 7, 7],
        "info": "William Anderson is 18 y.o. Interests: chemistry",
    },
    {
        "id": 9,
        "name": "Isabella Thomas",
        "marks": [8, 8, 8, 8, 8, 8, 8],
        "info": "Isabella Thomas is 19 y.o. Interests: biology",
    },
    {
        "id": 10,
        "name": "Benjamin Jackson",
        "marks": [9, 9, 9, 9, 9, 9, 9],
        "info": "Benjamin Jackson is 20 y.o. Interests: history",
    },
]


# CRUD
def add_student(student: dict) -> dict | None:
    if not (2 <= len(student) <= 3):
        return None

    if not student.get("name") or not student.get("marks"):
        return None
    else:
        # action
        storage.append(student)

        return student


def show_students():
    print("=========================\n")
    for student in storage:
        print(f"{student['id']}. Student {student['name']}\n")
    print("=========================\n")


def search_student(student_id: int) -> None:
    for student in storage:
        info = (
            "=========================\n"
            f"[{student['id']}] Student {student['name']}\n"
            f"Marks: {student['marks']}\n"
            f"Info: {student['info']}\n"
            "=========================\n"
        )

        if student["id"] == student_id:
            print(info)
            return

    print(f"Student {student_id} not found")


def show_student(student_id: int) -> None:
    filtered_data = [s for s in storage if s.get('id') == student_id]
    if filtered_data:
        info = "=========================\n"
        for elem in filtered_data:
            for key, value in elem.items():
                info += f"{key.capitalize()}: {value}\n"
            info += "=========================\n"
        print(f"Student: \n{info}")
    else:
        print(f"Student {student_id} not found")


def ask_student_payload() -> dict:
    ask_prompt = (
        "Enter student's payload data using text template: "
        "John Doe;John Doe is 18 y.o. Interests: math\n"
        "where 'John Doe' is a full name"
        "and 'John Doe is 18 y.o. Interests: math' are optional info about student.\n"
        "The data must be separated by ';'"
    )

    def parse(data) -> dict:
        name, raw_marks, details = data.split(";")

        return {
            "name": name,
            "marks": [],
            "info": details | "",
        }

    user_data: str = input(ask_prompt)
    return parse(user_data)


def student_management_command_handle(command: str):
    if command == "show students":
        show_students()
    elif command == "show student":
        student_id: str = input("\nEnter student's ID: ")
        if student_id:
            show_student(student_id=int(student_id))
        else:
            print("Student's name is required to search")
    elif command == "add":
        data = ask_student_payload()
        if data:
            student: dict | None = add_student(data)
            print(f"Student: {student['name']} is added")
        else:
            print("The student's data is NOT correct. Please try again")
    elif command == "search":
        student_id: str = input("\nEnter student's ID: ")
        if student_id:
            search_student(student_id=int(student_id))
        else:
            print("Student's name is required to search")


def handle_user_input():
    OPERATIONAL_COMMANDS = ("quit", "help")
    STUDENT_MANAGEMENT_COMMANDS = ("show students", "show student", "add", "search")
    AVAILABLE_COMMANDS = (*OPERATIONAL_COMMANDS, *STUDENT_MANAGEMENT_COMMANDS)

    HELP_MESSAGE = (
        "Hello in the Journal! User the menu to interact with the application.\n"
        f"Available commands: {AVAILABLE_COMMANDS}"
    )

    print(HELP_MESSAGE)

    while True:

        command = input("\n Select command: ")

        if command == "quit":
            print("\nThanks for using the Journal application")
            break
        elif command == "help":
            print(HELP_MESSAGE)
        else:
            student_management_command_handle(command)


def main():
    handle_user_input()


if __name__ == "__main__":
    main()
