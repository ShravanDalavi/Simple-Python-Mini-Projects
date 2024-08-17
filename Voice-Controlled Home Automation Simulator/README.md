## Voice-Controlled Home Automation Simulator

## Description:
The Voice-Controlled Home Automation Simulator project simulates a voice-controlled system that can turn on or off virtual appliances such as lights, fans, and TVs. Users can issue voice commands to control the appliances, check their status, and save/load the states of the appliances.

## Features:
1. Control virtual appliances (e.g., lights, fans, TV) using voice commands.
2. Turn appliances on or off.
3. Query the status of appliances.
4. Save and load appliance states to/from a file.

## Required Modules:
- `json`
- `speech_recognition`

## How to Install Required Modules:
To install the required modules, use the following steps:

1. Open Command Prompt (Windows) or Terminal (macOS/Linux).
2. Install the speech_recognition module by running:
```sh
pip install SpeechRecognition
```
## How to Run the Script:
1. Navigate to the project directory in Command Prompt (Windows) or Terminal (macOS/Linux).
2. Run the script using Python:
```sh
python home_automation.py
```
## Example Usage:
```vbnet
Voice-Controlled Home Automation
1. Issue Voice Command
2. Save Appliance States to File
3. Load Appliance States from File
4. Exit
Choose an option: 1
Listening...
You said: turn on light
```
## Acknowledgments:
- This project uses the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library for voice command recognition.