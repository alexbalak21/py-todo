from flaskext.mysql import MySQL
from app import app


mysql = MySQL()
mysql.init_app(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'test'


class Todo:
    def __init__(self, id: int, name: str, done: bool):
        self.id: int = id
        self.name: str = name
        self.done: bool = done


class Db:
    # def __init__(self):
    #     self.connect = mysql.connect()
    #     self.cursor = self.connect.cursor()

    def test_conn():
        try:
            conn = mysql.connect()
            conn.close()
            return True
        except:
            return False

    def exists(id: int):
        connect = mysql.connect()
        cursor = connect.cursor()
        select = """SELECT * FROM tasks WHERE ID=%s;"""
        result = cursor.execute(select, (id,))
        connect.commit()
        connect.close()
        if result != 1:
            return False
        else:
            return True

    """RETURNS ALL THE TODOS FROM THE DB"""
    def read_all():
        connect = mysql.connect()
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM tasks;')
        data = cursor.fetchall()
        connect.commit()
        connect.close()
        formated = []
        for row in data:
            todo = Todo(*row)
            formated.append(todo.__dict__)
        return formated

    def read_one(id: int):
        qry = """SELECT * FROM tasks WHERE ID=%s;"""
        connect = mysql.connect()
        cursor = connect.cursor()
        data = cursor.execute(qry, (id))
        if data != 1:
            connect.close()
            return None
        task = cursor.fetchone()
        return Todo(*task).__dict__

    """SAVE ToDo TO THE DB """
    def new_todo(taskName: str):
        qry = """INSERT INTO tasks (name) VALUES (%s);"""
        connect = mysql.connect()
        cursor = connect.cursor()
        done = cursor.execute(qry, (taskName,))
        connect.commit()
        connect.close()
        return done

    def update_one(id: int, name: str):
        connect = mysql.connect()
        cursor = connect.cursor()
        select = """SELECT * FROM tasks WHERE ID=%s;"""
        update = """UPDATE tasks SET name=%s WHERE id=%s;"""
        exists = cursor.execute(select, (id,))
        connect.commit()
        if exists != 1:
            connect.close()
            return None
        updated = cursor.execute(update, (name, id))
        connect.commit()
        connect.close()
        return updated

    def delete_one(id: int):
        connect = mysql.connect()
        cursor = connect.cursor()
        dlt = """DELETE FROM tasks WHERE id=%s;"""
        select = """SELECT * FROM tasks WHERE ID=%s;"""
        exists = cursor.execute(select, (id,))
        connect.commit()
        if exists != 1:
            connect.close()
            return None
        delted = cursor.execute(dlt, (id,))
        connect.commit()
        connect.close()
        return delted

    def update_state(id: int):
        return
