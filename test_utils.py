import json
import utils

def test_add_task(tmp_path,monkeypatch) :
    data_file = tmp_path / "task.json"
    monkeypatch.setattr(utils,"data_file",str(data_file))

    task = utils.add_task(task_name="Buy Milk")

    assert task["task_name"] == "Buy Milk"

    with open(data_file,"r",encoding="utf-8") as t :
        tasks = json.load(t)
    assert len(tasks) == 1
    assert tasks[0]["task_name"] == "Buy Milk"

def test_list_tasks(tmp_path,monkeypatch) :
    data_file = tmp_path / "task.json"
    monkeypatch.setattr(utils,"data_file",str(data_file))

    utils.add_task(task_name="Buy_Car",description="in April")
    l_tasks = utils.list_tasks()

    assert len(l_tasks) == 1
    assert l_tasks[0]["task_name"] == "Buy_Car"

def test_update_task(tmp_path,monkeypatch) :
    data_file = tmp_path / "task.json"
    monkeypatch.setattr(utils,"data_file",str(data_file))

    task = utils.add_task(task_name="Buy Milk")
    assert task["task_name"] == "Buy Milk"

    u_t = utils.update_tasks(task_name="Buy Milk",description="for school",status="done")

    assert u_t["description"] == "for school"
    assert u_t["status"] == "done"

    with open(data_file,"r",encoding="utf-8") as u :
        u_data = json.load(u)
    assert u_data[0]["description"] == "for school"
    assert u_data[0]["status"] == "done"

def test_delete_task(tmp_path,monkeypatch) :
    data_file = tmp_path / "task.json"
    monkeypatch.setattr(utils,"data_file",str(data_file))

    fake_task = utils.add_task(task_name="Buy Milk")
    assert fake_task["task_name"] == "Buy Milk"

    delete = utils.delete_task(tas_name="Buy Milk")
    assert delete is True