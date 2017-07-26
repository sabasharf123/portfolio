class User:

    def __init__(self, name):
        self.name = name
        self.birthdate = ""
        self.age = ""
        self.current location = ""


    def set_birthdate(self, birthdate):  #these functions can change your values stored in the init function
        self.birthdate = birthdate

    def set_age(self, age):
        self.age = age

    def set_current_location(self, current_location):
        self.current_location = current_location



def main():

        ConnectMe = User("user")

        ConnectMe.set_age
        ConnectMe.set_birthdate
        ConnectMe.set_current_location
        
        new_users_name = input("Create a username")
        new_user = User(new_users_name)


main()
