#
# Project from https://www.youtube.com/watch?v=t8pPdKYpowI
#

import datetime

if __name__ == '__main__':
    user_input=input("Enter your goal with a deadline seperated by colons(i.e. 'goal:mo.day.yr'\n")
    input_list = user_input.split(":")
    goal = input_list[0]
    deadline = input_list[1]

    deadline_date=datetime.datetime.strptime(deadline, "%m.%d.%Y")

    time_remaing = deadline_date - datetime.datetime.today()

    print("The time remaining for your goal is {} days".format(time_remaing.days))
    hours_until = int(time_remaing.seconds / 60 )
    print("The time remaining for your goal is {} hours".format(hours_until))
    
    
