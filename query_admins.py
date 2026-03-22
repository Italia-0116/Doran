import sqlite3
conn = sqlite3.connect('instance/doran.db')
c = conn.cursor()

# Check if admins table exists
c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='admins'")
table_exists = bool(c.fetchone())
print(f"Admins table exists: {table_exists}")

if table_exists:
    # Check admins data
    c.execute("SELECT id, email FROM admins")
    admins = c.fetchall()
    print(f"Admins found: {len(admins)}")
    for admin in admins:
        print(f"  ID: {admin[0]}, Email: {admin[1]}")
else:
    print("No admins table - run db.create_all() or check DB connection")

# Check users table too for completeness
c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
users_table = bool(c.fetchone())
print(f"Users table exists: {users_table}")

conn.close()
