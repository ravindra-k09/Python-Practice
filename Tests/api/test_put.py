import requests


def test_put():
    url="https://fakestoreapi.com/products/21"
    payload={
    "id": 21,
    "title": "Ravindra",
    "price": 0.1,
    "description": "Qa Testing",
    "category": "QA",
    "image": "http://example.com"
}
    response=requests.put(url,json=payload, verify=False)
    print(response.json())
    assert response.status_code==200