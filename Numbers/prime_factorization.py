# Created on 28/05/2014
# Author: Tartuffe

def prime_factors(number):
    list=[]
    while number % 2 == 0:
        number = number / 2
        list.append(2)
    while number % 3 == 0:
        number = number / 3
        list.append(3)
    while number % 5 == 0:
        number = number / 5
        list.append(5)
    while number % 7 == 0:
        number = number / 7
        list.append(7)
        
    # maybe prime factor is prime number, so it couldn't be passed through loops above
    if number > 1: list.append(number)
    
    if len(list)==1:
        print number, " is prim number" 
    else:
        for fact in list:
            print fact, " ",
    
       
if __name__ == '__main__':
    number = raw_input("Please, input your number: ")
    
    # Capturing input error, input variable must be a number after converting with int(number)
    # (This block is not necessary for problem solving)
    isNumber=False 
    while not isNumber:
        try:
            number=int(number)
            isNumber=True
        except ValueError:
            number = raw_input("Please, you must input a number: ")
            isNumber=False
    #
    
    list=[]
    while number % 2 == 0:
        number = number / 2
        list.append(2)
    while number % 3 == 0:
        number = number / 3
        list.append(3)
    while number % 5 == 0:
        number = number / 5
        list.append(5)
    while number % 7 == 0:
        number = number / 7
        list.append(7)
        
    if number > 1: list.append(number)
    
    if len(list)==0:
        print number, " is prim number" 
    else:
        for fact in list:
            print fact, " ",
