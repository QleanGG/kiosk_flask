from flask import jsonify, request
from app import app,db
from models import Product

@app.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "hello class"})

@app.route('/products', methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([{
        'id': product.id,
        'title': product.title,
        'company': product.company,
        'kosher': product.kosher,
        'amount': product.amount,
        'expiration_date': product.expiration_date
    }for product in products])
    
@app.route('/products/<int:id>', methods=["GET"])
def get_product(id):
    product = Product.query.get(id) # Select * from Product Where products.id = 2;
    if not product:
        return jsonify({"message":"no item was found"}),404
    
    return jsonify({
        'id': product.id,
        'title': product.title,
        'company': product.company,
        'kosher': product.kosher,
        'amount': product.amount,
        'expiration_date': product.expiration_date
    })
        
    
@app.route('/products', methods=["POST"])
def add_product():
    data = request.get_json()
    new_prod = Product(
        title = data['title'],
        company = data['company'],
        kosher=data['kosher'],
        amount=data['amount']
    )
    db.session.add(new_prod)
    db.session.commit()
    return jsonify({"message": f"product added! {new_prod}"}), 201

@app.route('/products/<int:id>', methods=["DELETE"])
def del_product(id):
    product = Product.query.get(id) # Select * from Product Where products.id = 2;
    if not product:
        return jsonify({"message":"no item was found"}),404
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "product deleted!"})

@app.route('/products/<int:id>', methods=["PUT","PATCH"])
def edit_product(id):
    old_product = Product.query.get(id)  #Select * from Product Where products.id = 2;
    if not old_product:
        return jsonify({"message":"no item was found"}),404
    
    data = request.get_json()
    old_product.title = data.get('title',old_product.title)
    old_product.company = data.get('company',old_product.company)
    old_product.kosher = data.get('kosher',old_product.kosher)
    old_product.amount = data.get('amount',old_product.amount)
    
    db.session.commit() 
    return jsonify({"message": "product edited succesfully!"})