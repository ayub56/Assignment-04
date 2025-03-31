
print("01_add_two_numbers")

def add():
  print("This application for add two numbers")
  first_number = int(input("Enter your first number. "))
  second_number = int(input("Enter your second nunber. "))
  total = int(first_number + second_number)
  print(f'The total sum of {first_number} and {second_number} is {total}')

if __name__ == "__main__":
  add()



print("02_agreement_bot")

def bot():
  animal = str(input("what their favorite animal is? "))
  print(f'My favorite animal is also {animal}!')

if __name__ == "__main__":
  bot()


print("03_fahrenheit_to_celsius")

def temp():
  print("This code for converting fahrenheit to celsius")
  fahrenheit_degree = float(input("Enter your fahrenheit degree. "))
  celsius_degree = (fahrenheit_degree - 32) * 5.0/9.0
  print(f'Tempereture {fahrenheit_degree} F = {celsius_degree} C')

if __name__ == "__main__":
  temp()




print("04_how_old_are_they")

def add_ages():
  anthon:int = 21
  beth:int = anthon + 6
  chen:int = beth + 20
  drew:int = chen + anthon
  ethan:int = chen

  print("Anthon is " + str(anthon))
  print("Beth is " + str(beth))
  print("Chen is " + str(chen))
  print("Drew is " + str(drew))
  print("Ethen is " + str(ethan))


if __name__ == "__main__":
  add_ages()


print("05_triangle_perimeter.")

def triangle():
  print("This code is about perimeter of triangle.")
  side1:float = float(input("Enter your first side no of triangle. "))
  side2:float= float(input("Enter your second side no of triangke. "))
  side3:float = float(input("Enter your third side no of triangle. "))
  total:float = float(side1 + side2 + side3)
  print(f'The perimeter of the triangle is {total}')

if __name__ == "__main__":
  triangle()


print("06_square_number")

def square():
  print("This code is about square of given number")
  num1:int = int(input("Enter any number and i will give u a square value. "))
  print(f'The square of {num1} is {num1 ** 2}')

if __name__ == "__main__":
  square()


