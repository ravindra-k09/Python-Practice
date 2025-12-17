from faker import Faker
import pytest
f=Faker("en_IN")
@pytest.fixture
def faker_data():
    return{
    "id": 21,
    "title": f.name(),
    "price": f.random_int(),
    "description": f.sentence(),
    "category": f.job(),
    "image": "http://example.com"
    }