from flask import Flask, render_template, redirect, url_for, request, session, flash
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-for-testing')

# Add context processor to make 'now' available in all templates
@app.context_processor
def inject_now():
    return {'now': datetime.now()}

# Sample course data
courses = [
    {
        'id': 1,
        'title': 'AWS Certified Solutions Architect - Associate',
        'description': 'Learn to design and deploy scalable, highly available systems on AWS.',
        'price': 299.99,
        'duration': '3 months',
        'level': 'Intermediate',
        'image': 'sa-associate.jpg'
    },
    {
        'id': 2,
        'title': 'AWS Certified Developer - Associate',
        'description': 'Master developing, deploying, and debugging cloud-based applications using AWS.',
        'price': 249.99,
        'duration': '2.5 months',
        'level': 'Intermediate',
        'image': 'developer.jpg'
    },
    {
        'id': 3,
        'title': 'AWS Certified SysOps Administrator - Associate',
        'description': 'Learn to deploy, manage, and operate scalable systems on AWS.',
        'price': 279.99,
        'duration': '2.5 months',
        'level': 'Intermediate',
        'image': 'sysops.jpg'
    },
    {
        'id': 4,
        'title': 'AWS Certified Solutions Architect - Professional',
        'description': 'Advanced architectural patterns and best practices for complex AWS solutions.',
        'price': 449.99,
        'duration': '4 months',
        'level': 'Advanced',
        'image': 'sa-pro.jpg'
    },
    {
        'id': 5,
        'title': 'AWS Certified DevOps Engineer - Professional',
        'description': 'Master continuous delivery and process automation on AWS.',
        'price': 399.99,
        'duration': '3.5 months',
        'level': 'Advanced',
        'image': 'devops.jpg'
    }
]

# Shopping cart stored in session
def get_cart():
    if 'cart' not in session:
        session['cart'] = []
    return session['cart']

@app.route('/')
def home():
    return render_template('index.html', courses=courses)

@app.route('/course/<int:course_id>')
def course_detail(course_id):
    course = next((c for c in courses if c['id'] == course_id), None)
    if course:
        return render_template('course_detail.html', course=course)
    return redirect(url_for('home'))

@app.route('/cart')
def cart():
    cart_items = get_cart()
    cart_courses = []
    total = 0
    for item_id in cart_items:
        course = next((c for c in courses if c['id'] == item_id), None)
        if course:
            cart_courses.append(course)
            total += course['price']
    return render_template('cart.html', cart_courses=cart_courses, total=total)

@app.route('/add_to_cart/<int:course_id>')
def add_to_cart(course_id):
    cart = get_cart()
    if course_id not in cart:
        cart.append(course_id)
        session['cart'] = cart
        flash('Course added to cart!', 'success')
    else:
        flash('Course is already in your cart!', 'info')
    return redirect(url_for('home'))

@app.route('/remove_from_cart/<int:course_id>')
def remove_from_cart(course_id):
    cart = get_cart()
    if course_id in cart:
        cart.remove(course_id)
        session['cart'] = cart
        flash('Course removed from cart!', 'success')
    return redirect(url_for('cart'))

@app.route('/checkout')
def checkout():
    cart_items = get_cart()
    if not cart_items:
        flash('Your cart is empty!', 'warning')
        return redirect(url_for('home'))
    
    cart_courses = []
    total = 0
    for item_id in cart_items:
        course = next((c for c in courses if c['id'] == item_id), None)
        if course:
            cart_courses.append(course)
            total += course['price']
    
    return render_template('checkout.html', cart_courses=cart_courses, total=total)

@app.route('/process_payment', methods=['POST'])
def process_payment():
    # In a real app, this would process payment through a payment gateway
    # For demo purposes, we'll just clear the cart and show a success message
    session['cart'] = []
    return render_template('thank_you.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=os.environ.get('DEBUG', 'False').lower() == 'true')