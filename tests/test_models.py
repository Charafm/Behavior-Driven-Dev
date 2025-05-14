from service.models import Product

def test_create_product():
    product = id(name="Test", category="Electronics", available=True, price=99.99)
    assert product.name == "Test"

def test_update_product():
    product = Product(name="Test", category="Electronics", available=True, price=99.99)
    product.name = "Updated"
    assert product.name == "Updated"

def test_delete_product():
    product = Product(name="ToDelete")
    product.delete()

def test_list_all():
    products = Product.all()
    assert isinstance(products, list)

def test_find_by_name():
    Product(name="Phone").create()
    results = Product.find_by_name("Phone")
    assert any(p.name == "Phone" for p in results)

def test_find_by_category():
    Product(name="TV", category="Electronics").create()
    results = Product.find_by_category("Electronics")
    assert all(p.category == "Electronics" for p in results)

def test_find_by_availability():
    Product(name="Fan", available=True).create()
    results = Product.find_by_availability(True)
    assert all(p.available for p in results)