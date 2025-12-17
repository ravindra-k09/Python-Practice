#python -m pytest tests/api/test_post.py 
import requests
import json
import pytest
from Tests.testData.pydanticSchema import Product

def load_test_data():
    with open("tests/testData/productData.json") as testdata:
        return json.load(testdata)


@pytest.mark.parametrize("payload", load_test_data())
def test_post(payload):
    url="https://fakestoreapi.com/products"
    response=requests.post(url,json=payload, verify=False)
    assert response.status_code==201
    print(response.status_code)
    response_data=response.json()
   
    product = Product(**response_data)
    print("Pydantic Validation Done")

