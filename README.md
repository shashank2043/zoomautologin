# Class Link Automation

This Python script automates the process of opening Zoom links for your classes at scheduled times.

## How to Use

1. **Install Required Libraries**

   Before running the script, you'll need to install the necessary Python libraries. Open your terminal or command prompt and run the following commands:

   ```bash
   pip install schedule
   pip install pywhatkit
2. **Update the Script**

Replace the placeholders in the script with your actual Zoom links. For example:

python
open_link('Zoom link')  # Replace 'Zoom link' with your actual Zoom link
Update the links and times according to your class schedule.
Run the Script

Execute the script by running the following command in your terminal or command prompt:

bash
Copy code
python your_script_name.py
Replace your_script_name.py with the name of your Python file.

Adjust Your Schedule

If you need to add or remove classes, modify the schedule lines in the script. For example, you can change:

python
Copy code
schedule.every().day.at("08:00").do(classone)
To adjust the time and function according to your needs.

Example Schedule
Here's a sample schedule you might have in your script:

08:00 AM - First class link
09:40 AM - Second class link
11:20 AM - Third class link
Note
Make sure your computer is on and connected to the internet when running the script, as it needs to access the web browser to open the Zoom links.
