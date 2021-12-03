from app import app

def test_home():
    response = app.test_client().get('/')

    assert response.status_code == 200
    welcome_present = b"Welcome!" in response.data
    assert welcome_present == True

def test_days():
    response = app.test_client().get('/days/')

    assert response.status_code == 200
    monday_present = b"Monday" in response.data
    assert monday_present == True
