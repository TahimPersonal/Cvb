from tinydb import TinyDB, Query

db = TinyDB("db.json")
posts_table = db.table("posts")

def is_post_processed(post_link):
    """Check if the post link has already been processed."""
    return posts_table.contains(Query().link == post_link)

def mark_post_processed(post_link):
    """Mark a post link as processed."""
    if not is_post_processed(post_link):
        posts_table.insert({"link": post_link})
