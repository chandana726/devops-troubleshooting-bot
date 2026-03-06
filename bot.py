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

    found = False

    for issue in knowledge:
        if issue in user_input:
            print("Bot:", knowledge[issue])
            found = True
            break

    if not found:
        print("Bot: Sorry, I don't know that issue yet.")