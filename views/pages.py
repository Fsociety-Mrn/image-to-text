from flask import Blueprint, render_template, redirect, url_for

pages = Blueprint('pages', __name__)

@pages.route('/')
def default_redirect():
    return redirect(url_for('pages.pages_index'))

@pages.route('/pages')
def pages_index():
    return render_template('index.html')

@pages.route('/pages/demo-ocr')
def demo_ocr():
    return render_template('demo-ocr.html')

