import requests
from Tests.testData.fakerPostData import faker_data
import pytest

@pytest.mark.regression
def test_post_faker():
    url="https://fakestoreapi.com/products"
    i=0
    for i in range(10):
        payload= faker_data()
        response=requests.post(url,json=payload, verify=False)
        print(response.json())
        assert response.status_code==201
        