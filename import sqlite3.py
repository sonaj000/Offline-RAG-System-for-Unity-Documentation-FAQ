import sqlite3

database = sqlite3.connect("unreal_docs.db")
cursor = database.cursor()

# Create Classes table
cursor.execute("""
CREATE TABLE IF NOT EXISTS classes (
    class_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name TEXT NOT NULL,
    class_description TEXT,
    class_references TEXT,
    class_syntax TEXT, 
    url TEXT
)
""")

# Create Class Variables table
cursor.execute("""
CREATE TABLE IF NOT EXISTS class_variables (
    variable_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_id INTEGER NOT NULL,
    variable_name TEXT NOT NULL,
    variable_type TEXT,
    variable_description TEXT,
    url TEXT,
    FOREIGN KEY (class_id) REFERENCES classes (class_id)
)
""")

# Create Class Functions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS class_functions (
    function_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_id INTEGER NOT NULL,
    function_name TEXT NOT NULL,
    function_signature TEXT,
    function_description TEXT,
    url TEXT,
    FOREIGN KEY (class_id) REFERENCES classes (class_id)
)
""")

database.commit()