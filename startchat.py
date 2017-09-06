#startchat() function definition
def startchat(name,age,rating):
    showmenu = True         #to display menu
    while showmenu:
        menuchoices = "What do you want to do?\n1) Add a status update\n2) Close the application\ny"
        result = int(raw_input(menuchoices))

        #validating the menuchoice
        if result == 1:
            print "You choose to update the status "
        elif result == 2:
            showmenu = False
