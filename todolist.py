

def read():
    f = open("list.txt", "r+")
    print(f.read())
    f.close()


def write():
    with open("list.txt") as f:
        text = input("To do: ")
        i = len(f.readlines())
    with open("list.txt", "a+") as f:
        i = str(i)
        f.write(i)
        f.write(".")
        f.write(text)
        f.write("\n")
        f.close()

def check():
    numb = input("What number would you like to check off: ")
    with open("list.txt") as f:
        lines = f.readlines()
    i = 0
    with open("list.txt", "a+") as f: 
        for line in lines:
            if numb in line:
                break
            elif numb not in line:
                i += 1
        line= line.replace("\n","")
    with open("list.txt", "r") as f:
        x = f.readlines()
        
        x[i] = line +" Done\n"
    with open("list.txt", "w") as f:
        f.writelines(x)

        

def main():
    menu = int(input("""1.Read
2.Write
3.Check off \n:"""))

    if menu == 1:
        read()
    elif menu == 2:
        write()
    elif menu == 3:
        check()
while True:
    main()





