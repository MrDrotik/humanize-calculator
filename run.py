from main import humanize
from sys import argv


def input_loop():
    print('If you want exit, write "exit".\nWrite your expression into a console:')
    while True:
        user_input = input()
        if user_input == 'exit' or user_input == 'quit':
            break
        print(humanize(user_input), is_solve_expression)


if __name__ == '__main__':
    if '-s' in argv:
        argv.remove('-s')
        is_solve_expression = True
    elif '--solve' in argv:
        argv.remove('--solve')
        is_solve_expression = True
    else:
        is_solve_expression = False

    if len(argv) == 1:
        input_loop()
    else:
        user_input = ''.join(argv[1:])
        print(humanize(user_input, is_solve_expression))
