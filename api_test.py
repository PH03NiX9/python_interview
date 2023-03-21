# Write a pytest test for checking the endpoint of an API
import requests


def test_api_endpoint():
    response = requests.get("https://api.example.com/my-endpoint")
    assert response.status_code == 200
    assert response.json()["data"] == "expected result"
