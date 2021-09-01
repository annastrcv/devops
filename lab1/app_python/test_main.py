import main


def test_page():
    client = main.app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200, "The page is not available"


def test_time():
    client = main.app.test_client()
    resp = client.get('/')
    assert resp.data is not None, "The page returns smth"


