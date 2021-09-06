age=int(input("saisissez votre age : "))
if(age > 18):
    print("accès interdit")
elif(14 <=age< 18):
    print("accès payant")
elif(age < 14):
    print("accès gratuit")


