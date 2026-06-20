print("===== SIMPLE CHAT APPLICATION =====")

chat_history = []

while True:

    user1 = input("User 1: ")

    if user1.lower() == "exit":
        break

    chat_history.append("User 1: " + user1)

    user2 = input("User 2: ")

    if user2.lower() == "exit":
        break

    chat_history.append("User 2: " + user2)

print("\n===== CHAT HISTORY =====")

for message in chat_history:
    print(message)


