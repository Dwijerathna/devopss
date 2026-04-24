from app import app
def test_home():
    cilent=app.test_client()
    response=cilent.get('/')
    assert response.status_code==200
    assert response.data==b'Hello, Devops World:V1 'in response.data