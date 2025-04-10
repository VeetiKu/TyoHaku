import db

def add_item(title, author, description, salary, location, deadline, user_id):
    sql = "INSERT INTO items (title, author, description, salary, location, deadline, user_id) VALUES (?, ?, ?, ? ,?, ?,?)"
    db.execute(sql, [title, author, description, salary, location, deadline, user_id])
    
def get_items():
    sql = "SELECT id, title, location FROM items ORDER BY id DESC"
    
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.id, items.title, items.author, items.salary, items.description, items.location, items.deadline, users.username, users.id user_id
    FROM items, users
    Where items.user_id = users.id AND
    items.id = ?
    """
    result = db.query(sql, [item_id])
    return result[0] if result else None

def update_item(item_id, title, author, description, salary, location, deadline):
    sql = """ UPDATE items SET title = ?, description = ?, author = ?, salary = ?, location = ?, deadline = ? WHERE id = ?
    """
    db.execute(sql, [title, author, description, salary, location, deadline, item_id])
    
def remove_item(item_id):
    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])
    
def find_items(query):
    sql = """ SELECT id, title FROM items WHERE description LIKE ? OR title LIKE ? ORDER BY id DESC
    """
    
    like = "%" + query + "%"
    return db.query(sql, [like, like])