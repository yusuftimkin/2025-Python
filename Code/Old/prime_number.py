def is_prime():
    num = int(input("Please enter a number: "))

    if num == 2:
        print("Prime")
        return True
    if num == 1:
        print("Not prime")
        return False
    
    divider_count = 0
    for i in range (1, num+1):
        if num % i == 0:
            divider_count += 1
                
    if divider_count == 2:
        print("Prime")
        return True
    else:
        print("Not prime")
        return False

is_prime()
