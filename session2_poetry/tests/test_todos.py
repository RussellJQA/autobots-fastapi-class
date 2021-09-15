# Poetry-installed
import requests

TO_DOS_URL = "https://df-flask-todo-api-class.herokuapp.com/todos"
TO_DO_URL = "https://df-flask-todo-api-class.herokuapp.com/todo"
DONE_URL = "https://df-flask-todo-api-class.herokuapp.com/todo/335"


def test_math():
    assert 2 + 2 == 4


def test_get_todos():
    response = requests.get(TO_DOS_URL)
    assert response.status_code == 200


def test_add_todo():
    payload = {"title": "buy bread", "done": False}
    add_response = requests.post(TO_DO_URL, json=payload)
    if add_response.status_code == 200:
        todo = add_response.json()
        assert todo["title"] == "buy bread"
    else:
        assert False, f"add_response.status_code: {response.status_code}"


def test_delete_todo():
    payload = {"title": "buy eggs", "done": False}
    add_response = requests.post(TO_DO_URL, json=payload)
    if add_response.status_code == 200:
        todo = add_response.json()
        todo_id = todo["id"]
        delete_response = requests.delete(f"{TO_DO_URL}/{todo_id}")
        assert delete_response.status_code == 200
    else:
        assert False, f"add_response.status_code: {add_response.status_code}"


def test_mark_todo_complete():
    payload = {"title": "buy milk", "done": False}
    add_response = requests.post(TO_DO_URL, json=payload)
    if add_response.status_code == 200:
        todo = add_response.json()
        todo_id = todo["id"]
        done_response = requests.patch(f"{TO_DO_URL}/{todo_id}", json={"done": True})
        completed_todo = done_response.json()
        assert completed_todo["done"] is True
    else:
        assert False, f"add_response.status_code: {add_response.status_code}"
