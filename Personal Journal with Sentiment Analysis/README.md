# Personal Journal with Sentiment Analysis

## Description

The Personal Journal with Sentiment Analysis project allows users to maintain a daily journal, analyze the sentiment of their entries, and view sentiment trends over time. The application enables users to add journal entries, view all entries, perform sentiment analysis using TextBlob, and save/load entries from a file.

## Features

- Add journal entries with date and content.
- View all journal entries.
- Perform sentiment analysis on entries.
- View sentiment summary over time.
- Save journal entries to a file.
- Load journal entries from a file.

## Required Modules
- `textblob`
- `nltk`
- `json`
- `datetime`

## How to Install Required Modules
To install the required modules, use the following steps:

1. Open Command Prompt (Windows) or Terminal (macOS/Linux).
2. Install `textblob` module by running:
    ```sh
    pip install textblob
    ```
3. Open Python interpreter to download NLTK corpora:
    ```sh
    python
    ```
4. In the Python interpreter, run the following commands:
    ```python
    import nltk
    nltk.download('punkt')
    exit()
    ```

## ▶️ How to Run the Script
1. Clone the Repository:
   ```
   git clone https://github.com/ShravanDalavi/Simple-Python-Mini-Projects.git
   ```
2. Navigate to Directory:
   ```bash 
          cd Simple-Python-Mini-Projects/Personal\ Journal\ with\ Sentiment\ Analysis
   ```
3. Run the Script:
   ```bash 
      python personal_journal.py
   ```
   
## Example Usage
```sh 
Personal Journal

Add Journal Entry
View All Entries
View Sentiment Summary
Save Entries to File
Load Entries from File
Exit
Choose an option: 1
Enter your journal entry: Had a great day at the park!
Personal Journal

Add Journal Entry
View All Entries
View Sentiment Summary
Save Entries to File
Load Entries from File
Exit
Choose an option: 2
2024-08-07 14:23:45 - Sentiment: 0.8
Had a great day at the park!

```
