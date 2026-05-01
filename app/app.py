import pytest


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def assert_ok(res):
    assert res.status_code == 200, f"URL {res.request.url} returned {res.status_code}"

def test_home(client):
    res = client.get("/")
    assert_ok(res)

def test_health(client):
    res = client.get("/health")
    assert_ok(res)