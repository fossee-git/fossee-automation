import re
import tkinter as tk
from tkinter import scrolledtext
from nltk.corpus import words
import nltk
import language_tool_python


try:
    nltk.download('words')
except Exception as e:
    print(f"NLTK Download Error: {e}")

try:
    tool = language_tool_python.LanguageTool('en-US')
except language_tool_python.ServerException as e:
    print(f"LanguageTool Initialization Error: {e}")


def checkSpelling(text):
    wordList = set(words.words())
    misspelled = []
    for word in re.findall(r'\b\w+\b', text):
        if word.lower() not in wordList:
            misspelled.append(word)
    return misspelled

def checkGrammar(text):
    matches = tool.check(text)
    return matches

def checkText():
    text = textArea.get("1.0", tk.END)
    spellingErrors = checkSpelling(text)
    grammarErrors = checkGrammar(text)

    result = "Spelling Errors:\n"
    if spellingErrors:
        result += ", ".join(spellingErrors)
    else:
        result += "None"

    result += "\n\nGrammar Errors:\n"
    if grammarErrors:
        for match in grammarErrors:
            result += f"{match.context} -> {match.message}\n"
    else:
        result += "None"

    resultArea.config(state=tk.NORMAL)
    resultArea.delete("1.0", tk.END)
    resultArea.insert(tk.END, result)
    resultArea.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Spelling and Grammar Checker")

textArea = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
textArea.pack(pady=10)

checkButton = tk.Button(root, text="Check", command=checkText)
checkButton.pack(pady=5)

resultArea = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15, state=tk.DISABLED)
resultArea.pack(pady=10)

root.mainloop()
