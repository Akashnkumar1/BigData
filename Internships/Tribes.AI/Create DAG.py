from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime


def create_dag(dag_id,
               schedule,
               dag_number,
               default_args):

    def new_dag_py(*args):
        print('This is DAG: {}'.format(str(dag_number)))

    dag = DAG(dag_id,
              schedule_interval=schedule,
              default_args=default_args)

    with dag:
        t1 = PythonOperator(
            task_id='hello_world',
            python_callable=hello_world_py)

    return dag

n = input('Enter DAG ID: ')

dag_id = '{}'.format(str(n))

default_args = {'owner': 'airflow',
                    'start_date': datetime(2021, 1, 1)
                    }

ls = ['None','@once','@daily','@hourly','@weekly','@monthly','@yearly']
print('Availabe Schedules {}'.format(ls))
operation = input('Choose Schedule: ')
if operation in ls:
    schedule = operation
else:
    print('Enter correct values')

dag_number = n

globals()[dag_id] = create_dag(dag_id,
                                  schedule,
                                  dag_number,
                                  default_args)