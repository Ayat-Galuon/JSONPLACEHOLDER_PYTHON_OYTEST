import pytest
import requests
import json
import csv


# Base URL of the API

BASE_URL = "https://jsonplaceholder.typicode.com"

def log_test_result(results):
    with open('results.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Request Type', 'Test', 'Response Status', 'Result'])
        writer.writerow(results)

# -------------------------------------get---------------------------------------

# Test 1: Status code is 200
def test_status_code_200():
    response = requests.get(f"{BASE_URL}/posts")
    result = 'Pass' if response.status_code == 200 else 'Fail'
    test_result = {
        'Request Type': 'GET',
        'Test': 'test_status_code_200',
        'Response Status': response.status_code,
        'Result': result
    }
    log_test_result(test_result)

    assert response.status_code == 200

# Test 2: Response time is less than 400ms
def test_response_time():
    response = requests.get(f"{BASE_URL}/posts")
    result = 'Pass' if response.elapsed.total_seconds() * 1000 < 400 else 'Fail'
    test_result = {
        'Request Type': 'GET',
        'Test': 'test_response_time',
        'Response Status': response.status_code,
        'Result': result
    }
    log_test_result(test_result)

    assert response.elapsed.total_seconds() * 1000 < 400 



# Test 3: Each post contains id, title, and body
def test_post_contains_required_fields():
    response = requests.get(f"{BASE_URL}/posts")
    json_data = response.json()
    result = 'Pass' if all("id" in post and "title" in post and "body" in post for post in json_data) else 'Fail'
    test_result = {
        'Request Type': 'GET',
        'Test': 'test_post_contains_required_fields',
        'Response Status': response.status_code,
        'Result': result
    }
    log_test_result(test_result)
    for post in json_data:
        assert "id" in post
        assert "title" in post
        assert "body" in post

# Test 4: Content-Type is application/json
def test_content_type_json():
    response = requests.get(f"{BASE_URL}/posts")
    result = 'Pass' if response.headers["Content-Type"] == "application/json; charset=utf-8" else 'Fail'
    test_result = {
        'Request Type': 'GET',
        'Test': 'test_content_type_json',
        'Response Status': response.status_code,
        'Result': result
    }
    log_test_result(test_result)    
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

# Test 5: Response should be JSON
def test_response_is_json():
    response = requests.get(f"{BASE_URL}/posts")
    try:
        response.json()
        result = 'Pass'
    except ValueError:
        result = 'Fail'
    test_result = {
        'Request Type': 'GET',
        'Test': 'test_response_is_json',
        'Response Status': response.status_code,
        'Result': result
    }
    log_test_result(test_result)
    assert result == 'Pass'

# Test 6: Status code is 404
def test_status_code_404():
    response = requests.get(f"{BASE_URL}/invalid_endpoint")
    result = 'Pass' if response.status_code == 404 else 'Fail'
    test_result = {
        'Request Type': 'GET',
        'Test': 'test_status_code_404',
        'Response Status': response.status_code,
        'Result': result
    }
    log_test_result(test_result)
    assert response.status_code == 404

# Test 7: Response body is empty
def test_empty_body():
    response = requests.get(f"{BASE_URL}/invalid_endpoint")
    result = 'Pass' if response.text == '{}' else 'Fail'
    test_result = {
        'Request Type': 'GET',
        'Test': 'test_empty_body',
        'Response Status': response.status_code,
        'Result': result
    }
    log_test_result(test_result)
    assert response.text == '{}'

# -------------------------------------put---------------------------------------


# Test 8: Status code is 200 (after updating post)
def test_status_code_200_after_update():
    response = requests.put(f"{BASE_URL}/posts/1", json={"title": "my new title", "body": "updated post"})
    result = 'Pass' if response.status_code == 200 else 'Fail'
    test_result = {
        'Request Type': 'PUT',
        'Test': 'test_status_code_200_after_update',
        'Response Status': response.status_code,
        'Result': result
    }
    log_test_result(test_result)
    assert response.status_code == 200


