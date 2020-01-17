from homeworks.homework14.student import Student
from homeworks.homework14.quiz import Quiz

# STUDENTS
student1 = Student("Ty McFarland", "Computer Science", 3.1, False)
student2 = Student("Tar Pod", "Biology", 3.5, True)
student3 = Student("Ashe Astrairre", "Philology", 2.7, True)

student1.print_info()
student1.print_major()
print("\n")
student2.print_info()
student2.print_major()
print("\n")
student3.print_info()
student3.print_major()
print("\n\n\n")


# QUIZ

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n (c) Orange\n"
    "What color are the bananas?\n(a) Teal\n(b) Magenda\n (c) Yellow\n"
    "What color are strawberries?\n(a) Yellow\n(b) Red\n (c) Blue\n\n"
]


questions = [
    Quiz(question_prompts[0], "a"),
    Quiz(question_prompts[1], "c"),
    Quiz(question_prompts[2], "b ")
]


def run_test(question):
    score = 0
    for question in questions:
        answer = input(question_prompts)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "Correct")

run_test(questions)
quiz.asd()