from sys import argv
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
    if len(inputlst) > 0:
        colorlst = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.MAGENTA]
        for i, item in enumerate(inputlst, start=1):
            print(str(i) + ") " + colorlst[(i-1)%6] + item)
        print()
    else:
        print(Fore.RED + "The list is empty")

def additem(inputlst, item = None):
    if item == None:
        printlist(inputlst)
        item = input("Enter item> ")
    inputlst.append(item)


def deleteitem(inputlst):
    printlist(inputlst)
    if len(inputlst) <= 0:
        system("Pause")
    else:
        while 1:
            try: 
                index = getindex()
                if index != -1:
                    _ = inputlst.pop(index)
                break
            except:
                print(Fore.RED + "Invalid input")

def edititem(inputlst):
    printlist(inputlst)
    index = getindex()
    if index != -1:
        inputlst[index] = input("Enter item> ")

def rearangelist(inputlst):
    printlist(inputlst)
    while 1:
        index1 = getindex(" 1st ")
        if index1 != -1:
            index2 = getindex(" 2nd ")
            if index2 != -1:
                try:
                    inputlst[index1], inputlst[index2] = inputlst[index2], inputlst[index1]
                    break
                except:
                    print(Fore.RED + "Invalid input")
            else: break
        else: break

def getindex(numstr = " "):
    while 1:
        try:
            index = input("Enter"+numstr+"index> ")
            return int(index)-1
        except:
            if index == 'cancel':
                return -1
            print(Fore.RED + "Invalid input")

def menu():
    print(Fore.RED + "1) Print list")
    print(Fore.YELLOW + "2) Add item")
    print(Fore.GREEN + "3) Delete item")
    print(Fore.BLUE + "4) Edit item")
    print(Fore.CYAN + "5) Rearrange list")
    print(Fore.MAGENTA + "6) Quit")
    print()
    return getch()

def run_ui():
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
            edititem(lst)
        elif choice == b'5':
            rearangelist(lst)
        elif choice == b'6':
           break
        updatelist(lst)

def main():
    try:
        _ = argv.pop(0)
        length = len(argv)
        if length > 1:
            raise(Exception("Too many args"))
    except Exception as e:
        print("Error: " + str(e)) 
    else:
        if length == 0:
            run_ui()
        elif argv[0] == "--print" or argv[0] == "-p":
            printlist(getlist())
        else:
            lst = getlist()
            additem(lst, argv[0])
            updatelist(lst)

if __name__ == "__main__":
    main()
