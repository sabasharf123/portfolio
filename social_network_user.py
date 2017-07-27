class User:
    def __init__(self, name):
        self.name = name
        self.birthdate = ""
        self.age = ""
        self.currentLocation = ""

    def set_age(self, age):     #these functions can change your values stored in the init function
        self.age = age

    def set_birthdate(self, birthdate):
        self.birthdate = birthdate

    def set_current_location(self, current_location):
        self.current_location = current_location

    def set_education(self, education):
        self.education = education

    def set_number(self, number):
        self.number = number

    def set_email(self, email):
        self.email = email

    def add_connections(self, connections):
        self.connections.append(connections)



def main():
    new_users_name = input("Create a name ") #input for username
    NewUser = User(new_users_name)  #creating the user

    new_users_birthdate = input("When is you birthday ") #input for birthday
    NewUser.set_birthdate(new_users_birthdate) #building off the user

    new_users_age = input("What is your age? ") #input for age
    NewUser.set_age(new_users_age)

    new_users_location = input("Where do you currently live? ") #input for current location
    NewUser.set_current_location(new_users_location)

    new_users_education = input("What school/university do you attend? ") #input for school
    NewUser.set_education(new_users_education)

    new_users_phoneNumber = input("What is your phone number? ") #input for phone number
    NewUser.set_number(new_users_phoneNumber)

    new_users_email = input("What is your email? ") #input for email
    NewUser.set_email(new_users_email)

    print("You have successfully created your biography. Here is a review of what you added. ")
    print("Hello! My name is " + new_users_name + ". I am currently" + new_users_age + " years old. My birthday is on " + new_users_birthdate + " I go to schoool at " + new_users_education + "You can contact me by calling me at " + new_users_phoneNumber + "  or emailing me at " + new_users_email + ".")


    while True:  #if it's true, then it will keep running the program

        #ask for what the user wants to do
        user_action = input("What do you want to do? Create a user to connect with (a), list connections (l), \n \
        see other biographies (b), or quit (q): ")

        if user_action == 'q':
            print("Sorry to see you go!")
            exit()

         #elif = else if. So, if the user action was NOT q, now check if it's u
        elif user_action == 'a':
            connections = input("Who would you like to add?")

            new_users_name = input("Create a name ") #input for username
            NewUser = User(new_users_name)  #creating the user

            print("You have successfully connected with this person")

        elif user_action == 'l' :
            print("Here are your connections!")
            print(new_users_name)

        #elif user_action == 'b':
            #move_right_from(room_number)


        #else here means, if the user action was ANYTHING else
        #besides q, u, d, r, or l.
        else:
            print("Um, I don't know what that means. Please ask again.")


main()
