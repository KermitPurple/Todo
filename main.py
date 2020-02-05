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

def main():
    print(getlist())

if __name__ == "__main__":
    main()

