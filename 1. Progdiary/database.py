import sqlite3

connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row # anables to have named access to row fields

def create_table():
    with connection:  # automatically commits after executing commands
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")


def add_entry(entry_content, entry_date):
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES (?,?);", (entry_content, entry_date)
        )


def get_entries():
    cursor = connection.execute("SELECT * FROM entries;")

    # makes the same as command above
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM entries;")

    return cursor # gives coursor to the data. Possible to iterate on it. Result is array of tuples

