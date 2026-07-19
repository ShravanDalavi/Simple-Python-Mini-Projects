
import os
import webbrowser
from datetime import datetime

import pyperclip
import pyshorteners
import validators
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Constants
HISTORY_FILE = "history.txt"
LINE = "=" * 60


def banner():
    print(Fore.CYAN + LINE)
    print(Fore.CYAN + " " * 20 + "URL SHORTENER")
    print(Fore.CYAN + LINE)


def save_history(original: str, short: str) -> None:
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(f"{LINE}\n")
        file.write(
            f"Date      : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        file.write(f"Original  : {original}\n")
        file.write(f"Short URL : {short}\n")
        file.write(f"{LINE}\n\n")


def shorten_url() -> None:
    print(Fore.YELLOW + "\nEnter the URL to shorten.\n")

    url = input("Long URL : ").strip()

    if not validators.url(url):
        print(Fore.RED + "\n✖ Invalid URL.\n")
        return

    try:
        shortener = pyshorteners.Shortener()

        short_url = shortener.tinyurl.short(url)

        print(Fore.GREEN + "\n✔ URL Shortened Successfully\n")

        print(Fore.CYAN + "Original URL")
        print(url)

        print("\n" + Fore.CYAN + "Short URL")
        print(short_url)

        save_history(url, short_url)

        pyperclip.copy(short_url)
        print(Fore.GREEN + "\n✔ Short URL copied to clipboard.")

        choice = input(
            "\nOpen the shortened URL in browser? (y/n): "
        ).lower()

        if choice == "y":
            webbrowser.open(short_url)

    except Exception as error:
        print(Fore.RED + "\n✖ Error")
        print(error)


def view_history() -> None:

    print()

    if not os.path.exists(HISTORY_FILE):
        print(Fore.YELLOW + "No history found.")
        return

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        history = file.read()

    if history.strip():
        print(history)
    else:
        print(Fore.YELLOW + "History is empty.")


def clear_history() -> None:

    with open(HISTORY_FILE, "w", encoding="utf-8"):
        pass

    print(Fore.GREEN + "\n✔ History cleared successfully.")


def menu() -> None:

    while True:

        banner()

        print("1. Shorten URL")
        print("2. View History")
        print("3. Clear History")
        print("4. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            shorten_url()

        elif choice == "2":
            view_history()

        elif choice == "3":
            clear_history()

        elif choice == "4":
            print(Fore.GREEN + "\nThank you for using URL Shortener.")
            break

        else:
            print(Fore.RED + "\nInvalid choice.")

        input(Fore.BLUE + "\nPress Enter to continue...")


if __name__ == "__main__":
    menu()