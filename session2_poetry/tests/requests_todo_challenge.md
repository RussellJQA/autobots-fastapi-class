# Requests Todo Challenge

You have been tasked to make sure the following api works using `requests` and `pytest`. Sadly the developer who created this api didn't document his code and didn't know about the awesome auto docs [swaggerui](https://swagger.io/tools/swagger-ui/). All you get is the url to the ui which is https://df-react-todo-client-class.herokuapp.com/. Please take what you learned from class on how to use the network tab to find out what api calls are being used, which should be full CRUD. Once you feel comfortable with the routes go ahead and create any tests that make you confident in this api.

> Please try to not use any `for loops` and `while loops` or else we will run out of the free hours for everyone.

## Example

```python
def test_get_todos():
    response = requests.get("PUT URL HERE")
    assert response.status_code == 200

def test_add_todos():
    pass

def test_delete_todos():
    pass

def test_mark_todos_complete():
    pass
```

## Helpful Sites

- [Requests Docs](https://docs.python-requests.org/en/master/)
- [Pytest Docs](https://pytest.org/)
- [TestAutomationU Pytest Course](https://testautomationu.applitools.com/pytest-tutorial/)
- [TestAutomationU API Testing In Python](https://testautomationu.applitools.com/python-api-testing/)
  - I personally haven't taken this course but TestAutomationU hasn't let me down
- ASK QUESTIONS IN SLACK!!!
