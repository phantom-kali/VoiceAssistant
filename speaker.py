import os

def speak(text_to_speak):
    # Escape single quotes in the text
    text_to_speak = text_to_speak.replace("'", r"'\''")

    # Festival command
    festival_command = f"festival -b '(voice_cmu_us_slt_arctic_hts)' '(SayText \"{text_to_speak}\")'"
    
    # Execute the Festival command using os.system
    os.system(festival_command)



