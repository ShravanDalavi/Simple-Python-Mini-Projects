# Translator Application

This is a simple GUI-based Python application for translating text between different languages using the Google Translate API.

## Description

The application allows users to enter text in one language and translate it to another language using the `googletrans` library. The GUI is built with `tkinter`.

## Requirements

- Python 3.x
- `tkinter` library (usually included with Python installations)
- `googletrans` library

## Installation

1. Clone this repository to your local machine:
```bash
    git clone https://github.com/yourusername/translator-app.git
```

2. Navigate to the project directory:
```bash
    cd translator-app
```

3. Install the required Python modules:
```bash
    pip install googletrans==4.0.0-rc1
```

## Usage

1. Run the script:
```bash
    python Translate.py
```

2. Enter the text you want to translate in the "Text to Translate" field.

3. Select the source language from the "Source Language" dropdown menu.

4. Select the destination language from the "Destination Language" dropdown menu.

5. Click the "Translate" button to see the translated text in the "Translated Text" field.

## Example

```bash
$ python Translate.py
```