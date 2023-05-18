from flaskext.mysql import MySQL
from app import app


mysql = MySQL()
mysql.init_app(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'test'



"""Class representing the structure of the data in the DB Key = Colum, Value = Data."""
class Todo:
    def __init__(self, id: int, name: str, done: bool):
        self.id: int = id
        self.name: str = name
        self.done: bool = done

"""Class to interface to the datebase."""
class Db:
    """Connects to the dataBase and obtains an cursor"""
    def __init__(self):
        self.connect = mysql.connect()
        self.cursor = self.connect.cursor()

    def commit_close(self):
        self.connect.commit()
        self.connect.close()

    def test_conn():
        try:
            conn = mysql.connect()
            conn.close()
            return True
        except:
            return False
        
        
    """Check if ID exists in the database."""
    def exists(self, id: int):
        select = """SELECT * FROM tasks WHERE ID=%s;"""
        result = self.cursor.execute(select, (id,))
        self.connect.commit()
        if result != 1:
            return False
        else:
            return True

    """RETURNS ALL THE ROWS FROM THE DB"""
    def read_all(self):
        self.cursor.execute('SELECT * FROM tasks;')
        data = self.cursor.fetchall()
        self.commit_close()
        formated = []
        for row in data:
            todo = Todo(*row)
            formated.append(todo.__dict__)
        return formated
    
    """Return one row of the table in thd DB."""
    def read_one(self, id: int):
        qry = """SELECT * FROM tasks WHERE ID=%s;"""
        data = self.cursor.execute(qry, (id))
        if data != 1:
            self.commit_close()
            return None
        task = self.cursor.fetchone()
        return Todo(*task).__dict__

    """SAVE NEW ToDO TO THE DB """
    def new_todo(self, taskName: str):
        qry = """INSERT INTO tasks (name) VALUES (%s);"""
        done = self.cursor.execute(qry, (taskName,))
        self.commit_close()
        return done


    """UPDATES THE NAME OF THE TASK IN THE DB"""
    def update_one(self, id: int, name: str):
        if not self.exists(id): 
            return None
        update = """UPDATE tasks SET name=%s WHERE id=%s;"""
        updated = self.cursor.execute(update, (name, id,))
        self.commit_close()
        return updated
    


    def delete_one(self, id: int):
        if not self.exists(id): return None
        dlt = """DELETE FROM tasks WHERE id=%s;"""
        delted = self.cursor.execute(dlt, (id,))
        self.commit_close()
        return delted
    

    def update_state(self, id: int, state:bool):
        if not self.exists(id):
            self.commit_close()
            return None
        update = """UPDATE tasks SET done=%s WHERE id=%s;"""
        updated = self.cursor.execute(update, (state, id))
        self.commit_close()
        return updated