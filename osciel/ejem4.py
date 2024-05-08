print("The Love Calculator is calculating your score...")
name1 = str(input("Name 1: ")) # What is your name?
name2 = str(input("Name 2: ")) # What is their name?

resultado = 0
x = name1.lower()
y = name2.lower()

pareja = str(x+(' ')+y)

print(pareja)


true = "true"
love = "love"
var1 = 0
var2 = 0

list(love)
list(true)

for i in range(len(love)):
    var2 = var2 + pareja.count(love[i])
    
for i in range(len(true)):
    var1 =  var1 + pareja.count(true[i])


print(str(var1) + str(var2))
resultado = var1 + var2


if resultado < 10 or resultado > 90:
  print(f'Your score is {resultado} , you go together like coke and mentos.')
elif resultado > 40 and resultado < 50:
  print(f"Your score is {resultado}, you are alright together.")
else:
  print(f'Your score is {resultado}')