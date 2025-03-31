
import random
print("01_dicesimulator")

def roll_dice():
  die1:int = random.randint(1,6)
  die2:int = random.randint(1,6)
  total:int = die1 + die2
  print(f'Total of two dies: {total}')

def main():
  die1:int = 10
  print("die1 in main() start as: " + str(die1))
  roll_dice()
  roll_dice()
  roll_dice()
  print("die1 in main() is: " + str(die1))

if __name__ == "__main__":
  main()



print("02_e=mc2")

def energy():
  c:float = 299792458
  m:float = float(input("Enter Kilos of mass: "))
  print("e = m*c^2")
  print("Mass = " + str(m) + " kg")
  print("C = "+ str(c) + " m/s")
  print("e = " + str(m * c ** 2) + " jules")

if __name__ == "__main__":
  energy()



print("03_feet_to_inches")

inch: int = 12

def foot():
  feet:int = int(input("Enter feet and i will convert into inches. "))
  print(f'There are {inch * feet} inches in {feet} feet.')

if __name__== "__main__":
  foot()



import math
print("04_pythagorean_theorem")

def triangle():
  ab:float = float(input("Enter the length of the side ab. "))
  ac:float = float(input("Enter the length of the side ac. "))
  bc:float = math.sqrt(ab**2 + ac**2)
  print(f'The length of bc (the hypothenuse is : {bc})')

if __name__=="__main__":
  triangle()
     


print("05_remainder_division")

def reminder():
  num1:int = int(input("Enter an integer to be divided: "))
  num2:int = int(input("Enter an integer to divide by: "))
  quotient:int = num1 // num2
  remainder:int = num1 % num2
  print(f'The result of following division is {quotient} with the reminder of {remainder}')

if __name__ == "__main__":
  reminder()



import random
print("06_rolldice.")

def dice():
  die1:int= random.randint(1,6)
  die2:int  = random.randint(1,6)
  total:int = int(die1 + die2)
  print("First die: " + str(die1))
  print("Second die:" + str(die2))
  print(f'Total of two dies : {total}' )

if __name__=="__main__":
  dice()



print("06_seconds_in_year")

days_in_year:int = 365
hours_per_day:int = 24
minutes_per_hour:int = 60
seconds_per_minute:int = 60

def seconds():
  print(f'There are {days_in_year * hours_per_day * minutes_per_hour * seconds_per_minute} seconds in a year!')

if __name__=="__main__":
  seconds()



print("7_tiny_mad_lib")

def mad_lib():
  noun:str = str(input("Enter a noun: "))
  adjective:str = str(input("Enter an adjective: "))
  verb:str = str(input("Enter a verb: "))
  print(f"Do you {verb} your {adjective} {noun}?")



if __name__=="__main__":
  mad_lib()