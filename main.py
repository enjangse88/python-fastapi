from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

class BlogType(str, Enum):
    short = 'short'
    story = 'Story'
    howto = 'howto'

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
@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog type: {type}'}

#Predefined Type
@app.get('blog/{id}')
def get_blog(id: int):
    return {'message': f'Blog with id {id}'}

#Query Parameter
#Default value
@app.get('/blog/all')
def get_blog_all(page = 1, page_size = 10):
    return {'message' : f'All {page_size} blogs on page {page}'}

#Optional parameters
@app.get('/blog/all_op')
def get_blog_optional(page = 1, page_size: Optional[int] = None):
    return {'message' : f'All {page_size} blogs on page {page}'}

#
@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message' : f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}' }