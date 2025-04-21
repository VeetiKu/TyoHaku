import db


def get_all_classes():
    sql = "SELECT title, value FROM classes ORDER BY id"
    result = db.query(sql)
 
    classes = {}
    for title, value in result:
        classes[title] = []
    for title, value in result:
        classes[title].append(value)
 
    return classes

def add_item(title, author, description, salary, location, deadline, user_id, classes):
    sql = "INSERT INTO items (title, author, description, salary, location, deadline, user_id) VALUES (?, ?, ?, ? ,?, ?,?)"
    db.execute(sql, [title, author, description, salary, location, deadline, user_id])
    
    item_id = db.last_insert_id()
    
    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [item_id, title, value])
        
        
def get_classes(item_id):
    sql = "SELECT title, value FROM item_classes WHERE item_id = ?"
    return db.query(sql, [item_id])
        
    
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

def update_item(item_id, title, author, description, salary, location, deadline, classes):
    sql = """ UPDATE items SET title = ?, description = ?, author = ?, salary = ?, location = ?, deadline = ? WHERE id = ?
    """
    db.execute(sql, [title, author, description, salary, location, deadline, item_id])
    
    sql = "DELETE FROM item_classes WHERE item_id = ?"
    db.execute(sql, [item_id])
    
    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [item_id, title, value])
    
def remove_item(item_id):
    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])
    
def find_items(query):
    sql = """ SELECT id, title FROM items WHERE description LIKE ? OR title LIKE ? ORDER BY id DESC
    """
    
    like = "%" + query + "%"
    return db.query(sql, [like, like])

def add_application(item_id, user_id, message):
    sql = """INSERT INTO applications (item_id, user_id, message)
            VALUES (?, ?, ?)"""
    db.execute(sql, [item_id, user_id, message])
 
def get_applications(item_id):
    sql = """SELECT applications.message, users.id user_id, users.username
            FROM applications, users
            WHERE applications.item_id = ? AND applications.user_id = users.id
            ORDER BY applications.id DESC"""
    return db.query(sql, [item_id])