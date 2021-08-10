'''
Python game project made with freecodecamp.org and Tech with Tim

'''
print ("Welcome to the game!") #print statement
name = str(input("What is your name? ")) #input statement
print ('Are you sure', name ,' is your name?') #prints the name in the sentenace
user_name_confirm=input()
#confirmation_screen(user_name_confirm)

#def confirmation_screen(user_name_confirm):
    
if user_name_confirm =="yes" or "Yes":
    print("Lets continue ",name)
    game_age_checker()

elif user_name_confirm =="No" or "no":
    print("Would you like to change your name? ")
    user_choice_2=input()

    if user_choice_2 =="yes":
        user_new_name=str(input('Enter your new name, we promise not to judge: '))
        game_age_checker()
        
    elif user_choice_2:
        game_age_checker()

else:
    print('Sorry I dont understand')
    #welcome_screen()


def welcome_screen():
    print ("Welcome to the game!") #print statement
    name = str(input("What is your name? ")) #input statement
    print ('Are you sure', name ,' is your name?') #prints the name in the sentenace
    user_name_confirm=input()
    #confirmation_screen(user_name_confirm)
        



def game_age_checker():
    '''game age checker function'''
    user_age=str(input('Are you over 18 years old to play the game? '))

    if user_age > 18:
        print('Even if you lied we arent responible happy gaming')
        quiz_start()

    else:
        quiz_end()



def quiz_start():
    #function for the quiz game to begin
   

    
    print("Before your journey", name ,'can continue select your type class')
    print('Archer-')

def quiz_end():
    print("This is the end")

#def
#function for the user to change their name
