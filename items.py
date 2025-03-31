import db

def add_item(title, author, description, salary, location, user_id):
    sql = "INSERT INTO items (title, author, description, salary, location, user_id) VALUES (?, ?, ?, ? ,?, ?)"
    db.execute(sql, [title, author, description, salary, location, user_id])
    
def get_items():
    sql = "SELECT id, title, location FROM items ORDER BY id DESC"
    
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.title, items.author, items.salary, items.description, items.location, users.username
    FROM items, users
    Where items.user_id = users.id AND
    items.id = ?
    """
    return db.query(sql, [item_id])[0]