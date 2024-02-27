def create_new_task(client, name=None):
    client.post("/task", json={
        "name": "test-name" if name is None else name
    })


def test_post_task(client):
    response = client.post("/task", json={"name": "test-post"})
    assert response.status_code == 201
    content = response.get_json()
    assert content["result"]["name"] == "test-post"
    assert content["result"]["id"] == 1
    assert content["result"]["status"] == 0


def test_post_task_error(client):
    response = client.post("/task", json={"id": "test-post"})
    assert response.status_code == 400


def test_get_tasks(client):
    create_new_task(client, name="test-get")
    response = client.get("/tasks")
    assert response.status_code == 200
    content = response.get_json()
    assert content["result"][0]["name"] == "test-get"
    assert content["result"][0]["id"] == 1
    assert content["result"][0]["status"] == 0


def test_put_task(client):
    create_new_task(client, name="test-put")
    response = client.put("/task/1", json={"id": 1, "name": "new-name", "status": 1})
    assert response.status_code == 200
    content = response.get_json()
    assert content["result"]["name"] == "new-name"
    assert content["result"]["id"] == 1
    assert content["result"]["status"] == 1


def test_put_task_lack_info(client):
    create_new_task(client, name="test-put")
    response = client.put("/task/1", json={"name": "new-name", "status": 1})
    assert response.status_code == 400


def test_put_not_exist_task(client):
    response = client.put("/task/1", json={"name": "new-name", "status": 1})
    assert response.status_code == 404


def test_delete_task(client):
    create_new_task(client, name="test-delete")
    response = client.delete("/task/1")
    assert response.status_code == 200
    response = client.get("/tasks")
    content = response.get_json()
    assert content["result"] == []
