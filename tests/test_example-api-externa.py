import json
from flask import Flask
from src.app import create_app

def test_usd_to_brl(monkeypatch):
    # Simula a resposta da API externa
    class MockResponse:
        status_code = 200
        
        def json(self):
            return {
                "USDBRL": {
                    "bid": "5.10"
                }
            }

    def mock_get(url):
        return MockResponse()

    # Substitui requests.get pela versão mockada
    import requests
    monkeypatch.setattr(requests, "get", mock_get)

    app = create_app()
    client = app.test_client()
    response = client.get('/exchange/usd-to-brl')

    assert response.status_code == 200
    data = response.get_json()
    assert data["rate"] == "5.10"
