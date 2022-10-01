

def main():
	prev_result = 0

	while True:
		print('Добро пожаловать в калькулятор!')
		try:
			num1, operator, num2 = get_expression(prev_result)
		except ValueError:
			continue
		except KeyboardInterupt:
			break
		except TypeError:
			continue

		result = choose_action(num1, operator, num2)

		print('Результат: ', result)
		cntn = input('Продллжить вычисления с этим числом? ')
		if cntn == 'да':
			prev_result = result
		else:
			prev_result = 0
			close = input('Выйти из калькулятора? ')
			if close == 'да':
				print('Вы вышли из калькулятора!')
				break

def choose_action(num1, operator, num2):
	if operator == '+':
			return addition(num1, num2)
	if operator == '-':
			return subtraction(num1, num2)
	if operator == '*':
			return multiplication(num1, num2)
	if operator == '/':
			return division(num1, num2)

def get_expression(prev_result):
	try:
		if prev_result == 0: 
			num1 = int(input('Введите число: '))
		else:
			num1 = prev_result
			operator = input('Введите знак действия (*, /, +, -): ')
			num2 = int(input('Введите число: '))
			if operator == '/' and num2 == 0:
				raise ValueError
			return num1, operator, num2
	except ValueError:
		print('Ошибка!')

def addition(num1, num2):
	return num1 + num2
	
def subtraction(num1, num2):
	return num1 - num2

def multiplication(num1, num2):
	return num1 * num2

def division(num1, num2):
	return num1 / num2



if __name__ == '__main__':
	main()