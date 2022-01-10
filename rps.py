import random

user_score = 0
comp_score = 0
num_games = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_choice = input('Enter rock/paper/scissors or b to exit: ').lower()
    
    if user_choice == 'b':
        break
    elif user_choice not in options:
        continue

    rand = random.randint(0, 2)
    comp_choice = options[rand]
    print(f'Computer chose {comp_choice}')

    if comp_choice == user_choice:
        print('Draw')
    elif comp_choice == 'scissors' and user_choice == 'rock':
        print('You win!')
        user_score += 1
    elif comp_choice == 'paper' and user_choice == 'scissors':
        print('You win!')
        user_score += 1
    elif comp_choice == 'rock' and user_choice == 'paper':
        print('You win!')
        user_score += 1
    else:
        print('You lose!')
        comp_score += 1

    num_games += 1

print(f'You won {user_score} games!')
print(f'That was a {int((user_score / num_games) * 100)}% win rate!')
