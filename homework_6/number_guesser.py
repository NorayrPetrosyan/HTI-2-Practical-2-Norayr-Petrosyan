def number_guesser(start, end, step_number):
    if step_number == 11:
        return "I couldn’t guess in 10 steps! This means you cheated!"

    guess_number = (start + end) // 2
    print(f'My guess number {step_number}: {guess_number}')
    input_number = int(input())

    if input_number == 0:
        return f'I guessed in {step_number} steps!'

    if input_number == 1:
        step_number += 1
        return number_guesser(guess_number, end, step_number)

    if input_number == -1:
        step_number += 1
        return number_guesser(start, guess_number, step_number)

def game_beginning(beginning_number):
    while beginning_number != 0:
        beginning_number = int(input('Input 0 once you’re ready to play: '))
    return number_guesser(1, 1000, 1)

beg_num = int(input('Think of a number between 1 and 999. Input 0 once you’re ready to play.'))
print(game_beginning(beg_num))