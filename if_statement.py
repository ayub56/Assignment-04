print("01_print_events")

def even():
  for i in range(40):
    even = i*2
    print(even)
  #  print("Here is 20 even numbers are: ",i * 2)


if __name__ == "__main__":
  even()



print("02_international_voting_age")

Peturksbouipo:int = 16
Stanlau:int = 25
Mayengua:int = 48
age:int = int(input("How old are you?"))

def main():

  if age >= Peturksbouipo:
    print(f"Your age is {age}.you are eligible to vote in Peturksbouipo!")
  else:
    print(f"Your age is {age}.you are not eligible to vote in Peturksbouipo!")


if age >= Stanlau:
      print(f"Your age is {age}.you are eligible to vote in Stanlau!")
else:
      print(f"Your age is {age}.you are not eligible to vote in Stanlau!")


if age >= Mayengua:
      print(f"Your age is {age}.you are eligible to vote in Mayengua!")
else:
      print(f"Your age is {age}.you are not eligible to vote in Mayengua!")

if __name__ == "__main__":
  main()
     


print("03_leap_year")

def leap_year():
  year:int = int(input("Enter as year."))

  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print(f'{year} is a leap year.')
      else:
        print(f"{year} is not a leap year.")
    else:
      print(f'{year} is not a leap year.')
  else:
    print(f"{year} is not a leap year.")

if __name__ == "__main__":
  leap_year()



print("04_tall_enough_to_ride")

min_height:int = 50
def main():
  user:int = int(input("How tall are you? "))
  if user >= min_height:
    print("you are tall enough to ride")
  else:
    print("you are not tall enough to ride.May be next year.")

if __name__ == "__main__":
  main()


import random

def main():
  for i in range(10):
    num:list[int] =  random.randint(1,100)
    print(num)

if __name__ == "__main__":
  main()
