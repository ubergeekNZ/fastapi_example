import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

db = 'chinook.db'

def run_query(q):
    with sqlite3.connect(db) as conn:
        return pd.read_sql(q,conn)

def run_command(c):
    with sqlite3.connect(db) as conn:
        conn.isolation_level = None
        conn.execute(c) 

def show_tables():
    q = '''
        SELECT
            name,
            type
        FROM sqlite_master
        WHERE type IN ("table","view");
        '''
    return run_query(q)

show_tables()

albums_to_purchase = '''
WITH 
    usa_tracks_sold AS
        (
         SELECT il.* FROM invoice_line il
         INNER JOIN invoice i ON il.invoice_id = i.invoice_id
         INNER JOIN customer c ON i.customer_id = c.customer_id
         WHERE c.country = "USA" 
        )
SELECT 
    g.name Genre, 
    COUNT(uts.invoice_line_id) "Number of Tracks Sold", 
    CAST(COUNT(uts.invoice_line_id) AS FLOAT)/(SELECT COUNT(*) FROM usa_tracks_sold) "Percentage of Tracks Sold"
FROM usa_tracks_sold uts
INNER JOIN track t ON uts.track_id = t.track_id
INNER JOIN genre g ON t.genre_id = g.genre_id
GROUP BY 1 
ORDER BY 2 DESC
LIMIT 10;
'''

run_query(albums_to_purchase)

genre_sales_usa = run_query(albums_to_purchase)
genre_sales_usa.set_index('Genre', drop=True, inplace=True)
genre_sales_usa.sort_values('Number of Tracks Sold', inplace=True)
genre_sales_usa['Number of Tracks Sold'].plot.barh(
        title="Top Selling Genres in the USA",
        xlim=(0, 625),
        colormap=plt.cm.Accent
)

plt.ylabel('')

for i, label in enumerate(list(genre_sales_usa.index)):
    score = genre_sales_usa.loc[label, "Number of Tracks Sold"]
    label = (genre_sales_usa.loc[label, "Percentage of Tracks Sold"] * 100
            ).astype(int).astype(str) + "%"
    plt.annotate(str(label), (score + 10, i - 0.15))

plt.show()