def square(num):
   return num * num

def convertTemp(temp, scale):
   if scale == "c":
      return (temp - 32.0) * (5.0/9.0)
   elif scale == "f":
      return temp * 9.0/5.0 + 32

def onePerLine(str):
   for i in str:
      print(i)



# number = 12
# print(square(number))

# temp = int(input("Enter a temperature: "))
# scale = input("Enter the scale to convert to: ")
# converted = convertTemp(temp, scale)
# print("The converted temp is: " + str(converted))

word = input("Enter a word: ")
onePerLine(word)