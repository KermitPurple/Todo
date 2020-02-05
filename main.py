from msvcrt import getch
from os import system
from colorama import init, Fore
init(autoreset=True)

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
    if len(inputlst) > 0:
        colorlst = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.MAGENTA]
        for i, item in enumerate(inputlst, start=1):
            print(str(i) + ") " + colorlst[(i-1)%6] + item)
        print()
    else:
        print(Fore.RED + "The list is empty")

def additem(inputlst):
    printlist(inputlst)
    inputlst.append(input("Enter item>"))

def deleteitem(inputlst):
    printlist(inputlst)
    if len(inputlst) <= 0:
        system("Pause")
    else:
        while 1:
            try:
                _ = inputlst.pop(int(input("Enter index>"))-1)
                break
            except:
                print(Fore.RED + "Invalid input")

def menu():
    system("cls")
    print(Fore.RED + "1) Print list")
    print(Fore.YELLOW + "2) Add item")
    print(Fore.GREEN + "3) Delete item")
    print(Fore.BLUE + "4) Quit")
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
