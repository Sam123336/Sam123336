import math
#first creat a function which creat a list  then return it 
#then creat another function and pass the first function in it's atribute
#then take a input(in this function) and run a while loop which break when the number is 0 this loop append the numberes 
#then creat a another function join the number like 1x2x3x5x7 and use math.prod for multiply
#creat another function and pass all function in it then pass this function
def creatlist():
    myList=[]
    return myList
def fillList(myList):
    number=int(input("please enter a number:"))

    while number!=0:
        myList.append(number)
        number =int(input("please enter a number:"))
def printList(myList):
    print("x".join(map(str,myList)),end=" ")
    print(math.prod(myList))
def main():
    myList=creatlist()
    fillList(myList)
    printList(myList)
main()
