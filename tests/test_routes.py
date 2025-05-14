def test_get_product(client):
    response = client.get("/products/1")
    assert response.status_code == 200

def test_update_product(client):
    response = client.put("/products/1", json={"name": "Updated"})
    assert response.status_code == 200

def test_delete_product(client):
    response = client.delete("/products/1")
    assert response.status_code == 204

def test_list_all_products(client):
    response = client.get("/products")
    assert response.status_code == 200

def test_list_by_name(client):
    response = client.get("/products", query_string={"name": "Phone"})
    assert response.status_code == 200

def test_list_by_category(client):
    response = client.get("/products", query_string={"category": "Electronics"})
    assert response.status_code == 200

def test_list_by_availability(client):
    response = client.get("/products", query_string={"available": "true"})
    assert response.status_code == 200