
from latin_assembler import assemble_number_name

accepted_char_names = (' plus', ' minus', ' multiply by', ' divide by', ' equals')
accepted_chars = ('+', '-', '*', '/', '=')
accepted_digits = tuple(map(str, range(10)))
skipped_chars = (' ', '\n', '\t', '\r')

digit_name_map = ((
        '', ' one', ' two', ' three',  ' four', ' five', ' six', ' seven',
        ' eight', ' nine'
    ),
    (
        ' ten', ' eleven', ' twelve', ' thirteen', ' fourteen', ' fifteen',
        ' sixteen', ' seventeen', ' eighteen', ' nineteen'
    ),
    (
        '', '', ' twenty', ' thirty', ' forty', ' fifty', ' sixty', ' seventy',
        ' eighty', ' ninety'
    ))

# exponent_text = ' ten to the'
failed_validation_text = 'invalid input'
hyphen = '-'
connection_word = ' and'


# TODO: Добавить проверку на наличие чисел по сторонам от операндов
def expression_validate(input_str,
                        is_solve_expression):
    if not input_str or \
            not isinstance(input_str, str) or \
            input_str.count(accepted_chars[4]) != 1:
        return False
    splitted_str = input_str.split(accepted_chars[4])
    splitted_str = list(filter(lambda s: s and not s.isspace(), splitted_str))
    if is_solve_expression and len(splitted_str) < 1:
        return False
    elif not is_solve_expression and len(splitted_str) != 2:
        return False
    input_str = set(input_str)
    for char in input_str:
        if char not in accepted_chars and \
                char not in accepted_digits and \
                char not in skipped_chars:
            return False
    return True


def humanize_chunk(input_str):

    out_str = ''

    if input_str in accepted_chars:
        index = accepted_chars.index(input_str)
        return accepted_char_names[index]

    input_str = input_str[-1::-1]
    input_str = map(int, input_str)
    number_tuple = tuple(input_str)
    number_tuple_len = len(number_tuple)
    bit_depth = 0
    for digit in number_tuple:
        bit_depth += 1
        if number_tuple_len == bit_depth:
            next_digit = 0
        else:
            # Добавлять единицу не нужно потому что кортеж
            # начинается с ноля, а разрядность чисел с единицы.
            next_digit = number_tuple[bit_depth]

        local_bit_depth = bit_depth % 3

        if local_bit_depth == 1:

            # Тут я проверяю будут ли дальше числа кроме ноля чтобы
            # знать отображать ли приставку (hundred, thousand, etc)
            next_digits_sum = digit + next_digit
            if next_digits_sum:
                if bit_depth+2 == number_tuple_len:
                    # Добавляю единицу, а не два потому что кортеж
                    # начинается с ноля, а разрядность числа с единицы.
                    next_digits_sum += number_tuple[bit_depth + 1]
                if next_digits_sum > 0 and bit_depth > 1:
                    # Отнимаю единицу потому что в bit_depth указана длина
                    # числа, а в таблице степень десяти.
                    out_str = ' ' + assemble_number_name(bit_depth - 1) + out_str

            if next_digit == 1:
                out_str = digit_name_map[1][digit] + out_str
            else:
                out_str = digit_name_map[0][digit] + out_str

        elif local_bit_depth == 2:
            # Если цифра в переменной - единица, то значит этот
            # отрезок уже обработан (одну итерацию назад на выводе
            # был "eleven", "twelve", etc).
            if digit > 1:
                additional_symbol = ''
                if previous_digit != 0:
                    additional_symbol = hyphen
                    out_str = out_str.lstrip()
                out_str = digit_name_map[2][digit] + additional_symbol + out_str

        elif local_bit_depth == 0:
            if bit_depth == 3 and out_str.rstrip():
                out_str = connection_word + out_str
            if digit > 0:
                out_str = assemble_number_name(2) + out_str
                out_str = digit_name_map[0][digit] + ' ' + out_str

        previous_digit = digit
    return out_str


def humanize(input_string, is_solve_expression=False):
    if not expression_validate(input_string, is_solve_expression):
        return failed_validation_text

    # Разделяет строку на числа и операнды
    chunks_list = []
    chunk_buffer = ''
    previous_char = ''
    iteration = 0
    input_string_len = len(input_string)
    for char in input_string:
        iteration += 1
        if not char.isspace():
            if char.isdigit() != previous_char.isdigit():
                chunks_list.append(chunk_buffer)
                chunk_buffer = ''
            chunk_buffer += char
            if input_string_len == iteration:
                chunks_list.append(chunk_buffer)
            previous_char = char

    # Обрабатывает каждое число и операнд, полученные в предыдущем блоке for
    out_str = ''
    for element in chunks_list:
        if element == accepted_chars[4] and is_solve_expression:
            splitted_str = input_string.split(accepted_chars[4])
            str_for_evaluating = filter(lambda s: s and not s.isspace(), splitted_str[0])
            str_for_evaluating = ''.join(str_for_evaluating)
            print(str_for_evaluating)
            exp_solve = eval(str_for_evaluating)
            exp_solve = humanize_chunk(str(exp_solve))
            out_str = out_str + accepted_char_names[4] + exp_solve
            return out_str.strip()
        if element:
            out_str += humanize_chunk(element)
    return out_str.strip()
