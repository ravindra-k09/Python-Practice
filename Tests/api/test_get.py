#python -m pytest tests/api/test_get.py
import requests
import pytest

@pytest.mark.regression
def test_get():
    url = "https://fakestoreapi.com/products/1"
    response = requests.get(url, verify=False)
    assert response.status_code==200
    print(response.text)
    data = response.json()
    for field in ["id", "title", "price", "description", "category"]:
        assert field in data, f"Missing field: {field}"

def test_negitive():
    url = "https://fakestoreapi.com/product/1"
    response=requests.get(url, verify=False)
    assert response.status_code == 404 