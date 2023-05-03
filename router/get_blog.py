from enum import Enum
from fastapi import APIRouter, status, Response
from typing import Optional

router = APIRouter(
    prefix='/blog'
)

class BlogType(str, Enum):
  short = 'short'
  story = 'story'
  howto = 'howto' 


@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog type: {type}'}

#Predefined Type
#@app.get('blog/{id}')
#def get_blog(id: int):
#    return {'message': f'Blog with id {id}'}

#Query Parameter
#Default value
@router.get('/all')
def get_blog_all(page = 1, page_size = 10):
    return {'message' : f'All {page_size} blogs on page {page}'}

#Optional parameters
@router.get('/all_op')
def get_blog_optional(page = 1, page_size: Optional[int] = None):
    return {'message' : f'All {page_size} blogs on page {page}'}

#
@router.get('/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message' : f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}' }

@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog_status(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id}',
                'id': f'{id}',
                'message2': f'Selamat ID yg anda cari ada'
                }
