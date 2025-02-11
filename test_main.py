from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test creating a product
def test_create_product():
    response = client.post("/products/", json={"name": "Test Product", "description": "A test product", "price": 100.0})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["price"] == 100.0

# Test retrieving a product
def test_read_product():
    response = client.post("/products/", json={"name": "Sample", "description": "Another test", "price": 150.0})
    product_id = response.json()["id"]
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == product_id

# Test updating a product
def test_update_product():
    response = client.post("/products/", json={"name": "Old Product", "description": "Before update", "price": 99.0})
    product_id = response.json()["id"]
    update_response = client.put(f"/products/{product_id}", json={"name": "Updated Product", "description": "After update"})
    assert update_response.status_code == 200
    updated_data = update_response.json()
    assert updated_data["name"] == "Updated Product"

# Test deleting a product
def test_delete_product():
    response = client.post("/products/", json={"name": "To Be Deleted", "description": "Will be deleted", "price": 50.0})
    product_id = response.json()["id"]
    delete_response = client.delete(f"/products/{product_id}")
    assert delete_response.status_code == 200
