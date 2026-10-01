from app.hello import hello


def test_hello():
    assert hello() == "Hello from Mom Between Deployments!"
