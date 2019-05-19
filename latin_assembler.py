unique_numbers = {
    0: '', 1: 'ten', 2: 'hundred', 3: 'thousand', 6: 'million', 9: 'billion',
    12: 'trillion', 15: 'quadrillion', 18: 'quintillion', 21: 'sextillion',
    24: 'septillion', 27: 'octillion', 30: 'nonillion'
}

latin_digit_prefix = (
    '', 'un', 'duo', 'tre', 'quattuor', 'quin',
    'sex', 'septen', 'octo', 'novem'
)

latin_tens_name = (
    '', 'dez', 'vigint', 'trigint', 'quadragint', 'quinquagint', 'sexagint',
    'septuagint', 'octogint', 'nonagint'
)

alternative_ten_number_name = 'dec'

latin_hundreds_names = ( 
    '', 'cent', 'ducent', 'trecent', 'quadringent', 'quingent', 'sescent',
    'septingent', 'octingent', 'nongent'
)

latin_thousands_name = (
    '', 'millia', 'duomillia', 'tremillia', 'quattuormillia',
    'quinquemillia', 'sexmillia', 'septemmillia', 'octomillia', 'novemmillia'
)


def number_name_assemble(count_of_zeros):
    
    if count_of_zeros in unique_numbers:
        return unique_numbers[count_of_zeros]
    
    assert isinstance(count_of_zeros, int) or \
        not count_of_zeros % 3 or \
        not count_of_zeros < 0 or \
        not count_of_zeros > 1200
    
    out_str = ''
    latin_number = (count_of_zeros - 3) / 3
    latin_number = int(latin_number)
    latin_number = str(latin_number)
    latin_number = latin_number[-1::-1]
    iteration = 0
    for digit in latin_number:
        iteration += 1
        digit = int(digit)
        local_iteration = iteration % 3
        
        if local_iteration == 1:
            if iteration > 1:
                if digit == 0:
                    out_str = latin_thousands_name[1] + out_str
                else:
                    out_str = latin_thousands_name[digit] + out_str
        
        elif local_iteration == 2:
            if iteration == 2 and count_of_zeros <= 60:
                tens_for_injection = alternative_ten_number_name 
            else:
                tens_for_injection = latin_tens_name[digit]
            out_str = latin_digit_prefix[previous_digit] + tens_for_injection + out_str
        
        elif local_iteration == 0:
            out_str = latin_hundreds_names[digit] + out_str
        
        previous_digit = digit
    return out_str + 'illion'
