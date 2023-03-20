#Author: spasemax0
# simple customizable AI base script

import json
import requests
import speech_recognition as sr
import pyttsx3
import pyaudio

# Initialize speech recognition engine
r = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Define a function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: ", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""

# Define the main function
def main():
    while True:
        # Ask the user for input
        speak("How can I help you?")
        text = recognize_speech()

        # Process the input
        def process_text(input_text):
            if "search for" in input_text:
                search_term = input_text.split("search for")[-1].strip()
                search_url = f"https://duckduckgo.com/html/?q={search_term}"
                results = get_search_results(search_url)
                if results:
                    speak(f"Here are the top search results for {search_term}")
                    for result in results:
                        speak(result)
                else:
                    speak("Sorry, I could not find any results for that search query.")
            elif "google" in input_text:
                search_term = input_text.split("google")[-1].strip()
                search_url = f"https://www.google.com/search?q={search_term}"
                results = get_search_results(search_url)
                if results:
                    speak(f"Here are the top search results for {search_term}")
                    for result in results:
                        speak(result)
                else:
                    speak("Sorry, I could not find any results for that search query.")





        # Add more functionality as needed

# Call the main function
if __name__ == "__main__":
    main()
