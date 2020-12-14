from db.run_sql import run_sql
from models.investor import Investor


def save(investor):
    sql = 'INSERT INTO investors (name, email) VALUES (%s, %s) RETURNING id'
    values = [investor.name, investor.email]
    results = run_sql (sql, values)
    investor.id = results[0]['id']
    return investor

def select_all():
    investors = []

    sql = 'SELECT * FROM investors'
    results = run_sql(sql)

    for row in results:
        investor = Investor(row['name'], row['email'], row['id'])
        investors.append(investor)
    
    return investors

def select(id):
    investor = None
    sql = 'SELECT * FROM investors WHERE id=%s'
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        investor = Investor(result['name'], result['email'], result['id'])
    
    return investor

def delete_all():
    sql = 'DELETE FROM investors'
    run_sql(sql)