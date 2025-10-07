# ⏱️ Countdown Timer

import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  # \r replaces the line dynamically
        time.sleep(1)
        seconds -= 1
    print("⏰ Time's up!            ")  # extra spaces clear previous text

def main():
    print("⏱️ Welcome to Countdown Timer ⏱️")
    try:
        total_seconds = int(input("Enter time in seconds: "))
        countdown(total_seconds)
    except ValueError:
        print("❌ Invalid input! Please enter an integer value.")

if __name__ == "__main__":
    main()
