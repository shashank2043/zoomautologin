import schedule  # Import the schedule library for scheduling tasks
import time  # Import the time library to manage time-related tasks
import webbrowser  # Import the webbrowser library to open URLs in a web browser

def open_link(link):
    """
    Open the provided URL in the default web browser.
    """
    webbrowser.open(link)

def classone():
    """
    Open the Zoom link for the first class.
    """
    open_link('Zoom link')  # Replace 'Zoom link' with your actual Zoom link
    print('Opening first class...')

def classtwo():
    """
    Open the Zoom link for the second class.
    """
    open_link('Another zoom link')  # Replace 'Another zoom link' with your actual Zoom link
    print('Opening second class...')

def classthree():
    """
    Open the Zoom link for the third class.
    """
    open_link('Other zoom link')  # Replace 'Other zoom link' with your actual Zoom link
    print('Opening third class...')

# Schedule the class links to open at specific times
schedule.every().day.at("08:00").do(classone)  # Open the first class link at 8:00 AM
schedule.every().day.at("09:40").do(classtwo)  # Open the second class link at 9:40 AM
schedule.every().day.at("11:20").do(classthree)  # Open the third class link at 11:20 AM

# Main loop to keep the script running and check for scheduled tasks
while True:
    schedule.run_pending()  # Check if any scheduled task needs to be run
    time.sleep(1)  # Wait for 1 second before checking again
