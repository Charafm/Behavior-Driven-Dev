from service.models import Product
from behave import given

@given('the following products')
def step_impl(context):
    for row in context.table:
        product = Product(name=row['name'], category=row['category'], available=row['available'] == 'True', price=row['price'])
        product.create()