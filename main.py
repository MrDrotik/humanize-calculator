char_names = (' plus', ' minus', ' multiply by', ' divide by', ' equals')
accepted_chars = ('+', '-', '*', '/', '=', ' ')
accepted_digits = tuple(map(str, range(0,10)))

digit_map = ( ('', ' one', ' two', ' three',  ' four', ' five', ' six', ' seven', ' eight', ' nine'),
	(' ten', ' eleven', ' twelve', ' thirteen', ' fourteen', ' fifteen', ' sixteen', ' seventeen', ' eighteen', ' nineteen'),
	('', '', ' twenty', ' thirty', ' forty', ' fifty', ' sixty', ' seventy', ' eighty', ' ninety' ) )

# Нет, мне не лень было этим заниматься. Я вообще для этого регулярки использовал.
digit_categoty_map = {1 : '', 3 : ' hundred', 4 : ' thousand', 7 : ' million', 10 : ' billion', 13 : ' trillion', 16 : ' quadrillion', 19 : ' quintillion', 
	22 : ' sextillion', 25 : ' sepillion', 28 : ' octiillion', 31 : ' nonillion', 34 : ' decillion', 37 : ' undecillion', 40 : ' duodecillion', 43 : ' tredecillion', 
	46 : ' quattuordecillion', 49 : ' quindecillion', 52 : ' sexdecillion', 55 : ' septendecillion', 58 : ' octodecillion', 61 : ' novemdecillion', 
	64 : ' vigintillion', 67 : ' unvigintillion', 70 : ' duovigintillion' , 73 : ' tresvigintillion' , 76 : ' quattuorvigintillion' , 
	79 : ' quinquavigintillion' , 82 : ' sesvigintillion' , 85 : ' septemvigintillion' , 88 : ' octovigintillion' , 91 : ' novemvigintillion' , 94 : ' trigintillion' , 
	97 : ' untrigintillion' , 100 : ' duotrigintillion' , 103 : ' trestrigintillion' , 106 : ' quattuortrigintillion' , 109 : ' quinquatrigintillion' , 112 : ' sestrigintillion' , 
	115 : ' septentrigintillion' , 118 : ' octotrigintillion' , 121 : ' noventrigintillion' , 124 : ' quadragintillion'}

validator_error_text = 'invalid input'

def humanizers_validator(input):
	input = set(input)
	for char in input:
		if not char in accepted_chars and not char in accepted_digits:
			return False
	return True
	
def number_humanizer(input_str):
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
			# Добавлять единицу не нужно потому что 
			# кортеж начинается с ноля, а разрядность чисел с единицы.
			next_digit = number_tuple[bit_depth] 
			
		local_bit_depth = bit_depth % 3 
		
		if local_bit_depth == 1:
			
			# Тут я проверяю будут ли дальше числа кроме ноля чтобы знать 
			# отображать ли приставку из digit_category_map.
			next_digits_sum = 0
			for i in range(0,3):
				sum = bit_depth + i -1
				next_digits_sum += number_tuple[sum]
				if sum == number_tuple_len - 1:
					break
				
			if next_digits_sum > 0:
				out_str = digit_categoty_map[bit_depth] + out_str
			
			if next_digit == 1:
				out_str = digit_map[1][digit] + out_str
			else:
				out_str = digit_map[0][digit] + out_str
				
				
		elif local_bit_depth == 2:
			# Если цифра в переменной - единица, то значит этот отрезок уже обработан 
			# (одну итерацию назад на выводе был "eleven", "twelve", etc).
			if digit > 1:
				additional_symbol = ''
				if previous_digit != 0:
					additional_symbol = '-'
					out_str = out_str.lstrip()
				out_str = digit_map[2][digit] + additional_symbol + out_str
				
				
		elif local_bit_depth == 0:
			if bit_depth == 3 and out_str:
				out_str = ' and' + out_str
			if digit > 0:
				out_str = digit_map[0][digit] + digit_categoty_map[3] + out_str
				
			
		previous_digit = digit
	return out_str

	
	

def humanizer(input_string):
	if not humanizers_validator(input_string):
		return validator_error_text
		
	chunks_list = []
	buffer = ''
	previous_char = ''
	iteration = 0
	input_string_len = len(input_string)
	for char in input_string:
		iteration += 1
		if not char.isspace():
			if char.isdigit() != previous_char.isdigit():
				chunks_list.append(buffer)
				buffer=''
			buffer += char
			if input_string_len == iteration:
				chunks_list.append(buffer)
			previous_char = char
		
	out_str = ''
	for element in chunks_list:
		if element:
			out_str += number_humanizer(element)
	return out_str.strip()
		
