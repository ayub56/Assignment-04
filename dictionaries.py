print("00_count_nums")

def count_numbers():
  count_dict = {}

  while True:
    num = input("Enter a number (or 'Exit' to quit): ")
    if num.lower() == 'Exit':
      break
    if num.isdigit():
      num = int(num)
      count_dict[num] = count_dict.get(num, 0) + 1
      print(count_dict)
    else:
      print("Invalid input. Please enter a number or 'Exit'.")
      return count_dict

def display_counts(count_dict):
  print("\n Number Counts:")
  for key,value in count_dict.items():
      print(f'{key} appears {value} times')


if __name__ == "__main__":
  count = count_numbers()
  display_counts(count)