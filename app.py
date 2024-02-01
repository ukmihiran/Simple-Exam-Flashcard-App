import json
import random

# Load questions from JSON file
def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions = json.load(file)
    return questions

# Present question to user
def present_question(question):
    print(question['prompt'])
    for option in question['options']:
        print(option)
    print("Type 'exit' to end the quiz.")

# Main function
def main():
    file_path = 'questions.json'
    questions = load_questions(file_path)
    random.shuffle(questions)

    score = 0
    total_questions = len(questions)

    for i, question in enumerate(questions, start=1):
        print(f'\nQuestion {i}/{total_questions}:')
        present_question(question)
        user_answer = input('Your answer: ').strip().upper()

        if user_answer == 'EXIT':
            print('Quiz ended. Your score:', score)
            break

        if user_answer == question['answer']:
            print(f'Correct! The answer is {question["answer"]}\n')
            score += 1
        else:
            print(f'Incorrect. The correct answer is {question["answer"]}\n')

    print(f'Your final score: {score}/{total_questions}')

if __name__ == "__main__":
    main()
