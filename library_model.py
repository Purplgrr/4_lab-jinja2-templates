import pandas as pd

def get_book(conn, begin_date, end_date):
    return pd.read_sql(f'''
        SELECT
            title AS Название,
            genre_name AS Жанр,
            publisher_name AS Название_издательства,
            available_numbers AS Количество_доступных_книг
        FROM book
            JOIN genre ON genre.genre_id=book.genre_id
            JOIN publisher USING (publisher_id)
        WHERE book_id NOT IN (
            SELECT 
                book_id
            FROM 
                book_reader
            WHERE 
                borrow_date BETWEEN {begin_date} AND {end_date}
        )
    ''',
    conn
    )