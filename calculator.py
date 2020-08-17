
def main():
	#write your code here
	operators = ["+","-","/","*"]

	num_1 = input("Enter the first number: ")
	num_2 = input("Enter the second number: ")
	operator = input("Choose the operation (+, -, /, *): ")


	if not num_1.isdigit() or not num_2.isdigit() or operator not in operators:
		print("please enter a valid number")
	else:
		# cast to int
		num_1 = int(num_1) 
		num_2 = int(num_2) 
		result = 0
		# do the operation
		if operator == "+":
			result = num_1+num_2
		elif operator == "-":
			result = num_1-num_2
		elif operator == "/":
			result = int(float(num_1)/float(num_2))
		elif operator == "*":
			result = num_1*num_2
		
		print("the answer is " + str(result))
    		




if __name__ == '__main__':
	main()
