'''
Python game project made with freecodecamp.org and Tech with Tim

'''

import random #import random module


#random game names for the user
random_game_names =['Jimmy', 'Levi','Princess James','Lady Bailey','Eren','Lord uncool', 'Prince Fluffy', 'Princess Jigsaw']

banned_game_names =['Slender man', 'gingerbread man', 'name',69, 'Mr T']


# game classes for user to choose from
character_class_list ={
"A":"Archer",
"C":"Caster",
"L":"Lancer",
"S":"Saber",
"R":"Rider",
"AA":"Assassin",
"B":"Beserker",
"W":"Wizard",
"X":"Random character"
    }

def game_name_change():
    '''Game name changer function'''
    user_choice=str(input("Would you like us to give you a name?: ")).lower()
    if user_choice == "yes":
        random_name = random.randint(0,7) #assign random a range
        game_name_pick= random_game_names[random_name] #access the list we have created
        print('Your new name is', game_name_pick, '\n')
        game_age_checker(game_name_pick)#function call
        
    elif user_choice =="no":
        user_new_name=str(input('Enter your new name, we promise not to judge: '))
        name_checker =isinstance(user_new_name, str)
        if name_checker == True:
            game_age_checker(user_new_name)
        
   # elif user_choice_2:
    #    game_age_checker()

    else:
        print('Sorry I dont understand')
        game_name_change()





def quiz_end():
    #function for ending the game
    print("\n This is the end \n Beautiful friend \n This is the end \n My only friend, the end")



def game_age_checker(name):
    '''game age checker function'''
    user_age=str(input('Are you over 18 years old to play the game? ')).upper()
    if user_age == 'YES':
        user_age_input_2 = int(input('Please enter your age: '))

        if user_age_input_2 >= 18:
            print('Even if you lied we arent responible happy gaming')
            quiz_start(name)
        
        elif user_age_input_2 < 18:
            print('Sorry', name, ' you are too young to play this game')
            

        else:
            print('Sorry i dont understand what you have said')
            #while True:
            game_age_checker(name)
            
        
    elif user_age =="NO":
        print('Sorry', name, ' you are too young to play this game')

    else:
        print('Sorry', name,'I dont understand what you have typed')
        #while True:
        game_age_checker(name)
        

    
    

def quiz_start(name):
    health =10
    #function for the quiz game to begin
    print('You will have 10 health')
    print("Before your journey", name ,'can continue select your type class by entering the class letter')
    print (character_class_list)
    #print('Archer-(A)')
    
    user_class_type=input('Choose your adventure Class from the list above with the corresponding letter: ')
    
    





def welcome_screen():
    print ("Welcome to the game!") #print statement
    name = input("What is your name? ") #input statement
    print ('Are you sure', name ,' is your name? ') #prints the name in the sentenace
    user_name_confirm=str(input())
    
        
    if user_name_confirm =="yes" or user_name_confirm=="Yes":
        for bgn in banned_game_names:
            if bgn == name:
                print('Sorry you cant use that name \n')
                welcome_screen()                
            else:
                print("Lets continue ",name)
                game_age_checker(name)

    elif user_name_confirm =="No" or user_name_confirm=="no":
        print("Would you like to change your name? ")
        user_choice_2 =str(input())
        if user_choice_2 == 'yes' or user_choice_2 == 'Yes':
            game_name_change()
        elif user_choice_2 == 'no' or user_choice_2 == 'No':
            game_age_checker(name)
        else:
            print('Sorry I dont understand')
            welcome_screen()

    else:
        print('Sorry I dont understand')
        welcome_screen()
        


#runs the first function we have made above
if __name__=='__main__':
    welcome_screen()
    
