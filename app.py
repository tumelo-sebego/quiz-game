from string import ascii_lowercase
import random

# 1st iteration

# answer = input('What year was Mandela released from prision ')

# if answer == '1994':
#     print('Correct!')
# else:
#     print(f'The answer is 1994, not{answer!r}')

# answer = input('How many official languages are spoken in South Africa ')

# if answer == '11':
#     print('Correct!')
# else:
#     print(f'The answer is 11, not{answer!r}')

# 2nd iteration

# QUESTIONS = [('What year was Mandela released from prision', '1994'),
#              ('How many official languages are spoken in South Africa', '11'), ('What is the capital city of South Africa', 'Pretoria')]

# for question, answer in QUESTIONS:
#     u_answer = input(f'{question}? ')
#     if u_answer == answer:
#         print('Correct!')
#     else:
#         print(f'Incorrect, the answer is {answer!r} and not {u_answer!r}')


# 3rd iteration

# QUESTIONS = {'What year was Mandela released from prision': ['1994', '2001', '1990', '2014'],
#              'How many official languages are spoken in South Africa': ['11', '3', '21', '12'], 'What is the capital city of South Africa': ['Pretoria', 'Johannesburg', 'Cape Town', 'Durban']}

# for question, answers in QUESTIONS.items():
#     correct_answer = answers[0]
#     print(question)

#     for _ in sorted(answers):
#         print(f' - {_}')

#     u_answer = input('Your answer: ')

#     if u_answer == correct_answer:
#         print('correct!')
#     else:
#         print(
#             f'incorrect, the answer is {correct_answer!r} and not {u_answer!r} ')

# 4th iteration

# QUESTIONS = {'What year was Mandela released from prision': ['1994', '2001', '1990', '2014'],
#              'How many official languages are spoken in South Africa': ['11', '3', '21', '12'], 'What is the capital city of South Africa': ['Pretoria', 'Johannesburg', 'Cape Town', 'Durban']}

# for question, answers in QUESTIONS.items():
#     correct_answer = answers[0]
#     print(question)
#     sorted_answers = sorted(answers)

#     for index, _ in enumerate(sorted_answers):
#         print(f' {index}) {_}')

#     u_answer = sorted_answers[int(input('Your answer: '))]

#     if u_answer == correct_answer:
#         print('correct!')
#         print()
#     else:
#         print(
#             f'incorrect, the answer is {correct_answer!r} and not {u_answer!r} ')
#         print()

# 5th iteration

# QUESTIONS = {'What year was Mandela released from prision': ['1994', '2001', '1990', '2014'],
#              'How many official languages are spoken in South Africa': ['11', '3', '21', '12'], 'What is the capital city of South Africa': ['Pretoria', 'Johannesburg', 'Cape Town', 'Durban']}

# correct_num = 0
# for num, (question, answers) in enumerate(QUESTIONS.items(), start=1):
#     correct_answer = answers[0]
#     print(f'\nQuestion {num}')
#     print(f'{question}? ')

#     labeled_answers = dict(zip(ascii_lowercase, sorted(answers)))

#     for label, answer in labeled_answers.items():
#         print(f' {label}) {answer}')

#     u_answer = labeled_answers[(input('\nYour answer: ')).lower()]

#     if u_answer == correct_answer:
#         print('⭐ correct! ⭐')
#         correct_num += 1
#     else:
#         print(
#             f'incorrect, the answer is {correct_answer!r} and not {u_answer!r} ')
# print(f'\nYou got {correct_num} correct out of {num} questions')

# 6th iteration

# QUESTIONS = {'What year was Mandela released from prision': ['1994', '2001', '1990', '2014'],
#              'How many official languages are spoken in South Africa': ['11', '3', '21', '12'], 'What is the capital city of South Africa': ['Pretoria', 'Johannesburg', 'Cape Town', 'Durban']}

# correct_num = 0
# for num, (question, answers) in enumerate(QUESTIONS.items(), start=1):
#     correct_answer = answers[0]
#     print(f'\nQuestion {num}')
#     print(f'{question}? ')

#     labeled_answers = dict(zip(ascii_lowercase, sorted(answers)))

#     for label, answer in labeled_answers.items():
#         print(f' {label}) {answer}')

#     while (u_answer := input('\nYour answer: ')) not in labeled_answers:
#         print(f'Please answer one {", ".join(labeled_answers)}')

#     if labeled_answers[u_answer] == correct_answer:
#         print('⭐ correct! ⭐')
#         correct_num += 1
#     else:
#         print(
#             f'incorrect, the answer is {correct_answer!r} and not {u_answer!r} ')
# print(f'\nYou got {correct_num} correct out of {num} questions')

# 7th iteration

# NUM_QUESTIONS_PER_QUIZ = 5
# QUESTIONS = {'What year was Mandela released from prision': ['1994', '2001', '1990', '2014'],
#              'How many official languages are spoken in South Africa': ['11', '3', '21', '12'], 'What is the capital city of South Africa': ['Pretoria', 'Johannesburg', 'Cape Town', 'Durban']}

# num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
# rand_questions = random.sample(list(QUESTIONS.items()), k=num_questions)

# correct_num = 0
# for num, (question, answers) in enumerate(rand_questions, start=1):
#     correct_answer = answers[0]
#     print(f'\nQuestion {num}')
#     print(f'{question}? ')

#     labeled_answers = dict(
#         zip(ascii_lowercase, random.sample(answers, k=len(answers))))

#     for label, answer in labeled_answers.items():
#         print(f' {label}) {answer}')

#     while (u_answer := input('\nYour answer: ')) not in labeled_answers:
#         print(f'Please answer one {", ".join(labeled_answers)}')

#     if labeled_answers[u_answer] == correct_answer:
#         print('⭐ correct! ⭐')
#         correct_num += 1
#     else:
#         print(
#             f'incorrect, the answer is {correct_answer!r} and not {u_answer!r} ')
# print(f'\nYou got {correct_num} correct out of {num} questions')

# 8th iteration

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {'What year was Mandela released from prision': ['1994', '2001', '1990', '2014'],
             'How many official languages are spoken in South Africa': ['11', '3', '21', '12'], 'What is the capital city of South Africa': ['Pretoria', 'Johannesburg', 'Cape Town', 'Durban']}

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
rand_questions = random.sample(list(QUESTIONS.items()), k=num_questions)

correct_num = 0
for num, (question, answers) in enumerate(rand_questions, start=1):
    correct_answer = answers[0]
    print(f'\nQuestion {num}')
    print(f'{question}? ')

    labeled_answers = dict(
        zip(ascii_lowercase, random.sample(answers, k=len(answers))))

    for label, answer in labeled_answers.items():
        print(f' {label}) {answer}')

    while (u_answer := input('\nYour answer: ')) not in labeled_answers:
        print(f'Please answer one {", ".join(labeled_answers)}')

    if labeled_answers[u_answer] == correct_answer:
        print('⭐ correct! ⭐')
        correct_num += 1
    else:
        print(
            f'incorrect, the answer is {correct_answer!r} and not {u_answer!r} ')
print(f'\nYou got {correct_num} correct out of {num} questions')
