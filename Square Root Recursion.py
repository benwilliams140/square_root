running = True
nextNum = 0.0
curNum = 1.0
num = 0

def getNumber():
    try:
        #ensures the inputted value is a valid number
        num = float(input("\nEnter any real number that you want to square root: "))
        if num < 0:
            print("\n\nError: Please enter a positive real number.\n\n")
        return num
    except:
        print("\n\nError: Please enter a real number.\n\n")
        return -1

def calculateSR(curNum, num, counter):
    if counter == 0: return curNum
    else:
        fx = curNum * curNum - num #calculating value from original function (x^2 - a)
        fxp = 2 * curNum #calculating derivative of original function (2x)
        curNum = curNum - fx / fxp #using Newton's formula to approximate square root
        return calculateSR(curNum, num, counter - 1) #recalls the function

def main():
    running = False
    curNum = 1.0
    num = 0

    print("This program uses Newton's Method of Square Rooting to manually solve for the square root of any positive integer.")

    running = True
    while(running):
        curNum = 1.0 #resets the current number value
        num = getNumber() #gets the user input for the number
        if num < 0: continue
        curNum = calculateSR(curNum, num, 10) #calculates the square root

        print("The approximate value for the square root of " + str(num) + " is "
              + str(curNum) + ".")

        running = True if input("\nDo you want to square root another number? (y/n): ").upper() == 'Y' else False

main()
