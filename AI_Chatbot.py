import nltk
import spacy

# Download necessary NLTK data
nltk.download('punk')
from nltk.tokenize import word_tokenize

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

def tokenize(text):
    # Using NLTK
    tokens_nltk = word_tokenize(text)
    
    # Using spaCy
    doc = nlp(text)
    tokens_spacy = [token.text for token in doc]
    
    return tokens_nltk, tokens_spacy

def respond(text):
    tokens_nltk, tokens_spacy = tokenize(text)
    
    # Simple rule-based responses
    if 'hello' in tokens_nltk:
        return "Hi there!"
    elif 'bye' in tokens_spacy:
        return "Goodbye!"
    else:
        return "I'm not sure how to respond to that."

def main():
    print("Welcome to the chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        response = respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
