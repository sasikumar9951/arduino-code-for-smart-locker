import serial
import speech_recognition as sr
import pyttsx3

# Initialize serial communication with Arduino
arduino = serial.Serial('COM5', 9600, timeout=1)  # Replace 'COM3' with your Arduino's port

# Predefined code word
CODE_WORD = "open"  # Set your desired code word

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('voice', 'english')  # Set voice

# Function to send commands to Arduino
def send_command(command):
    arduino.write((command + '\n').encode())
    response = arduino.readline().decode().strip()
    print(f"Arduino Response: {response}")
    engine.say(f"Arduino says {response}")
    engine.runAndWait()

# Function to recognize voice input
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your command...")
        engine.say("Listening for your command")
        engine.runAndWait()
        try:
            audio = recognizer.listen(source, timeout=5)  # Listen for 5 seconds
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I could not understand your voice.")
            engine.say("Sorry, I could not understand your voice.")
            engine.runAndWait()
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

# Main loop for handling commands
while True:
    # Listen for the initial command
    voice_command = recognize_speech()
    if voice_command in ["unlock", "lock"]:
        if voice_command == "unlock":
            # Ask for the code word
            engine.say("Please say the code word")
            engine.runAndWait()
            code_word_input = recognize_speech()  # Capture the code word in voice
            if code_word_input == CODE_WORD:
                send_command("UNLOCK")
            else:
                engine.say("Incorrect code word")
                engine.runAndWait()
                print("Incorrect code word!")
        elif voice_command == "lock":
            send_command("LOCK")
    else:
        engine.say("Invalid command. Please say unlock or lock.")
        engine.runAndWait()
        print("Invalid command. Please say unlock or lock.")




