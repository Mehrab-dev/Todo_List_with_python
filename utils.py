import json
import uuid
import datetime
import os
from json import JSONDecodeError

data_file = "task.json"

def add_task(task_name,tags=None,description=None,status=None) :
    id = str(uuid.uuid4())
    date = str(datetime.datetime.today())
    new_data = {
        "id":id,
        "task_name" : task_name,
        "today_is_date" : date,
        "description" : description if description else " ",
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

def update_tasks(task_name,tags=None,description=None,status=None) :
    u_date = str(datetime.datetime.today())
    if os.path.exists(data_file):
        with open(data_file,"r",encoding="utf-8") as o :
            try :
                old_data = json.load(o)
            except JSONDecodeError :
                old_data = []
    else :
        old_data = []

    for i in old_data :
        if i["task_name"] == task_name :
            if description is not None :
                i["description"] = description
            if status is not None :
                i["status"] = status
            if tags is not None :
                i["tags"] = tags
            i["updated"] = u_date
            update = i
            break

    with open(data_file,"w",encoding="utf-8") as n :
        json.dump(old_data,n,ensure_ascii=False,indent=2)

    return update

def delete_task(tas_name) :
    if os.path.exists(data_file) :
        with open(data_file,"r",encoding="utf-8") as d :
            try :
                d_task = json.load(d)
            except JSONDecodeError :
                d_task = []
    else :
        d_task = []
    delete = False
    for i in d_task :
        if i["task_name"] == tas_name :
            d_task.remove(i)
            delete = True
            break
    if delete :
        with open(data_file,"w",encoding="utf-8") as nd :
            json.dump(d_task,nd,ensure_ascii=False,indent=2)
    return delete









