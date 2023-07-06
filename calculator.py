import time
time.sleep(2)
print("hello and wellcome to atharva's calculator")
num1= input("enter number 1: ")
num1=int(num1)
time.sleep(1)
print("select your choice  adition: + | subraction: - | multiplication: * | division: /")
time.sleep(4)
choice=input("enter choice ( + | - | * | / )")
time.sleep(1)
num2= input("enter number 2: ")
num2=int(num2)
time.sleep(2)
do=input("do you want to calculate another number(yes|no)")
time.sleep(1)
if(do=="yes"):
    print("select your choice  adition: + | subraction: - | multiplication: * | division: /")
    time.sleep(4)
    choicea=input("enter choice ( + | - | * | / )")
    time.sleep(1)
    num3=int(input("enter number 3: "))
    time.sleep(1)
    counta=(input("continu(=|0)"))
    time.sleep(3)
    if(counta=="="):
      if(choice == "+")and(choicea=="+"):
         suma=num1+num2+num3
         print(suma)
      elif(choice == "+")and(choicea=="-"):
         mina=num1+num2-num3
         print(mina)
      elif(choice == "+")and(choicea=="*"):
         multia=num1+num2*num3
         print(multia)
      elif(choice == "+")and(choicea=="/"):
          dividea=num1+num2/num3
          print(dividea)
      elif(choice == "-")and(choicea=="+"):
          minpu=num1-num2+num3
          print(minpu)
      elif(choice == "-")and(choicea=="-"):
          minpi=num1-num2-num3
          print(minpi)
      elif(choice == "-")and(choicea=="*"):
          minpn=num1-num2*num3
          print(minpn)
      elif(choice == "-")and(choicea=="/"):
          minpt=num1-num2/num3
          print(minpt)
      elif(choice == "*")and(choicea=="+"):
         sumt=num1*num2+num3
         print(sumt)
      elif(choice == "*")and(choicea=="-"):
         minec=num1*num2-num3
         print(minec)
      elif(choice == "*")and(choicea=="*"):
         multitech=num1*num2*num3
         print(multitech)
      elif(choice == "*")and(choicea=="/"):
          dentoni=num1*num2/num3
          print(dentoni)
      elif(choice == "/")and(choicea=="+"):
          omgpt=num1/num2+num3
          print(omgpt)
      elif(choice == "/")and(choicea=="-"):
          blablaper=num1/num2-num3
          print(blablaper)
      elif(choice == "/")and(choicea=="*"):
          mustardsauce=num1/num2*num3
          print(mustardsauce)
      elif(choice == "/")and(choicea=="/"):
          iampro=num1/num2/num3
          print(iampro)
      else:
       print("invalid text please try again") 
    else:
     print("invalid text please try again")
elif(do=="no"):
    count=(input("continu(=|0)"))
    if(count=="="):
     if(choice == "+"):
       sum=num1+num2
       print(sum)
     elif(choice == "-"):
       min=num1-num2
       print(min)
     elif(choice == "*"):
      multi=num1*num2
      print(multi)
     elif(choice == "/"):
      divide=num1/num2
      print(divide)
     else:
      print("invalid text please try again") 
    else:
      print("invalid text please try again")
else:
      print("invalid text please try again")
time.sleep(5)