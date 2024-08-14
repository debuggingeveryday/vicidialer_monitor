# src/utils/text_utils.py
from bs4 import BeautifulSoup
import re
import pyautogui

def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")
    for data in soup(['style', 'script']):
        data.decompose()
    return ' '.join(soup.stripped_strings)

def clean_text(response):
    start = r"<\/a> \| CALLS \| HOLD \| IN-GROUP <\/tr>\n\+----------------\+------------------------\+-----------\+----------\+---------\+------------\+-------\+------\+-------------------<\/tr>\n\|"
    end = r" \|\n\+----------------\+------------------------\+-----------\+----------\+---------\+------------\+-------\+------\+-------------------<\/tr>"
    
    response = re.findall(start+"[\w\W]+"+end, response)
    try:
        response = response[0].replace("</a> | CALLS | HOLD | IN-GROUP </tr>", "")
        response = response.replace("+----------------+------------------------+-----------+----------+---------+------------+-------+------+-------------------</tr>", "")
        response = response.split("\n")
    except:
        print("No available calls")
        # pyautogui.alert('No available calls', "Error 1")  # always returns "OK"

    return response