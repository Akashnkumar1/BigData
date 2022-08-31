from datetime import timedelta, date
from sys import platform
from airflow.utils.dates import days_ago

# The DAG object; we'll need this to instantiate a DAG

from airflow import DAG

# Operators; we need this to operate!

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

# Defining Python Function (to be called by every Operator/users)


#--------------------------------------------------------Basic Python---------------------------------------------------------------#

import json
import datetime
import platform
from random import randint

mail = ["akashnkumar1@tribes.ai","vinit@tribes.ai", "guilermo@tribes.ai",
         "christian@tribes.ai", "elly@tribes.ai"]

minutes_used = randint(0,180)

data_temp = []

def gen_data(**kwargs):
    
    ti = kwargs['ti']
    """ Users Genrating Data"""
    created_at = datetime.datetime.now().strftime("%Y-%m-%d")
    for i in mail:
        data = { "Details" : 
        {
            "user_id" : i ,
            "usages_date": created_at,
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
    
        data_temp.append(data)

    ti.xcom_push('mobile_data', data_temp)

def get_data(**kwargs):
    ti = kwargs['ti']
    extract_data = ti.xcom_pull(task_ids='pull data', key = 'mobile_data')
    mobile_data = json.dumps(extract_data)
    print(mobile_data)

    

#-----------------------------------------------------Creating DAG (Apache-Airflow)------------------------------------------------------------#


# These args will get passed on to each operator

# You can override them on a per-task basis during operator initialization

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['akashnkumar1@tribes.ai','vinit@tribes.ai', 'guilermo@tribes.ai', 'christian@tribes.ai', 'elly@tribes.ai'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),

}
with DAG(
    'Mobile_Usage',
    default_args=default_args,
    description='Daily Mobile Usage',
    schedule_interval='@daily',
    start_date=days_ago(2),
    catchup=False,
    tags=['App_Usage'],
    
) as App_usage:
    

    App_usage.doc_md = __doc__  # providing that you have a docstring at the beggining of the DAG or a README file.
    
    App_usage.doc_md =( """ This is a documentation placed anywhere """ )


    for i in range(len(mail)):
        task = PythonOperator(
            task_id='user_'+str(i)+'_details',
            depends_on_past=False,
            retries=3,
            python_callable=gen_data
    )

    task_final = PythonOperator(
            task_id='Get the data',
            python_callable=get_data
    )

[task] >> task_final
    