from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_start_scrape():
    test_input = {"name": "Helen Wall", "organization_name": "LinkedIN"}
    response = client.post("/scrape", json=test_input)
    assert response.status_code == 200
    assert "job_id" in response.json()


def test_get_scrape_results():
    test_job_id = "test_job_id"
    response = client.get(f"/scrape_results/{1}")
    assert response.status_code == 200
    assert "status" in response.json()
