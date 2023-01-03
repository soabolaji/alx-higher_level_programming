#!/usr/bin/python3
for i in range(10):
  for j in range(10):
    if i != j:
      print(f"{i:01d}{j:01d}", end=", " if not (i == 9 and j == 8) else "\n")
for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and digit2 == 9:
            print("{}{}".format(digit1, digit2))
        else:
            print("{}{}".format(digit1, digit2), end=", ")
