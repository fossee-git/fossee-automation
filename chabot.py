from __future__ import annotations
import json
from difflib import get_close_matches


# Load data from a JSON file.
def loadData(filePath: str) -> dict:
    with open(filePath, 'r') as file:
        return json.load(file)


# Save data to a JSON file.
def saveData(filePath: str, data: dict):
    with open(filePath, 'w') as file:
        json.dump(data, file, indent=2)


# Find the closest match to the query from a list of questions.
def findClosestMatch(query: str, questions: list[str]) -> str | None:
    matches = get_close_matches(query, questions, n=1, cutoff=1.0)
    return matches[0] if matches else None


# Fetch the answer for the given query from the database.
def fetchAnswer(query: str, database: dict) -> str | None:
    for item in database["questions"]:
        if item["questions"].lower() == query:
            return item["answer"]
    return None


# Run the chatbot interface that interacts with the user.
def runChatbot():
    database = loadData('QnA_base.json')

    print("Hello! I'm here to help you with your questions. Type 'quit' to exit.")

    while True:
        userInput = input("Your question: ").lower()

        if userInput == "quit":
            print("Goodbye! Have a great day!")
            break

        closestMatch = findClosestMatch(userInput, [item["questions"].lower() for item in database["questions"]])

        if closestMatch:
            response = fetchAnswer(closestMatch, database)
            print(f"Bot says: {response}")
        else:
            print("Hmm, I don't have an answer for that. Can you teach me?")
            newResponse = input('Please provide the answer or type "skip" to skip: ').lower()

            if newResponse != "skip":
                database["questions"].append({"questions": userInput, "answer": newResponse})
                saveData('QnA_base.json', database)
                print("Great! I've learned something new.")

#Calling runChatbot()
runChatbot()

