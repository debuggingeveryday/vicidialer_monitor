import time
from utils.web_utils import fetch_data
from utils.text_utils import clean_text
from config import options
from check_status import show_status
import base64
import os

LINK="https://faj.keizarnetworks.com/vicidial/AST_timeonVDADall.php"
CREDENTIAL="faj:DjyfzN84v7A2R9ArV9FZV"

def option():
    choose=input("With sound?: ")
    if choose == "1":
        return True
    else:
        return False

def convertBase64(credential):
    credential_string = credential
    credential_string_bytes = credential_string.encode("ascii") 
    
    base64_bytes = base64.b64encode(credential_string_bytes) 
    base64_string = base64_bytes.decode("ascii") 

    return base64_string

def main():

    with_sound=option()

    while True:
        print("--------------------------------------------------------------------------------------------------------------")
        response = fetch_data(LINK, headers={'Authorization': f"Basic {convertBase64(CREDENTIAL)}"})
        cleaned_response = clean_text(response)
        show_status(cleaned_response, with_sound)
        
        print("--------------------------------------------------------------------------------------------------------------")
        time.sleep(60)

if __name__ == "__main__":
    main()
