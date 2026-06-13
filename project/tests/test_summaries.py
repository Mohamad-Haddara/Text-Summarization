import json

import pytest

def test_create_summary(test_app_with_db):
    response = test_app_with_db.post("/summaries/", data = json.dumps({"url": "https://foo.bar"}))
    
    assert response.status_code == 201
    # Parse the response body from JSON into a dict, grab the "url" field, and verify it matches the URL we expected
    assert response.json()["url"] == "https://foo.bar" 