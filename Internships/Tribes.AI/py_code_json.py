from datetime import date
from time import strftime
import platform
from random import randint

mail = ["akashnkumar1@tribes.ai","vinit@tribes.ai", "guilermo@tribes.ai",
         "christian@tribes.ai", "elly@tribes.ai"]
minutes_used = randint(0,180)

def gen_data():
    for i in mail:
        data = { "Details" : 
        {
            "user_id" : i ,
            "usages_date": date.today.strftime("%Y-%m-%D"),
            "OS" : platform.uname().system,
            "brand" : platform.uname().machine
        },
        "usages" : [
            {
                "app_name" : "slack",
                "minutes_used" : minutes_used ,
                "app_category" : "communication"
            },
            {
                "app_name" : "gmail",
                "minutes_used" : minutes_used ,
                "app_category" : "communication"
            },
            {
                "app_name" : "jira",
                "minutes_used" : minutes_used ,
                "app_category" : "communication"
            },
            {
                "app_name" : "google drive",
                "minutes_used" : minutes_used ,
                "app_category" : "communication"
            },
            {
                "app_name" : "chrome",
                "minutes_used" : minutes_used,
                "app_category" : "communication"
            },
            {
                "app_name" : "spotify",
                "minutes_used" :  minutes_used,
                "app_category" : "communication"
            }
        ]
    }

    return data

