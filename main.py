import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
'''
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post
'''
app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/hello', methods=['PUT'])
def hello():
    name = request.args.get('name')
    return f"Hello, {name}!" if name else "Hello, World!"

@app.route('/package', methods=['POST'])
def package():
    '''
    connect to the database first
    create an id for it and the id value increments
    request try if validate
    request.json to get inputs
    do the url one, require the URL as the input instead of zip
    Use github API to get name of package and 
    get and return the metadata as shown in swagger
    Get metadata using GitHub API
    '''

if __name__ == '__main__':
    app.run()