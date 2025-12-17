# python -m pytest -s tests/api/test_delete.py
import requests
import pytest

@pytest.mark.regression
def test_delete():
        url="https://fakestoreapi.com/products/1"
        response=requests.delete(url, verify=False)

        assert response.status_code==200
        data=response.json()
        print(data)