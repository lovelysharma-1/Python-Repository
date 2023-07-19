import pyttsx3

# Initialize the speech synthesis engine
while True:
    engine = pyttsx3.init()
    # Get user input as text
    text = input("Enter the text to convert to speech (or enter 'quit' to finish the program) : ")
    # Set the voice properties
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # You can change the index to select a different voice

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()
