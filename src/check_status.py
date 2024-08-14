from utils.text_utils import clean_html
from playsound import playsound
import re

def is_over_paused(minutes):
    minutes, _ = minutes.split(":")
    return int(minutes)

def extract_response(cleaned_response):
    results = []

    for res in cleaned_response:
        final = clean_html(res)

        if final:
            final = final.split("|")
                
            user = final[2].strip()
            status = final[4].strip()
            minutes = final[5].strip()

            results.append((user, status, minutes))
        
    return results
    

def show_status(cleaned_response, with_sound):
    for user, status, minutes in extract_response(cleaned_response):
        user = re.sub("\+", "", user)

        status = re.sub("\s[A-Z]", "", status)
        remarks = "PAUSE SO LONG" if status == "PAUSED" and is_over_paused(minutes) > 1 else "IS DEAD CALL" if status == "DEAD" else "DISPO SO LONG" if status == "DISPO" and is_over_paused(minutes) > 3 else ""
        remarks = f"\033[1;31;27m {remarks} \033[0;0;0m"
        info = f"{user} \t\t|\t\t {status}  \t\t|\t\t {minutes} \t\t|\t\t {remarks}"

        print(info)
                
        if status == "PAUSED" and is_over_paused(minutes) > 10 or status == "DISPO" and is_over_paused(minutes) > 10 or status == "DEAD" and is_over_paused(minutes) > 10:
            if with_sound:
                playsound("./media/uwu.mp3")
            