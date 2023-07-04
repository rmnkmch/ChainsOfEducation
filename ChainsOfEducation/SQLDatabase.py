import sqlite3


class SQLDatabase(object):
    """Database with SQL methods"""

    def create_connection(self, path):
        self.connection = None
        self.cursor = None
        try:
            self.connection = sqlite3.connect(path)
            self.cursor = self.connection.cursor()
        except:
            print("The create_connection error")

    def close_connection(self):
        try:
            self.cursor.close()
            self.connection.close()
        except:
            print("The close_connection error")

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            print("The execute_query error")

    def execute_read_query(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except:
            print("The execute_read_query error")

    def create_table_query(self):
        return """
        CREATE TABLE IF NOT EXISTS KnowledgeBlocks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL);"""

    def create_KB_query(self, title, description):
        return f"""
        INSERT INTO
        KnowledgeBlocks (title, description)
        VALUES ({title}, {description});"""

    def update_KB_query(self, title, description):
        return f"""
        UPDATE KnowledgeBlocks
        SET description = {description}
        WHERE title = {title}"""


"""
SELECT
  users.id,
  users.name,
  posts.description
FROM
  posts
  INNER JOIN users ON users.id = posts.user_id
"""

"""
SELECT
  posts.description as post,
  text as comment,
  name
FROM
  posts
  INNER JOIN comments ON posts.id = comments.post_id
  INNER JOIN users ON users.id = comments.user_id
"""
"""
SELECT
  description as Post,
  COUNT(likes.id) as Likes
FROM
  likes,
  posts
WHERE
  posts.id = likes.post_id
GROUP BY
  likes.post_id
"""
"SELECT description FROM posts WHERE id = 2"
       
"DELETE FROM comments WHERE id = 5"

""" SELECT name, weapon FROM characters ORDER BY name DESC """
"""SELECT * 
FROM albums 
WHERE genre = 'rock' AND sales_in_millions <= 50 
ORDER BY released
"""
"""SELECT artist,album,released 
FROM albums 
WHERE released = (
 SELECT MIN(released) FROM albums
);
"""
"""TRUNCATE TABLE table_name;"""

"""
SELECT * FROM albums WHERE genre IN ('pop','soul');
SELECT * FROM albums WHERE released BETWEEN 1975 AND 1985;
SELECT * FROM albums WHERE album LIKE '%R%';
"""

