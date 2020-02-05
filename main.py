def cleanlist(inputlst):
    lst = []
    for item in inputlst:
        lst.append(item[:-1])
    return lst

def getlist():
    with open("list.txt", 'r') as l:
        lst = l.readlines()
        lst = cleanlist(lst)
    return lst

def updatelist(inputlst):
    with open("list.txt", 'w') as l:
        for item in inputlst:
            l.write(item + "\n")

def printlist(inputlst):
    pass

def additem(inputlst):
    pass

def deleteitem(inputlst):
    pass

def menu():
    print("1) Print list")
    print("2) Add item")
    print("3) Delete item")
    print("4) quit")

def main():
    lst = getlist()
    updatelist(lst)

if __name__ == "__main__":
    main()
