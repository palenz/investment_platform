from db.run_sql import run_sql
from models.company import Company
from models.investor import Investor

def save(company):
    sql = 'INSERT INTO companies (name, industry) VALUES (%s, %s) RETURNING id'
    values = [company.name, company.industry]
    results = run_sql (sql, values)
    company.id = results[0]['id']
    return company

def select_all():
    companies = []

    sql = 'SELECT * FROM companies'
    results = run_sql(sql)

    for row in results:
        company = Company(row['name'], row['industry'], row['id'])
        companies.append(company)
    
    return companies

def select(id):
    company = None
    sql = 'SELECT * FROM companies WHERE id=%s'
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        company = Company(result['name'], result['industry'], result['id'])
    
    return company

def investors(company):
    investors = []
    sql = 'SELECT investors.* FROM investors INNER JOIN investments ON investments.investor_id = investors.id WHERE company_id = %s'
    values = [company.id]
    results = run_sql(sql, values)

    for row in results:
        investor = Investor(row['name'], row['email'], row['id'])
        investors.append(investor)

    return investors

def delete_all():
    sql = 'DELETE FROM companies'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM companies WHERE id=%s'
    values = [id]
    run_sql(sql, values)