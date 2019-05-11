char_names = (' plus', ' minus', ' multiply by', ' divide by', ' equals')
accepted_chars = ('+', '-', '*', '/', '=')
accepted_digits = tuple(map(str, range(0,10)))
skipped_chars = (' ', '\n', '\t', '\r')

digit_name_map = ( (
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
) )

# Нет, мне не лень было этим заниматься. Я вообще для этого
# регулярки использовал.
digit_categoty_map = {
    0 : '', 2 : ' hundred', 3 : ' thousand', 6 : ' million',
    9 : ' billion', 12 : ' trillion', 15 : ' quadrillion', 18 : ' quintillion',
    21 : ' sextillion', 24 : ' sepillion', 27 : ' octiillion', 30 : ' nonillion',
    33 : ' decillion', 36 : ' undecillion', 39 : ' duodecillion', 
    42 : ' tredecillion', 45 : ' quattuordecillion', 48 : ' quindecillion', 
    51 : ' sexdecillion', 54 : ' septendecillion', 57 : ' octodecillion', 
    60 : ' novemdecillion', 63 : ' vigintillion', 66 : ' unvigintillion', 
    69 : ' duovigintillion', 72 : ' tresvigintillion' ,
    75 : ' quattuorvigintillion', 78 : ' quinquavigintillion',
    81 : ' sesvigintillion', 84 : ' septemvigintillion', 
    87 : ' octovigintillion', 90 : ' novemvigintillion', 
    93 : ' trigintillion', 96 : ' untrigintillion', 99 : ' duotrigintillion',
    102 : ' trestrigintillion', 105 : ' quattuortrigintillion',
    108 : ' quinquatrigintillion', 111 : ' sestrigintillion',
    114 : ' septentrigintillion', 117 : ' octotrigintillion',
    120 : ' noventrigintillion', 123 : ' quadragintillion',
    153 : ' quinquagintillion', 183 : ' sexagintillion', 
    213 : ' septuagintillion', 243 : ' octogintillion',
    273 : ' nonagintillion', 303 : ' centillion', 306 : ' uncentillion',
    333 : ' decicentillion', 336 : ' undecicentillion',
    363 : ' viginticentillion', 366 : ' unviginticentillion',
    393 : ' trigintacentillion', 423 : ' quadragintacentillion',
    453 : ' quinquagintacentillion', 483 : ' sexagintacentillion',
    513 : ' septuagintacentillion', 543 : ' octogintacentillion',
    573 : ' nonagintacentillion', 603 : ' ducentillion', 903 : ' trecentillion',
    1203 : ' quadringentillion', 1503 : ' quingentillion',
    1803 : ' sescentillion', 2103 : ' septingentillion',
    2403 : ' octingentillion', 2703 : ' nongentillion', 3003 : ' millinillion'
}

validator_error_text = 'invalid input'
hyphen = '-'

def validate_chars(input):
    input = set(input)
    for char in input:
        if not char in accepted_chars and \
                not char in accepted_digits and \
                not char in skipped_chars:
            return False
    return True
    
    
def chunk_humanizer(input_str):
    
    out_str = ''
    
    if input_str in accepted_chars:
        index = accepted_chars.index(input_str)
        return char_names[index]
    
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
            # знать отображать ли приставку из digit_category_map.
            next_digits_sum = digit + next_digit
            if bit_depth+2 == number_tuple_len:
				# Добавляю единицу, а не два потому что кортеж
                # начинается с ноля, а разрядность числа с единицы.
                next_digits_sum += number_tuple[bit_depth + 1]
            if next_digits_sum > 0:
                # Отнимаю единицу потому что в bit_depth указана длина
                # числа, а в таблице степень десяти.
                out_str = digit_categoty_map[bit_depth - 1] + out_str
            
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
            if bit_depth == 3 and out_str:
                out_str = ' and' + out_str
            if digit > 0:
                out_str = digit_name_map[0][digit] + digit_categoty_map[2] + out_str
             
            
        previous_digit = digit
    return out_str

    
def humanizer(input_string):
    
    if not validate_chars(input_string):
        return validator_error_text
        
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
                chunk_buffer=''
            chunk_buffer += char
            if input_string_len == iteration:
                chunks_list.append(chunk_buffer)
            previous_char = char
        
    out_str = ''
    for element in chunks_list:
        if element:
            out_str += chunk_humanizer(element)
    return out_str.strip()