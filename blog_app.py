from fastapi import FastAPI, HTTPException
from datetime import datetime
import uuid

app = FastAPI()

posts = []
comments = []

@app.post("/posts")
def create_post(title:str,content:str):
    new_post = {
        "id" : str(uuid.uuid4()),
        "title" : title,
        "content" : content,
        "createTime" : datetime.utcnow()
    }
    posts.append(new_post)
    return new_post


@app.get("/posts")
def get_post():
    return posts

@app.put("/posts/{post_id}")
def update_post(post_id:str,content:str=None,title:str=None):
    for post in posts:
        if(post["id"] == post_id):
            if title :
                post["title"] = title
            if content:
                post["content"] = content
            return post
        raise HTTPException(status_code=404,details="Post not found")

@app.delete("/posts/{post_id}")
def delete_posts(post_id:str):
    global posts, comments
    posts = [p for p in posts : if p["id"]!=post_id]
    comments = [c for c in comments : if c["postID"]!=post_id]
    return{"message : post and comment deleted"}

@app.post("/posts/{post_id}/comments")
def add_comment(post_id:str,author:str,text:str):
    if not any(p["id"]==post_id for p in posts):
        raise HTTPException(status_code=404,details="Comment not found")

    new_comment{
        "id" = str(uuid.uuid4()),
        "postID" = post_id,
        "author" = author,
        "text" = text,
        "createTime" = datetime.utcnow()
    }    
    comments.append(new_comment)
    return new_comments

@app.get("/posts/{post_id}/comments")
def get_comments(post_id:str):
    return [c for c in comments : if c["postID"]==post_id]

@app.delete("/comments/{comment_id}")
def delete_comments(comment_id:str):
    global comments
    comments = [c for c in comments: if c["id"]!=comment_id]
    return {"message: comment deleted"}
