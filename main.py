from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://MyBloggy:MyBloggy@localhost:8889/MyBloggy'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)



class MyBloggy(db.Model):
    title = db.Column(db.String(50), primary_key=True)
    blog = db.Column(db.String(500))
    
    

    def __init__(self, title, blog):
        self.title = title
        self.blog = blog

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        blog = request.form['blog']
        new_post = MyBloggy(title, blog)
        db.session.add(new_post)
        db.session.commit()
    
    completed_title = MyBloggy.query.all()

    return render_template('blog.html', completed_title = completed_title)

@app.route('/postblog', methods=['POST', 'GET']) 
def postblog(): 

        
    return render_template('postblog.html')

@app.route('/blog-post', methods=['POST', 'GET']) 
def redirectblog(): 
    title = request.form['title']
    post = request.form['post']
    return render_template('blog-post.html', title = title, post = post)


if __name__ == '__main__':
    app.run()