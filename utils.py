import json
import uuid
import datetime
import os
from json import JSONDecodeError

data_file = "task.json"

def add_task(task_name,tags=None,description=None,status=None) :
    id = str(uuid.uuid4())
    date = str(datetime.date.today())
    new_data = {
        "id":id,
        "task_name" : task_name,
        "today_is_date" : date,
        "description" : description if description else None,
        "status" : status if status else " ",
        "tags" : tags if tags else " ",
        "updated" : date
    }

    if os.path.exists(data_file) :
        with open(data_file,"r",encoding="utf-8") as a :
            try :
                old_data = json.load(a)
            except json.JSONDecodeError :
                old_data = []
    else :
        old_data = []

    old_data.append(new_data)

    with open(data_file,"w",encoding="utf-8") as n :
        json.dump(old_data,n,ensure_ascii=False,indent=2)

    return new_data

def list_tasks() :
    if os.path.exists(data_file) :
        with open(data_file,"r",encoding="utf-8") as r :
            try :
                r_data = json.load(r)
            except JSONDecodeError :
                r_data = []
    else :
        r_data = []

    return r_data



