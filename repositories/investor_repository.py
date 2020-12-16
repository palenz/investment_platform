from db.run_sql import run_sql
from models.investor import Investor
from models.company import Company

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

def companies(investor):
    companies = []

    sql = "SELECT companies.* FROM companies INNER JOIN investments ON investments.company_id = companies.id WHERE investor_id = %s"
    values = [investor.id]
    results = run_sql(sql, values)

    for row in results:
        company = Company(row['name'], row['industry'], row['id'])
        companies.append(company)

    return companies

def delete_all():
    sql = 'DELETE FROM investors'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM investors WHERE id=%s'
    values = [id]
    run_sql(sql, values)

def count():
    number_of_investors = 0
    
    sql = 'SELECT * FROM investors'
    results = run_sql(sql)

    for row in results:
        number_of_investors += 1
    
    return number_of_investors
