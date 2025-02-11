from random import randint, uniform, choice

settings = {
    'multiplication': {
        'lower_bound': 1,
        'upper_bound': 100,
        'decimal_on': False,
        'approximation_on': False,
    },
    'square_root': {
        'lower_bound': 1,
        'upper_bound': 10000,
        'decimal_on': False,
        'approximation_on': False,
    },
    'addition': {
        'lower_bound': 1,
        'upper_bound': 10000,
        'decimal_on': False,
        'approximation_on': False,
    },
    'subtraction': {
        'lower_bound': 1,
        'upper_bound': 10000,
        'decimal_on': False,
        'approximation_on': False,
    },
    'division': {
        'dividend_lower_bound': 1,
        'dividend_upper_bound': 10000,
        'divisor_lower_bound': 1,
        'divisor_upper_bound': 20,
        'decimal_on': False,
    },
    'square': {
        'lower_bound': 1,
        'upper_bound': 100,
        'decimal_on': False,
        'approximation_on': False,
    },
}

def multiplication(settings: dict) -> tuple:
    A = randint(settings['lower_bound'], settings['upper_bound'])
    B = randint(settings['lower_bound'], settings['upper_bound'])
    if settings['decimal_on']:
        A += uniform(0, 1)
        A = round(A, 2)

    ans = [A * B, A * B]
    if settings['approximation_on']:
        ans[0] -= ans[0] * settings['approximation_range']
        ans[1] += ans[1] * settings['approximation_range']

    return f'{A} x {B}: ', ans

def square_root(settings: dict) -> tuple:
    A = randint(settings['lower_bound'], settings['upper_bound'])
    if settings['decimal_on']:
        A += uniform(0, 1)
        A = round(A, 2)

    ans = [A ** 0.5, A ** 0.5]
    if settings['approximation_on']:
        ans[0] -= ans[0] * settings['approximation_range']
        ans[1] += ans[1] * settings['approximation_range']

    return f'√{A}: ', ans

def addition(settings: dict) -> tuple:
    A = randint(settings['lower_bound'], settings['upper_bound'])
    B = randint(settings['lower_bound'], settings['upper_bound'])

    ans = [A + B, A + B]
    if settings['approximation_on']:
        ans[0] -= ans[0] * settings['approximation_range']
        ans[1] += ans[1] * settings['approximation_range']

    return f'{A} + {B}: ', ans

def subtraction(settings: dict) -> tuple:
    A = randint(settings['lower_bound'], settings['upper_bound'])
    B = randint(settings['lower_bound'], settings['upper_bound'])

    ans = [A - B, A - B]
    if settings['approximation_on']:
        ans[0] -= ans[0] * settings['approximation_range']
        ans[1] += ans[1] * settings['approximation_range']

    return f'{A} - {B}: ', ans

def division(settings: dict) -> tuple:
    dividend = randint(settings['dividend_lower_bound'], settings['dividend_upper_bound'])
    divisor = randint(settings['divisor_lower_bound'], settings['divisor_upper_bound'])

    ans = [dividend / divisor, dividend / divisor]
    if settings['decimal_on']:
        ans[0] = round(ans[0], 2)
        ans[1] = round(ans[1], 2)

    return f'{dividend} / {divisor}: ', ans

def square(settings: dict) -> tuple:
    A = randint(settings['lower_bound'], settings['upper_bound'])
    if settings['decimal_on']:
        A += uniform(0, 1)
        A = round(A, 2)

    ans = [A * A, A * A]
    if settings['approximation_on']:
        ans[0] -= ans[0] * settings['approximation_range']
        ans[1] += ans[1] * settings['approximation_range']

    return f'{A}^2: ', ans


def generate_question(mode: str, settings: dict) -> tuple:
    if mode == 'multiplication':
        return multiplication(settings)
    elif mode == 'square_root':
        return square_root(settings)
    elif mode == 'addition':
        return addition(settings)
    elif mode == 'subtraction':
        return subtraction(settings)
    elif mode == 'division':
        return division(settings)
    elif mode == 'square':
        return square(settings)
    else:
        raise ValueError(f'Invalid mode: {mode}')
    
def main():
    streak = 0
    TOL = 2.5
    while True:
        mode = choice(list(settings.keys()))
        print(f'Mode: {mode}')
        question, ans = generate_question(mode, settings[mode])
        print(question)
        print('input: ', end='')
        user_input = input()
        if user_input == 'q':
            break
        print(f'Correct answer: {ans[0]}')
        print(f'Your answer: {user_input}')
        percentage_error = abs((ans[0] - float(user_input)) / ans[0]) * 100
        print(f'Percentage error: {abs((ans[0] - float(user_input)) / ans[0]) * 100}%')
        if percentage_error > TOL:
            break
        streak += 1
        print('Streak: ', streak)
        print()
    print()
    print('Game over')
    print('Streak: ', streak)


if __name__ == '__main__':
    main()