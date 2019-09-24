

#********************************************************************************
#           This function ask player for replay
#********************************************************************************

def replay():

        ask_replay = input("Do you want to play again ? ").upper()
        if ask_replay == "YES":
            return True
        else:
            return False
    
