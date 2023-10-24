#Write a program that gets a number from an input and prints 100 of them

#i.e.
#input is 256 and output is 2
#input = -256, output = 2
#input is 1456.32, output = 4
#input = 78, output = 0


def main():
    number = int(input("Give me a number: "))
    hundred = int(number//10)
    only_hundred = hundred // 10
    if only_hundred > 10:
        print(only_hundred % 10)
    else:
        print("There is no hundreds value")
    
main()



def main():
    num1 = getData() #Has to return valid data
    num2 = getData()
    if getSum(num1) == getSum(num2):
        print("Equal")
    else:
        print("Unequal")

    #it seems that num1 is getting the sum of every even number
    #num2 is getting the sum of every odd number

def getData():
    num1 = str(input("Give me a number: "))
    for n in num1:
        even_sum = 0
        if int(n) % 2 == 0:
            even_sum += 1
            return even_sum
    num2 = str(input("Give me a number: "))
    for n in num2:
        odd_sum = 0
        if int(n) % 2 == 1:
            odd_sum += 1
            return odd_sum

def getSum(num1, num2):
    num1 = getData(num1)
    num2 = getData(num2)

main()