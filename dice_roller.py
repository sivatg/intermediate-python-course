import random
def main():
  dice_rolls = 2
  dice_sum = 0
  for i in range(0, dice_rolls):
    roll = random.randint(1, 6)
    dice_sum = dice_sum + roll
    x = "You rolled a dice and the value is "
    y = x + str(dice_sum)
  print(y)
  print('Bye')


if __name__== "__main__":
  main()