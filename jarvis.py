import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set voice (female voice usually index 1)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Speak function
def talk(text):
    engine.say(text)
    engine.runAndWait()


# Take voice command
def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print("Command:", command)

    except Exception as e:
        # Optional: print(e) for debugging
        pass

    return command


# Run assistant
def run_jarvis():
    command = take_command()

    if command == "":
        return

    print("You said:", command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + current_time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        try:
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        except:
            talk("Sorry, I couldn't find information")

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'date' in command:
        talk('Sorry, I have a headache')

    elif 'are you single' in command:
        talk('I am in a relationship with WiFi')

    elif 'stop' in command or 'exit' in command:
        talk("Goodbye!")
        exit()

    else:
        talk('Please say the command again.')


# Run continuously
while True:
    run_jarvis()