import json
import speech_recognition as sr

class Appliance:
    def __init__(self, name):
        self.name = name
        self.state = "off"

    def turn_on(self):
        self.state = "on"

    def turn_off(self):
        self.state = "off"

    def __repr__(self):
        return f"{self.name} is {self.state}"

class HomeAutomation:
    def __init__(self):
        self.appliances = {
            "light": Appliance("light"),
            "fan": Appliance("fan"),
            "tv": Appliance("tv")
        }

    def control_appliance(self, command):
        words = command.split()
        if "turn" in words and "on" in words:
            appliance_name = words[-1]
            if appliance_name in self.appliances:
                self.appliances[appliance_name].turn_on()
            else:
                print("Appliance not found.")
        elif "turn" in words and "off" in words:
            appliance_name = words[-1]
            if appliance_name in self.appliances:
                self.appliances[appliance_name].turn_off()
            else:
                print("Appliance not found.")
        elif "status" in words:
            appliance_name = words[-1]
            if appliance_name in self.appliances:
                print(self.appliances[appliance_name])
            else:
                print("Appliance not found.")
        else:
            print("Command not recognized.")

    def save_to_file(self, filename='appliances.json'):
        data = {name: appliance.state for name, appliance in self.appliances.items()}
        with open(filename, 'w') as f:
            json.dump(data, f)
        print("Appliance states saved to file.")

    def load_from_file(self, filename='appliances.json'):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for name, state in data.items():
                    if name in self.appliances:
                        self.appliances[name].state = state
            print("Appliance states loaded from file.")
        except FileNotFoundError:
            print("File not found. Starting with default appliance states.")

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        return None

def main():
    home_automation = HomeAutomation()
    home_automation.load_from_file()

    while True:
        print("\nVoice-Controlled Home Automation")
        print("1. Issue Voice Command")
        print("2. Save Appliance States to File")
        print("3. Load Appliance States from File")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            command = recognize_speech()
            if command:
                home_automation.control_appliance(command)
        elif choice == '2':
            home_automation.save_to_file()
        elif choice == '3':
            home_automation.load_from_file()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
