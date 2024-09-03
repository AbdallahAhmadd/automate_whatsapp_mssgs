import time
import pandas as pd
import webbrowser
import urllib.parse  # Import urllib for URL encoding
import pyautogui

# Load the CSV file
file_path = '2D Arrays Quiz Data.xlsx'
df = pd.read_excel(file_path)

#Custom Message You can customize it as you wish
Arrays_Mssg = ("You have an issue in *2D Array Topic* you will need to do the following:\n"
               "-*Watch 2D arrays Parts 1,2,3,4 recordings*\n"
               "-*Solve 2D Arrays Questions from the pseudocode translator*\n\n")

Code_Errors = ("You have an issue in *Code Errors* you will need to do the following:\n"
               "-*Solve Questions 1,2,3,4,5,6,7,8 in the classified starting from page 257*\n\n")

Functions = ("You have an issue in *Functions and procedures Topic* you will need to do the following:\n"
             "-*Watch Functions and procedures Parts 1,2 videos*\n"
             "-*Solve functions & procedures Questions from the pseudocode translator*\n\n")

Digital = ("You have an issue in *Digital logic* you will need to do the following:\n"
           "-*Solve Questions 11,12,13,14,15,16,17 in the CLassified*")

good_message = ("Excellent Performance, however *you need to check your correction comments and mistakes*")

# Iterate over each row and send a message
for index, row in df.iterrows():
    flag = False

    #Add your column name here
    phone_number = row['Phone Number']
    marks = int(row['Total /40'])
    arrays = row['Q1+Q2 2D Arrays /19']
    code_errors = row['Q3 Code Errors /4']
    functions_and_proc = row['Q4+Q5 Fns&Proc /9']
    digital_logic = row['Q6 Digital Logic /8']

    #welcome starting message
    message = f"Hello! You scored {marks} out of 40 in the last Practical Quiz.\n"

    #threshholds based on your excel sheet can be TRUE or FALSE too
    if arrays < 13:
        message += Arrays_Mssg
        flag = True
    if code_errors < 2:
        message += Code_Errors
        flag = True
    if functions_and_proc < 5:
        message += Functions
        flag = True
    if digital_logic < 5:
        message += Digital
        flag = True
    if not flag:
        message += good_message

    # URL encode the message
    encoded_message = urllib.parse.quote(message)

    print(message)
    try:
        # Open WhatsApp Web chat
        url = f"https://web.whatsapp.com/send?phone={phone_number}&text={encoded_message}"
        webbrowser.open(url)
        time.sleep(10)  # Wait for the page to load
        pyautogui.hotkey('command', 'enter')  # 'command' for Mac, use 'ctrl' for Windows
        time.sleep(2)  # Wait for the message to be sent
    except Exception as e:
        print(f"Failed to send message to {phone_number}: {e}")
