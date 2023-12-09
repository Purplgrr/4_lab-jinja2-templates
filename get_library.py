from jinja2  import Environment, FileSystemLoader
from sqlite3 import connect
from library_model import get_book

begin_date = "2020-01-01"
end_date = "2020-12-31"

conn = connect('library.sqlite')

with open('library.db', 'r', encoding='utf-8-sig') as dump:
    db_dump = dump.read()

conn.executescript(db_dump)

df_book = get_book(conn, begin_date, end_date)

conn.close()

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

result_html = template.render(
    df_request=df_book,
    begin_date=begin_date,
    end_date=end_date,
)

with open('result1.html', 'w', encoding ='utf-8-sig') as res:
    print(result_html, file=res)