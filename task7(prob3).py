chats=[]
users=[]

def register_user(user):
    users.append(user)


def send_message(message):
    chats.append(message)


def view_messages():
    for i in range(len(chats)):
        print(f"Chats:{chats[i]}")


def view_users():
    for i in range(len(users)):
        print(f"Users: {users[i]}")


def search_user(user):
    search_user(user)
    
    
def main():
    while True:
         print("1. Register user:")
         print("2. Send message:")
         print("3. View messages:")
         print("4. Search for user:")
         print("5. View users:")
         print("6. Exit")
         option=int(input("Enter an option:"))

         if option==1:
            user=input("Enter username:")
            register_user(user)
            print(f"user: {user} registered successfully!")


         elif option==2:
            message=input("Enter a message:")
            send_message(message)
            print(f"message: {message} sent successfully!")


         elif option==3:
            view_messages()



         elif option==4:
            user=input("Who are u searching for?")
            if user in users:
                print(f"user: {user} found successfully!")
            else:
                print(f"user: {user} not found!")


         elif option==5:
             view_users()


         elif option==6:
            break

         else:
            print("invalid option!")

main()

    



