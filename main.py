#This program calculates the result of two user numbers and prints the results
terminateProgram = 'y'

while terminateProgram == 'y': #Program runs while y is true
    try:
        num1 = float(input('Enter the 1st number: '))
        num2 = float(input('Enter the 2nd number: '))
        operation = input('Enter the operation to perform ( +, -, x, /): ')
        add = '+'
        minus = '-'
        multiply = 'x'
        divide = '/'
        result = 0

        #Method to print the results of the calculation
        def printResult():
            print ("\n{} {} {} = {}".format(num1, operation, num2, result))

        #If statement to perform calculations
        if operation == add:
            result = num1 + num2
            printResult()

        elif operation == minus:
            result = num1 - num2
            printResult()

        elif operation == multiply:
            result = num1 * num2
            printResult()

        elif operation == divide:
            result = num1 / num2
            printResult()

        else:
            print ("Please enter an valid operation!\n")

    except:
        print ("Please enter a valid number!\n")

    terminateProgram = input('\nDo you want to continue? y/n: ')
