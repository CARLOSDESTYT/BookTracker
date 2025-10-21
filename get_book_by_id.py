import sqlite3

def get_book_by_id(book_uid):
   
    try:
       
        conn = sqlite3.connect('books.db')
        conn.row_factory = sqlite3.Row  
        cursor = conn.cursor()
        
        
        cursor.execute("SELECT * FROM books WHERE uid = ?", (id,))
        
        
        book = cursor.fetchone()
        if book:
            return dict(book)
        else:
            return None
            
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        if conn:
            conn.close()

