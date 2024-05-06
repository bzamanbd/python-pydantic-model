from pydantic import BaseModel
class Comment(BaseModel):
    author:str
    comment:str
    likes:int

class Post(BaseModel):
    id:int
    author:str
    co_author:str | None = None
    date:str
    title:str
    content:str
    likes:list[str]
    comments:list[Comment]

comments = [ 
    Comment(author="userone",comment="comment from userone", likes=10),
    Comment(author="usertwo",comment="comment from usertwo", likes=20)
]

post = Post( 
    id=101,
    author="Rana", 
    co_author="",
    date="10/10/2010", 
    title="Title of Post", 
    content="This is the content of the post", 
    likes=['10'], 
    comments=comments
)


print(post.author)
