
""" 
Developer: Palash Khan on [22-01-2022]
website: www.randomwork.io

Test Heroku Cloud Application Platform 
"""

import schedule
import time
from datetime import datetime, timedelta
import pytz
import requests

def job():
    print('life is beautiful!!!')

# Run job every 2 minute
schedule.every(2).minutes.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)

