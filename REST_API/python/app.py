from flask import Flask, render_template, request, redirect, url_for, flash
from api_service import get_products, get_categories, post_product

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Thêm dòng này để sử dụng flash

@app.route('/')
def index():
    products = get_products()
    categories = get_categories()
    return render_template('index.html', products=products, categories=categories)

@app.route('/products', methods=['POST'])
def add_product_route():
    # Lấy dữ liệu từ form gửi lên
    product = {
        "title": request.form['title'],
        "price": float(request.form['price']),
        "description": request.form['description'],
        "categoryId": int(request.form['categoryId']),
        "images": [request.form['image']]
    }
    post_product(product)
    flash("Thêm sản phẩm thành công!", "success")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)