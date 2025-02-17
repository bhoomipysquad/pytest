import requests

BASE_URL = "http://127.0.0.1:8000/api/v1/job/category/"

def test_get_request_with_filter():
    """
    Test the GET request to the CategoryView endpoint with query parameters.
    """
    # Query parameters for filtering
    params = {
        "job": "Developer",  # Replace with actual query parameter to test
    }

    # Headers if needed (e.g., for authorization or content type)
    headers = {
        "Content-Type": "application/json",
        # "Authorization": "Bearer <your-token>"  # Uncomment if authorization is required
    }

    # Make the GET request
    response = requests.get(BASE_URL, params=params, headers=headers)

    # Print the response for debugging
    print("Status Code:", response.status_code)
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not JSON:", response.text)

def test_get_request_without_filter():
    """
    Test the GET request to the CategoryView endpoint without query parameters.
    """
    # Headers if needed
    headers = {
        "Content-Type": "application/json",
        # "Authorization": "Bearer <your-token>"  # Uncomment if authorization is required
    }

    # Make the GET request
    response = requests.get(BASE_URL, headers=headers)

    # Print the response for debugging
    print("Status Code:", response.status_code)
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not JSON:", response.text)

if __name__ == "__main__":
    # Call test functions
    print("Test GET request with filter:")
    test_get_request_with_filter()

    print("\nTest GET request without filter:")
    test_get_request_without_filter()

import requests

BASE_URL = "http://127.0.0.1:8000/api/v1/job/submissions/"

def test_get_request_with_filter():
    """
    Test the GET request to the Submissions endpoint with query parameters.
    """
    # Query parameters for filtering
    params = {
        "job_id": "123",  # Replace with actual query parameter to test
        "status": "pending",  # Example additional filter parameter
    }

    # Headers if needed (e.g., for authorization or content type)
    headers = {
        "Content-Type": "application/json",
        # "Authorization": "Bearer <your-token>"  # Uncomment if authorization is required
    }

    # Make the GET request
    response = requests.get(BASE_URL, params=params, headers=headers)

    # Print the response for debugging
    print("Status Code:", response.status_code)
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not JSON:", response.text)

def test_get_request_without_filter():
    """
    Test the GET request to the Submissions endpoint without query parameters.
    """
    # Headers if needed
    headers = {
        "Content-Type": "application/json",
        # "Authorization": "Bearer <your-token>"  # Uncomment if authorization is required
    }

    # Make the GET request
    response = requests.get(BASE_URL, headers=headers)

    # Print the response for debugging
    print("Status Code:", response.status_code)
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not JSON:", response.text)

def test_post_request():
    """
    Test the POST request to the Submissions endpoint.
    """
    # Payload to send with the POST request
    payload = {
        "job_id": "123",  # Replace with actual keys and values required by the API
        "applicant_name": "John Doe",
        "status": "pending",
    }

    # Headers for the request
    headers = {
        "Content-Type": "application/json",
        # "Authorization": "Bearer <your-token>"  # Uncomment if authorization is required
    }

    # Make the POST request
    response = requests.post(BASE_URL, json=payload, headers=headers)

    # Print the response for debugging
    print("Status Code:", response.status_code)
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not JSON:", response.text)

def test_method_not_allowed():
    """
    Test methods that are not allowed on the endpoint.
    """
    # Headers for the request
    headers = {
        "Content-Type": "application/json",
        # "Authorization": "Bearer <your-token>"  # Uncomment if authorization is required
    }

    # PUT request (not allowed)
    payload = {"status": "approved"}
    response = requests.put(BASE_URL, json=payload, headers=headers)
    print("PUT Status Code:", response.status_code)
    print("PUT Response Body:", response.text)

    # DELETE request (not allowed)
    response = requests.delete(BASE_URL, headers=headers)
    print("DELETE Status Code:", response.status_code)
    print("DELETE Response Body:", response.text)

if __name__ == "__main__":
    # Run all test cases
    print("Test GET request with filter:")
    test_get_request_with_filter()

    print("\nTest GET request without filter:")
    test_get_request_without_filter()

    print("\nTest POST request:")
    test_post_request()

    print("\nTest methods not allowed:")
    test_method_not_allowed()