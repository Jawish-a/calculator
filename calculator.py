
def main():
	#write your code here
	num_1 = 0
	num_2 = 0
	

	num_1 = input("Enter the first number: ")

	while not num_1.isnumeric():
		print("enter a valid number!")
		num_1 = input("Enter the first number: ")

	num_2 = input("Enter the second number: ")

	while not num_2.isnumeric():
		print("enter a valid number!")
		num_2 = input("Enter the second number: ")

	operator = input("Choose the operation (+, -, /, *): ")

	if operator == "+":
    		answer = int(num_1) + int(num_2)
    		print ("The answer is " + str(int(answer)))
	elif operator == "-":
    		answer = int(num_1) - int(num_2)
    		print ("The answer is " + str(int(answer)))
	elif operator == "/":
    		answer = float(num_1) / float(num_2)
    		print ("The answer is " + str(int(answer)))
	elif operator == "*":
    		answer = int(num_1) * int(num_2)
    		print ("The answer is " + str(int(answer)))
	else:
    		print("please choose an operator")
    		
	



if __name__ == '__main__':
	main()
