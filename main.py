from fastapi import FastAPI
from router import get_blog
from router import post_blog


app = FastAPI()
app.include_router(get_blog.router)
app.include_router(post_blog.router)

@app.get('/')
def index():
    return "Hello World"

@app.get('/hello')
def hello():
    return {'message': 'Welcome to the blog post'}

#@app.get('/blog/all')
#def get_all_blog():
#    return {'message': 'All blog post'}

#type Parameter
