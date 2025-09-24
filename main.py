import argparse
from xml.etree.ElementTree import indent

import utils
from utils import add_task,list_tasks

parser = argparse.ArgumentParser(description="Todo List")

sub_argument = parser.add_subparsers(dest="command")
a_task = sub_argument.add_parser("add",help="for add task")
a_task.add_argument("task_name")
a_task.add_argument("--t",help="tags for task",required=False)
a_task.add_argument("--ds",help="description of the task",required=False)
a_task.add_argument("--st",help="status the task",required=False)

li_tasks = sub_argument.add_parser("list",help="for list all tasks ")

args = parser.parse_args()

if args.command == "add" :
    add_task(task_name=args.task_name,tags=args.t,description=args.ds,status=args.st)

if args.command == "list" :
    print(utils.list_tasks())




