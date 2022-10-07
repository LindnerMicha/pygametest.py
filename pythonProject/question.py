from question_class import question

question_prompts = [
    "What Color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What Color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What Color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

question = [
    question(question_prompts[0], "a"),
    question(question_prompts[1], "c"),
    question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(question)