import random
import time

file = open("quotes.txt", "r")
responses = file.readlines()
file.close()

exits = ("quit", "exit", "bye")

time.sleep(1.5)
print("\n"
      "Let's chat.\n"
      "- T-PAIN"
      "\n")
while True:
    user_input = input("> ")
    random.shuffle(responses)
    response = responses[-1]
    if user_input in exits:
        print("\n"
              "Be well, my friend.\n"
              "- T-PAIN"
              "\n")
        break
    else:
        time.sleep(.75)
        print(f" 😎 {response} ")
