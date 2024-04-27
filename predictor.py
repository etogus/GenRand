MIN_LENGTH = 100

user_value = ""

print("Please provide AI some data to learn...")

while len(user_value) < MIN_LENGTH:
    print("The current data length is {}, {} symbols left".format(len(user_value), MIN_LENGTH - len(user_value)))
    print("Print a random string containing 0 or 1:")
    user_input = input()
    user_input = "".join([x for x in user_input if x == '0' or x == '1'])
    user_value += user_input

print("Final data string:")
print(user_value)

print("You have $1000. Every time the system successfully predicts your next press, you lose $1.\n"
      "Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!")

user_balance = 1000

dic = {bin(x)[2:].zfill(3): [0, 0] for x in range(8)}

for i in range(len(user_value) - 3):
    triad = user_value[i:i + 3]
    following_bit = user_value[i + 3]
    if following_bit == '0':
        dic[triad][0] += 1
    elif following_bit == '1':
        dic[triad][1] += 1

# for k, v in dic.items():
#    print("{}: {},{}".format(k, v[0], v[1]))

while True:
    print("Print a random string containing 0 or 1:")
    new_input = input()
    if new_input == "enough":
        print("Game over!")
        break
    else:
        new_input = "".join([x for x in new_input if x == "1" or x == "0"])
        if len(new_input) <= 3:
            continue
        else:
            predictions = ""
            for i in range(len(new_input) - 3):
                triad = new_input[i:i + 3]
                guess = ""
                if dic[triad][0] >= dic[triad][1]:
                    guess = "".join("0")
                else:
                    guess = "".join("1")
                predictions += guess

            correct_prediction = 0
            for i in range(len(predictions)):
                if predictions[i] == new_input[i + 3]:
                    correct_prediction += 1

            print(f"predictions:\n{predictions}")
            print("Computer guessed {} out of {} symbols right ({} %)".format(correct_prediction, len(predictions),
                                                                              round(correct_prediction / len(
                                                                                  predictions) * 100,
                                                                                    2)))
            user_balance = user_balance - correct_prediction + (len(predictions) - correct_prediction)
            print(f"Your balance is now ${user_balance}")

            # Update data about user's inputs
            for i in range(len(new_input) - 3):
                triad = new_input[i:i + 3]
                following_bit = new_input[i + 3]
                if following_bit == '0':
                    dic[triad][0] += 1
                elif following_bit == '1':
                    dic[triad][1] += 1
