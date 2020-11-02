###Clock 

import webbrowser
import os
import time

'''webbrowser.open('URL')'''
#will open a URL

#########Classes#########
PD1 = "https://mcpsmd.zoom.us/j/93615343796?pwd=QUE3V2U5YlJkNGdqR05xeUxIZVIrUT09"
#English
PD2 = "https://mcpsmd.zoom.us/j/87202300092?pwd=eE43aWxKQmhYdkZxc0NwWktpU1RnZz09"
#Math
PD3 = "https://mcpsmd.zoom.us/j/84016873002?pwd=aVh1QU1QM1JvUWw5bmJNNitjNjNKZz09&uname=Ates%2C+Thomas+C+%28Student%29"
#CompSi
PD4 = "https://mcpsmd.zoom.us/j/97692204600?pwd=VFFNTEYzcDc2L0xqS3pqaHAxOXd4Zz09"
#Econ
name = "Tommy"

#Greating
print("Good Morning " + name + "!")

while True:
#Loop running to see what time it is    
    from datetime import datetime
    #Takes time from computer
 
    now = datetime.now()
    #Sets time as var "now"

    now = str(now).split(" ")[1].split('.')[0]
    #Splits time to just hr:min:sec form

    time.sleep(1)#wait 1 second for time to be set

    if now == "8:59:00":#If now is 8:59:00 for English
        webbrowser.open(PD1)
        print("English is about to start")
    if now == "10:14:00":#If now is 10:14:00 for Math
        webbrowser.open(PD2)
        print("Math is about to start")
    if now == "12:29:00":#If now is 12:29:00 for CompSi
        webbrowser.open(PD3)
        print("Computer Science is about to start")
    if now == "13:39:00":#If now is 1:39:00 for Econ
        webbrowser.open(PD4)
        print("Econ is about to start")

    '''
    print(now)

    os.system('cls')
    '''
    #used for back testing the time in python shell
    
