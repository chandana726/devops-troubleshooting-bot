import json

print("DevOps Troubleshooting Bot")
print("Type 'help' to see supported issues")
print("Type 'exit' to quit\n")

with open("knowledge.json", "r") as file:
    knowledge = json.load(file)

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "exit":
        print("Bot: Goodbye!")
        break

    if user_input == "help":
        print("Bot: I can help with these issues:")
        for issue in knowledge:
            print("-", issue)
        continue

    found = False

    for issue, solution in knowledge.items():
        if issue in user_input:
            print("Bot:", solution)
            found = True
            break

    if not found:
        print("Bot: Sorry, I don't know that issue yet.")