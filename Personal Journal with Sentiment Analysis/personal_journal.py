import json
from datetime import datetime
from textblob import TextBlob

class JournalEntry:
    def __init__(self, date, content):
        self.date = date
        self.content = content
        self.sentiment = self.analyze_sentiment(content)
    
    def analyze_sentiment(self, content):
        analysis = TextBlob(content)
        return analysis.sentiment.polarity  # Returns a value between -1 (negative) and 1 (positive)
    
    def __repr__(self):
        return f"{self.date} - Sentiment: {self.sentiment}\n{self.content}"

class PersonalJournal:
    def __init__(self):
        self.entries = []
    
    def add_entry(self, content):
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        entry = JournalEntry(date, content)
        self.entries.append(entry)
    
    def view_entries(self):
        for entry in self.entries:
            print(entry)
    
    def view_sentiment_summary(self):
        sentiments = [entry.sentiment for entry in self.entries]
        if sentiments:
            avg_sentiment = sum(sentiments) / len(sentiments)
            print(f"Average Sentiment: {avg_sentiment:.2f}")
        else:
            print("No entries to analyze.")
    
    def save_to_file(self, filename='journal_entries.json'):
        data = [entry.__dict__ for entry in self.entries]
        with open(filename, 'w') as f:
            json.dump(data, f)
        print("Journal entries saved to file.")
    
    def load_from_file(self, filename='journal_entries.json'):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.entries = [JournalEntry(**entry) for entry in data]
            print("Journal entries loaded from file.")
        except FileNotFoundError:
            print("File not found. Starting with an empty journal.")

def main():
    journal = PersonalJournal()
    journal.load_from_file()
    
    while True:
        print("\nPersonal Journal")
        print("1. Add Journal Entry")
        print("2. View All Entries")
        print("3. View Sentiment Summary")
        print("4. Save Entries to File")
        print("5. Load Entries from File")
        print("6. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            content = input("Enter your journal entry: ")
            journal.add_entry(content)
        elif choice == '2':
            journal.view_entries()
        elif choice == '3':
            journal.view_sentiment_summary()
        elif choice == '4':
            journal.save_to_file()
        elif choice == '5':
            journal.load_from_file()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
