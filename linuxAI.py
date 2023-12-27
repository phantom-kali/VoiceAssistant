import threading
import pyperclip
from category import *
from speaker import speak
from tasks import *
from SelectCopy import *
from wikipedia import *
from reminders import *
import command_exec
from datetime import datetime, timedelta
from dateutil import parser
from utils import *
from vOsk import *



def main():
    
    reminders = load_reminders()
    
    check_thread = threading.Thread(target=check_and_notify, args=(reminders,), daemon=True)
    check_thread.start()
    

    user_input = recognize_data()

    if user_input.lower() == "exit":
        print("Goodbye!")
        

    # Use the classifier to predict the category
    predicted_category = predict_category(user_input)

    def capture_reminder_input(prompt):
        speak(prompt)
        print(f"listening for {prompt.lower()}...")
        
        input_text = recognize_data()
        return input_text
    
    if predicted_category == "Youtube Audio": 
        selectCopy()
        pyautogui.click()
        speak("downloading audio file...")
        download_youtube_audio(url=pyperclip.paste())
        speak("download complete...")

    
    elif predicted_category == "Youtube Video":
        selectCopy()
        pyautogui.click()
        speak("downloading video file...")
        download_youtube_video(url=pyperclip.paste())
        speak("download complete...")
    
    elif predicted_category == "Wikipedia":
        wiki_query()   
    
    elif predicted_category == "Increase Volume":
        increase_volume()  
            
    elif predicted_category == "Decrease Volume":
        decrease_volume()
        
    elif predicted_category == "Increase Brightness":
        increase_brightness()
        
    elif predicted_category == "Decrease Brightness":
        decrease_brightness()
        
    elif predicted_category == "Screenshot":
        take_screenshot()
        
    elif predicted_category == "Photo":
        take_photo()                                 


    elif predicted_category == "Linux Commands":
        command_exec.recognize()
    
    
    elif predicted_category == "Add Reminder":
        speak("Sure, let's add a reminder.")
        
        # Capture reminder message
        speak("Please say the reminder message.")
        message = capture_reminder_input("reminder message")
        
        # Capture date and time string
        speak("Now, please say the date and time for the reminder.")
        date_time_str = capture_reminder_input("date and time")
        
        # Replace "today" and "tomorrow" in the date and time string
        date_time_str = date_time_str.replace("today", datetime.now().strftime("%Y-%m-%d"))
        tomorrow_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        date_time_str = date_time_str.replace("tomorrow", tomorrow_date)
        
        # Use dateutil.parser to parse the modified string
        date_time = parser.parse(date_time_str)
        
        # Add the reminder
        add_reminder(reminders, message, date_time)
        speak("Reminder added successfully.")
    
    elif predicted_category == "View Reminders":
        speak("Sure, let's view your reminders.")
        reminders_str = get_reminders_str(reminders)
        speak(reminders_str)

    elif predicted_category == "Delete Reminder":
        
        speak("Sure, let's delete a reminder.")
        get_reminders_str(reminders)

        index_text = capture_reminder_input("the index of the reminder to delete")
        index = int(index_text)
        
        delete_reminder(reminders, index)
        speak("Reminder deleted successfully.")

    else:
        speak("if you work harder i will have that function in the next update")                    
    
      
if __name__ == "__main__":
    main()
