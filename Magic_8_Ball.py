import sys
import random
import time

thinktime = 5

ans = True

while ans:
    question = input("Ask me a question: ")
   
    answers = random.randint(1,8)
    print("Please wait as we connect NetFruit Technologies Server 1 to your console's Retrieval Data Package. This may take a while. Please do not turn off your device or exit this program...")
    time.sleep(thinktime)
   
   
    if question == "":
        sys.exit()
   

    elif answers == 1:
        print ("Unlikely")

    elif answers == 2:
        print ("Outlook good")
   
    elif answers == 3:
        print ("You will rely on it")
   
    elif answers == 4:
        print ("Ask again later")
   
    elif answers == 5:
        print ("Likely")

    elif answers == 6:
        print ("Apologies, try again")
   
    elif answers == 7:
        print ("My reply is most unfortunately no")
   
    elif answers == 8:
        print ("My sources of pentabytes of data say yes")