# Test 9: Response body contains updated fields
def test_updated_post_fields():
    response = requests.put(f"{BASE_URL}/posts/1", json={"title": "my new title", "body": "updated post"})
    json_data = response.json()
    result = 'Pass' if json_data["id"] == 1 and json_data["title"] == "my new title" and json_data["body"] == "updated post" else 'Fail'
    test_result = {
        'Request Type': 'PUT',
        'Test': 'test_updated_post_fields',
        'Response Status': response.status_code,
        'Result': result
    }
    log_test_result(test_result)
    assert json_data["id"] == 1
    assert json_data["title"] == "my new title"
    assert json_data["body"] == "updated post"

# Test 10: Content-Type is application/json (after update)
def test_content_type_json_after_update():
    response = requests.put(f"{BASE_URL}/posts/1", json={"title": "my new title", "body": "updated post"})
    result = 'Pass' if response.headers["Content-Type"] == "application/json; charset=utf-8" else 'Fail'
    test_result = {
        'Request Type': 'PUT',
        'Test': 'test_content_type_json_after_update',
        'Response Status': response.status_code,
        'Result': result
    }
    log_test_result(test_result)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

# -------------------------------------post---------------------------------------



# Test 11: Response body 'id' is a positive integer
def test_response_id_is_positive():
    response = requests.post(f"{BASE_URL}/posts", json={"title": "new post", "body": "test body", "userId": 1})
    json_data = response.json()
    result = 'Pass' if isinstance(json_data["id"], int) and json_data["id"] > 0 else 'Fail'
    test_result = {
        'Request Type': 'POST',
        'Test': 'test_response_id_is_positive',
        'Response Status': response.status_code,
        'Result': result
    }
    log_test_result(test_result)
    assert isinstance(json_data["id"], int)
    assert json_data["id"] > 0

# Test 12: Status code is 201 (after creating post)
def test_status_code_201():
    response = requests.post(f"{BASE_URL}/posts", json={"title": "Ayat", "body": "new post1", "userId": 5})
    result = 'Pass' if response.status_code == 201 else 'Fail'
    test_result = {
        'Request Type': 'POST',
        'Test': 'test_status_code_201',
        'Response Status': response.status_code,
        'Result': result
    }
    log_test_result(test_result)
    assert response.status_code == 201


# Test 13: Response body contains 'id' (after creating post)
def test_response_body_contains_id():
    response = requests.post(f"{BASE_URL}/posts", json={"title": "Ayat", "body": "new post1", "userId": 5})
    json_data = response.json()
    result = 'Pass' if "id" in json_data else 'Fail'
    test_result = {
        'Request Type': 'POST',
        'Test': 'test_response_body_contains_id',
        'Response Status': response.status_code,
        'Result': result
    }
    log_test_result(test_result)
    assert "id" in json_data

# Test 14: Response should be JSON (after creating post)
def test_response_is_json_after_create():
    response = requests.post(f"{BASE_URL}/posts", json={"title": "Ayat", "body": "new post1", "userId": 5})
    try:
        response.json()
        result = 'Pass'
    except ValueError:
        result = 'Fail'
    test_result = {
        'Request Type': 'POST',
        'Test': 'test_response_is_json_after_create',
        'Response Status': response.status_code,
        'Result': result
    }
    log_test_result(test_result)
    assert result == 'Pass'


    # Test 15: DELETE - Status code 200 when deleting post
def test_delete_post_success():
    response = requests.delete(f"{BASE_URL}/posts/1")
    result = 'Pass' if response.status_code == 200 else 'Fail'
    test_result = {
        'Request Type': 'DELETE',
        'Test': 'test_delete_post_success',
        'Response Status': response.status_code,
        'Result': result
    }
    log_test_result(test_result)
    assert response.status_code == 200

# Test 16: DELETE - Status code 404 when deleting non-existent post
def test_delete_post_not_found():
    response = requests.delete(f"{BASE_URL}/posts/9999")
    result = 'Pass' if response.status_code == 404 else 'Fail'
    test_result = {
        'Request Type': 'DELETE',
        'Test': 'test_delete_post_not_found',
        'Response Status': response.status_code,
        'Result': result
    }
    log_test_result(test_result)
    assert response.status_code == 404
