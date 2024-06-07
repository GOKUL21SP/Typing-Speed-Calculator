from time import * #For calculating the time
import random as r #For creating random instances in program

#Function for finding the error in input user typed.
def mistake(paratest,usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i]!=usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error

#Function to calculate the typing speed
def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay,2)   #round()is used to round-off the time 
    speed = len(userinput)/time_r
    return round(speed)

if __name__ == '__main__':
    while True: 
        ck = input("READY TO TEST : Yes/No :")
        if ck == "Yes":
            #You can enter any sentence as the reference to user for checking
            test =["The quick brown fox jumps over the lazy dog.This sentence is a panagram.",
                "This paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.",
                "In the middle of difficulty lies opportunity, and every challenge is an opportunity to learn and grow.",
                "Success is not final, failure is not fatal: it is the courage to continue that counts.",
                "Reading a good book by the fireplace on a rainy day is one of the life's simple yet profound pleasures."]
            test1 = r.choice(test) # Used to take a random sentence from 'test'
            print("\n")
            print("********** TYPING SPEED CALCULATOR **********")
            print("\n",test1)
            print()
            print()
            time_1 = time()
            test_input=input(" Enter : ")
            time_2 = time()
            
            #The result is displayed as below
            print("Speed : ",speed_time(time_1,time_2,test_input)," w/sec")
            print("Error : ",mistake(test1,test_input))
        elif ck == "No":
            print("******** THANK YOU ********")
            break

        else:
            print("Invalid input.!!! Please retry.")