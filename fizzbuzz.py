
def fizz_buzz(number):
    fbList = []
    for x in range(1, number):
        if (x%3 == 0 and x%5 != 0): 
            fbList.append("Fizz")
        elif (x%3 != 0 and x%5 == 0):
            fbList.append("Buzz")
        elif(x%3 == 0 and x%5 == 0):
            fbList.append("Fizz Buzz")
        else:
            fbList.append(str(x))
    return fbList

def fizz_buzzBranchless(number):
    fbList = []
    for x in range(1, number):
        fbList.append("Fizz"*(x%3==0) + "Buzz"*(x%5==0) + str(x)*(x%3!=0 and x%5!=0))
    return fbList
