import argparse
from utils import add_task, list_tasks, update_tasks, delete_task , search_task_with_tags , search_task_with_name

parser = argparse.ArgumentParser(description="Todo List")

sub_argument = parser.add_subparsers(dest="command")
a_task = sub_argument.add_parser("add",help="for add task")
a_task.add_argument("task_name")
a_task.add_argument("--t",help="tags for task",required=False)
a_task.add_argument("--ds",help="description of the task",required=False)
a_task.add_argument("--st",help="status the task",required=False)

li_tasks = sub_argument.add_parser("list",help="for list all tasks ")

up_task = sub_argument.add_parser("u",help="for update task")
up_task.add_argument("task_name",help="identifier to identify the task")
up_task.add_argument("--t",help="tags for task in task update",required=False)
up_task.add_argument("--ds",help="description for task (in update)",required=False)
up_task.add_argument("--st",help="to change to task status",required=False)

del_task = sub_argument.add_parser("del",help="to a delete task from json file with task_name")
del_task.add_argument("task_name")

search_task = sub_argument.add_parser("sr-t",help="search task with tags")
search_task.add_argument("tag",help="tag name for search")

search_task_name = sub_argument.add_parser("sr-n",help="search tasks with name")
search_task_name.add_argument("task_name",help="name task for search")

args = parser.parse_args()

if args.command == "add" :
    add_task(task_name=args.task_name,tags=args.t,description=args.ds,status=args.st)

if args.command == "list" :
    print(list_tasks())

if args.command == "u" :
    print(update_tasks(task_name=args.task_name,tags=args.t,description=args.ds,status=args.st))

if args.command == "del" :
    delete_task(args.task_name)

if args.command == "sr-t" :
    print(search_task_with_tags(args.tag))

if args.command == "sr-n" :
    print(search_task_with_name(args.task_name))


