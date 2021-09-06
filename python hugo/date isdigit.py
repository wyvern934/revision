date = input("donnez la date sous la forme de j/m/an : ")
for element in date:
    if(element.isdigit()):
        print(element,end ="")
    else:
        print(end =" ")