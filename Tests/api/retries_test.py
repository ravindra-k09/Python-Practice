import requests
from  src.retries import get_custom_session
def test_retries():
    try:
        url="https://fakestoreapi.com/carts/1?sleep=5000"
        session=get_custom_session()
        response=session.get(url, verify=False, timeout= 1)
        print(f"Status Code {response.status_code}")
        assert response.status_code==200
    except requests.exceptions.Timeout:
        print("Request timed out!")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")