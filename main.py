import schedule #pip install schedule
import time 
import webbrowser #pip install pywhatkit

def open_link(link):
    webbrowser.open(link)

def classone():
    open_link('Zoom link')
    print('Opening...')

def classtwo():
    open_link('Another zoom link')
    print('Opening...')

def classthree():
    open_link('Other zoom link')
    print('Opening...')

#add lines like above three as your need or remove one if you have only two classes
schedule.every().day.at("08:00").do(classone) 
schedule.every().day.at("09:40").do(classtwo)
schedule.every().day.at("11:20").do(classthree)

#adjust your time table and timings

while 1:
    schedule.run_pending()
    time.sleep(1)
#voila your classes are automated