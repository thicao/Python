def fizzbuzz(num):
    if div3(num) and div5(num):
        return "FizzBuzz"
    elif div3(num):
        return "Fizz"
    elif div5(num):
        return "Buzz"
    else:
        return num
            
    

def div3(n):
    if (n % 3 == 0):
        return True
    else:
        return False

def div5(n):
    if (n % 5 == 0):
        return True
    else:
        return False    
