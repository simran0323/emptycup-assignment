import sqlite3

def init_db():
    # Connect to SQLite database (creates the file if it doesn't exist)
    conn = sqlite3.connect('listings.db')
    cursor = conn.cursor()

    # Create the listings table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS listings (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            projects INTEGER NOT NULL,
            years INTEGER NOT NULL,
            price TEXT NOT NULL
        )
    ''')

    # Create the contacts table (for the contact numbers, since a listing can have multiple contacts)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            listing_id TEXT NOT NULL,
            phone TEXT NOT NULL,
            FOREIGN KEY (listing_id) REFERENCES listings (id)
        )
    ''')

    # Clear existing data (for idempotency)
    cursor.execute('DELETE FROM listings')
    cursor.execute('DELETE FROM contacts')

    # Insert sample data
    listings_data = [
        (
            "1",
            "Epic Designs",
            "Passionate team of 4 designers working out of Bangalore with an experience of 4 years.",
            57,
            8,
            "$$"
        ),
        (
            "2",
            "Studio - D3",
            "Passionate team of 4 designers working out of Bangalore with an experience of 4 years.",
            43,
            6,
            "$$$"
        )
    ]

    contacts_data = [
        ("1", "+91 - 984532853"),
        ("1", "+91 - 984532854"),
        ("2", "+91 - 984532853"),
        ("2", "+91 - 984532854")
    ]

    # Insert listings
    cursor.executemany('INSERT INTO listings (id, name, description, projects, years, price) VALUES (?, ?, ?, ?, ?, ?)', listings_data)

    # Insert contacts
    cursor.executemany('INSERT INTO contacts (listing_id, phone) VALUES (?, ?)', contacts_data)

    # Commit and close
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database initialized and populated with sample data.")