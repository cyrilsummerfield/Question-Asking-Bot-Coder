askone = input("Hello! What would you like your bot to ask first? ")
asktwo = input("What would you like your bot to ask after that? ")
askthree = input("What would you like your bot to ask after that? ")
say = input("What would you like your bot to say when it is done asking questions? ")
print("Awesome, I've wrote your code. Copy it and paste it into a code editor like visual studio code. Here it is:")
print("input(\""+askone+"\") input(\""+asktwo+"\") input(\""+askthree+"\") print(\""+say+"\")")

def myfunction(first,second,third,answer):
  input(first)
  input(second)
  input(third)
  print(answer)

run = input("Would you like me to run that code for you? ")
if run == "yes":
  print("--------------")
  myfunction(askone, asktwo, askthree, say)
  print("--------------")
  print("Bye!")
elif run == "no":
  print("Ok, bye!")

  