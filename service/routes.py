from flask import app, jsonify
from service.models import Product
from flask import request
from flask import Flask


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = Product.find(product_id)
    return jsonify(product.serialize()), 200

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = Product.find(product_id)
    product.deserialize(request.get_json())
    product.update()
    return jsonify(product.serialize()), 200

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.find(product_id)
    product.delete()
    return "", 204

@app.route("/products", methods=["GET"])
def list_products():
    name = request.args.get("name")
    category = request.args.get("category")
    available = request.args.get("available")

    if name:
        products = Product.find_by_name(name)
    elif category:
        products = Product.find_by_category(category)
    elif available:
        products = Product.find_by_availability(available.lower() == 'true')
    else:
        products = Product.all()

    return jsonify([p.serialize() for p in products]), 200