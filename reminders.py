import pickle
import os
import datetime
import time
from plyer import notification

REMINDERS_FILE = "reminders.pkl"

class Reminder:
    def __init__(self, message, date_time):
        self.message = message
        self.date_time = date_time

def save_reminders(reminders):
    with open(REMINDERS_FILE, "wb") as file:
        pickle.dump(reminders, file)

def load_reminders():
    if os.path.exists(REMINDERS_FILE):
        with open(REMINDERS_FILE, "rb") as file:
            return pickle.load(file)
    else:
        return []

def send_notification(message):
    notification.notify(
        title="Reminder",
        message=message,
        app_name="Reminder App",
    )

def add_reminder(reminders, message, date_time):
    reminder = Reminder(message, date_time)
    reminders.append(reminder)
    print(f"Reminder added: {reminder.message} at {reminder.date_time}")
    save_reminders(reminders)

def delete_reminder(reminders, index):
    if 1 <= index <= len(reminders):
        deleted_reminder = reminders.pop(index - 1)
        print(f"Deleted reminder: {deleted_reminder.message} at {deleted_reminder.date_time}")
        save_reminders(reminders)
    else:
        print("Invalid index. No reminder deleted.")

def get_reminders_str(reminders):
    if not reminders:
        return "You don't have any reminders."
    else:
        reminders_str = "Here are your current reminders:\n"
        for i, reminder in enumerate(reminders, start=1):
            reminders_str += f"Reminder {i}: {reminder.message} scheduled for {reminder.date_time}\n"
        return reminders_str

def check_and_notify(reminders):
    while True:
        current_time = datetime.datetime.now()
        due_reminders = [reminder for reminder in reminders if reminder.date_time <= current_time]

        for reminder in due_reminders:
            print(f"Reminder: {reminder.message} (Scheduled for {reminder.date_time})")
            send_notification(reminder.message)
            reminders.remove(reminder)

        if due_reminders:
            save_reminders(reminders)

        # Sleep for a short duration before checking again
        time.sleep(10)
