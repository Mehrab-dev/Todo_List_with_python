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
