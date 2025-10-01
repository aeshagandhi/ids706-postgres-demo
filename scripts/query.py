
import os
import psycopg2
from dotenv import load_dotenv

# Load .env if present (does nothing if file not found)
load_dotenv()

DB_NAME = os.getenv("DB_NAME", os.getenv("PGDATABASE", "duke_restaurants"))
DB_USER = os.getenv("DB_USER", os.getenv("PGUSER", "vscode"))
DB_PASSWORD = os.getenv("DB_PASSWORD", os.getenv("PGPASSWORD", "vscode"))
# In devcontainer, host is 'db'; on your laptop use 'localhost'
DB_HOST = os.getenv("DB_HOST", os.getenv("PGHOST", "localhost"))
DB_PORT = os.getenv("DB_PORT", os.getenv("PGPORT", "5432"))


cur = conn.cursor()

# Define search parameters
min_rating = 4.0

# Execute search query
cur.execute("""
    SELECT name, address, rating, cuisine, avg_cost
    FROM restaurants
    WHERE rating >= %s
    ORDER BY rating DESC;
""", (min_rating,))

# Fetch and convert results to DataFrame

rows = cur.fetchall()
df = pd.DataFrame(rows, columns=['name', 'address', 'rating', 'cuisine', 'avg_cost'])

# Group by cuisine and calculate average cost
avg_cost_by_cuisine = df.groupby('cuisine')['avg_cost'].mean().reset_index()

# Create a bar chart of average cost by cuisine
fig = px.bar(avg_cost_by_cuisine, x='cuisine', y='avg_cost',
             title='Average Cost by Cuisine (Rating ≥ 4.0)',
             labels={'avg_cost': 'Average Cost', 'cuisine': 'Cuisine'})

# Save the plot as HTML file (just to make it interactive)
fig.write_html('avg_cost_by_cuisine.html')

# Close the connection
cur.close()
conn.close()



# import os
# import psycopg2
# from dotenv import load_dotenv

# # Load .env if present (does nothing if file not found)
# load_dotenv()

# DB_NAME = os.getenv("DB_NAME", os.getenv("PGDATABASE", "duke_restaurants"))
# DB_USER = os.getenv("DB_USER", os.getenv("PGUSER", "vscode"))
# DB_PASSWORD = os.getenv("DB_PASSWORD", os.getenv("PGPASSWORD", "vscode"))
# # In devcontainer, host is 'db'; on your laptop use 'localhost'
# DB_HOST = os.getenv("DB_HOST", os.getenv("PGHOST", "localhost"))
# DB_PORT = os.getenv("DB_PORT", os.getenv("PGPORT", "5432"))

# def main():
#     print(f"Connecting to {DB_NAME} at {DB_HOST}:{DB_PORT} as {DB_USER} ...")
#     conn = psycopg2.connect(
#         dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
#     )
#     cur = conn.cursor()

#     print("\nTop rated places:")
#     cur.execute("""
#         SELECT name, rating
#         FROM restaurants
#         ORDER BY rating DESC, name ASC;
#     """)
#     for row in cur.fetchall():
#         print(row)

#     print("\nInserting a new restaurant...")
#     cur.execute("""
#         INSERT INTO restaurants (name, address, distance_miles, rating, cuisine, avg_cost, personal_rank)
#         VALUES (%s, %s, %s, %s, %s, %s, %s)
#         RETURNING id, name;
#     """, ("Queeny's", "321 E Chapel Hill St, Durham, NC", 1.5, 4.3, "American", 22.00, 7))
#     print("Inserted:", cur.fetchone())

#     print("\nUpdating rating for NuvoTaco...")
#     cur.execute("""
#         UPDATE restaurants
#         SET rating = rating + 0.1
#         WHERE name = %s
#         RETURNING name, rating;
#     """, ("NuvoTaco",))
#     print("Updated:", cur.fetchone())

#     print("\nDeleting lowest-rated place...")
#     cur.execute("""
#         DELETE FROM restaurants
#         WHERE id = (
#           SELECT id FROM restaurants
#           ORDER BY rating ASC, id ASC
#           LIMIT 1
#         )
#         RETURNING id, name, rating;
#     """)
#     print("Deleted:", cur.fetchone())

#     conn.commit()
#     cur.close()
#     conn.close()
#     print("\nDone.")

# if __name__ == "__main__":
#     main()

