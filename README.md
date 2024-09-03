# Automated Quiz Feedback Sender

This script automatically sends personalized feedback messages to students via WhatsApp based on their quiz performance. Follow the steps below to set up and run the script.

## Prerequisites

1. **Python**: Make sure Python is installed on your machine. You can download it from [here](https://www.python.org/downloads/).
2. **Libraries**: Install the necessary Python libraries by running:
   ```bash
   pip install pandas pyautogui openpyxl

## Web Browser

-The script uses your default web browser to open WhatsApp Web.

-**Make sure your whatsapp is logged in on this browser**

## Excel Sheet Format

Note: You are free to adjust the code based on the excel sheet column names and data whether it's marks of Boolean values

**The excel sheet for the code provided:**

<img width="873" alt="Screenshot 2024-09-03 at 4 17 39 PM" src="https://github.com/user-attachments/assets/ce6f127f-a822-4ebb-bcce-a5e66717deb2">

## Notes

- **WhatsApp Web**: You need to have WhatsApp Web logged in to your account for the script to work. Make sure to scan the QR code from your phone to log in.
- **Message Format**: The script uses the scores from the Excel file to determine the appropriate feedback for each student.
- **Delays**: The script includes delays to ensure the web pages load properly and messages are sent. Adjust these delays as necessary depending on your internet speed.

## Disclaimer

This script automates the process of sending messages via WhatsApp Web. **Please use this tool responsibly**. Overuse or misuse of automated messaging can potentially violate WhatsApp's [Terms of Service](https://www.whatsapp.com/legal/terms-of-service/) and [Privacy Policy](https://www.whatsapp.com/legal/privacy-policy/). Make sure to obtain consent from recipients before sending messages and avoid sending unsolicited messages. Automated messaging without proper consent can be considered spam and may result in your WhatsApp account being banned.


