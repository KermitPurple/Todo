from msvcrt import getch
from os import system

listpath= "C:\\Users\\Shane\\Dropbox\\Desktop\\Coding\\python\\todo\\list.txt"

def cleanlist(inputlst):
    lst = []
    for item in inputlst:
        lst.append(item[:-1])
    return lst

def getlist():
    with open(listpath, 'r') as l:
        lst = l.readlines()
        lst = cleanlist(lst)
    return lst

def updatelist(inputlst):
    with open(listpath, 'w') as l:
        for item in inputlst:
            l.write(item + "\n")

def printlist(inputlst):
    system("cls")
    for i, item in enumerate(inputlst, start=1):
        print(str(i) + ") " + item)
    print()

def additem(inputlst):
    printlist(inputlst)
    inputlst.append(input("Enter item>"))

def deleteitem(inputlst):
    printlist(inputlst)
    _ = inputlst.pop(int(input("Enter index>"))-1)

def menu():
    system("cls")
    print("1) Print list")
    print("2) Add item")
    print("3) Delete item")
    print("4) quit")
    return getch()

def main():
    while 1:
        lst = getlist()
        choice = menu()
        if choice == b'1':
            printlist(lst)
            system("pause")
        elif choice == b'2':
            additem(lst)
        elif choice == b'3':
            deleteitem(lst)
        elif choice == b'4':
           break
        updatelist(lst)

if __name__ == "__main__":
    main()
