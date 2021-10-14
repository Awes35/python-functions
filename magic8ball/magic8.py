#author Kollen Gruizenga
#function for magic8ball, returns string randomly chosen
#based on mix of 10 "yes", 5 "no" and 5 "maybe"

import random

def getMagic8Ball():
    answers = ['Why of course!','Definitely!','Most certainly.',"I don't see why not",'I suppose so','Affirmative','Go ahead','Please, do!','By all means!','Indeed', #yes answers
               "That wouldn't be acceptable","Please don't",'That would be unwise',"Heavens no",'Never', #no answers
               'Not sure','Perhaps','Could be','Possibly','Might be'] #maybe
    return answers[random.randint(0,19)]
