class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question("What is the capital of France?\n(a) Paris\n(b) Rome\n(c) Madrid\n\n", "a"),
    Question("Who wrote 'Hamlet'?\n(a) Shakespeare\n(b) Dickens\n(c) Hemingway\n\n", "a"),
    Question("What is the largest mammal?\n(a) Elephant\n(b) Blue whale\n(c) Giraffe\n\n", "b")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt).strip().lower()
        if answer == question.answer:
            score += 1
    print(f"You got {score}/{len(questions)} correct!")

run_quiz(questions)
