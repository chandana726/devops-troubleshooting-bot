import json

print("DevOps Troubleshooting Bot")
print("Type 'exit' to quit\n")

# Load knowledge base
with open("knowledge.json", "r") as file:
    knowledge = json.load(file)

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Bot: Goodbye!")
        break

    if user_input in knowledge:
        print("Bot:", knowledge[user_input])
    else:
        print("Bot: Sorry, I don't know that issue yet.")