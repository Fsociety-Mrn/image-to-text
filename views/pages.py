from flask import Blueprint, render_template, redirect, url_for

pages = Blueprint('image-to-text', __name__)

@pages.route('/')
def default_redirect():
    return redirect(url_for('image-to-text.pages_index'))

@pages.route('/image-to-text')
def pages_index():
    return render_template('index.html')

@pages.route('/image-to-text/demo-ocr')
def demo_ocr():
    return render_template('demo-ocr.html')

