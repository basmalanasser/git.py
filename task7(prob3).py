chats = {}
username = input
def user(username):
    if username in chats :
        return f"User '{username}' exists"
    else:
        user.append(username)
        return f"User '{username}' registered successfully."
def send_message(sender, receivers ,message):
    return "Message sent successfully."
    message = {
        "sender": sender,
        "receiver": receiver,
        "message": message_text
    }
    chat_system[sender].append(message)
    chat_system[receiver].append(message)
    return f"Message sent from '{sender}' to '{receiver}'."
def view_messages(username):
    for i in range(len(chats)):
        print(f"Chats:{chats[i]}")
def main():
    while True:
         print("1. Register user:")
         print("2. Send message:")
         print("3. View messages:")
         print("4. Exit")
         option=int(input("Enter an option:"))
         if option==1:
            user=input("Enter username:")
            print(f"user: {username} registered successfully!")
         elif option==2:
            message=input("Enter a message:")
            send_message :{sender, receivers ,message}
            print(f"message: {message} sent successfully!")
         elif option==3:
            view = input ("Enter your message :")
            view_messages :{username}
            print(f"view: {view} !")

         elif option==4:
            break
         else:
            print("invalid option!")
main()



