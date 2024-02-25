# Asian_clock
This project aims to develop a Talking Clock application in Python that provides users with the current time in a 12-hour format and offers voice output. The Talking Clock will support multiple languages, including Singapore(English), Japanese, Chinese, Korean, and Thai, providing a user-friendly interface for users to interact with. In addition, the user can set the alarm based on the local time that the user chooses. The project prioritizes data privacy and adheres to ethical considerations related to user consent.
################
1. Introduction
Welcome to the Talking Clock application! This application allows you to hear the current time spoken in various languages based on their time zones. Simply click on a country's button to hear the current time in that country's language, and use the alarm function to set reminders.

2. System Requirements
- Runtime environment (Python 3.9+) if not already installed. - Enough CPU to run the code
- Speakers or headphones for audio output
- Use pip to install Python libraries:
  -Tkinter toolkit for the GUI
  -gTTS (Google Text-to-Speech) library
  -pydub, librosa, sound file, audio_effects package for audio processing etc please our requirements.txt on our github.

3. Accessing the Talking Clock Application
To access the Talking Clock application, follow these steps:
  1. Download zip file from our git-hup
  2. Open the file in your python development environment (We recommend Pycharm). 3. Check requirements.txt and download libraries and packages.
  4. In case of audio effects package
  5. Run main.py
     
4. Main Interface
Upon running our program, you will see the main interface, which includes the following components:
  - Current Singapore time
  - Country buttons on the map
  - Scrollbars for changing speed rate, volume level - Combobox for changing background image
  - Alarm button

5. How to Use the Talking Clock
To use the Talking Clock application:
  1. Simply click on one of the country buttons to hear the current time in that country's language. The time will be announced aloud and displayed on the screen.
  2. If you click button over 57s, clock will speak one minute added from the time the button was pressed by reflecting program delay
  3. For Chinese you can choose between audio synthesized by gtts (Chinese synthesis) or audio recorded by a human (Chinese natural).
  4. Our background automatically changed based on current time. Background has two types; light/dark version and you can choose the mode you want using combobox.
  5. You can change the acoustic features through the speed rate and volume level scroll bars located at the bottom left.
  6. You can set the alarm using the ‘set alarm’ button! There is a detailed description at 6.

6. Alarm Function
- To set an alarm reminder, click the "Set Alarm" button.
- A dialog box will appear, allowing you to enter the time for your reminder and a brief message.
- After setting the alarm, you will receive an audio and visual notification at the specified time.
- Alarm will be set according to the time zone you select.
- Current Singapore time
- Country buttons on the map
- Scrollbars for changing speed rate, volume level - Combobox for changing background image
- Alarm button

7. Troubleshooting
If you encounter any issues while using the Talking Clock application, please ensure that you have a enough CPU and memory to run our codes. Also make sure that your libraries are up-to-date. Sometimes, depending on your computer, an error may occur where pygame is not initialized. This is not a glitch in the code, and the audio will play normally when you start the program again. If the problem persists, you may contact our support team for assistance (see Section 8).

8. Contact Support
If you have questions, encounter technical issues, or need assistance, please contact via deng134340@gmail.com. We are here to help you with any concerns or inquiries.

Enjoy using the Talking Clock application to hear the current time and set alarms for reminders. We hope it enhances your timekeeping and scheduling experience!
