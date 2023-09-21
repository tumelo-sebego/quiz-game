import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {'What year was Mandela released from prision': ['1994', '2001', '1990', '2014'],
             'How many official languages are spoken in South Africa': ['11', '3', '21', '12'], 'What is the capital city of South Africa': ['Pretoria', 'Johannesburg', 'Cape Town', 'Durban']}


def prepare_questions(questions, num_questions):
    num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(questions))
    return random.sample(list(questions.items()), k=num_questions)


def get_answer(question, alternatives):
    print(f'{question}?')
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))

    for label, alternative in labeled_alternatives.items():
        print(f' {label}) {alternative}')

    while (answer_label := input('\nChoose one? ')) not in labeled_alternatives:
        print(f'Please answer one of {", ".join(labeled_alternatives)}')

    return labeled_alternatives[answer_label]


def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print('⭐ Correct! ⭐')
        return 1
    else:
        print(f'Incorrect, the answer is {correct_answer!r}, not {answer!r}')
        return 0


def run_quiz():
    questions = prepare_questions(
        QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ)

    correct_count = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f'\nQuestion {num}')
        correct_count += ask_question(question, alternatives)
    print(f'\nYou got {correct_count} correct out of {num} questions')
