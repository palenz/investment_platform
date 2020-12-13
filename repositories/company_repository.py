from db.run_sql import run_sql
from models.company import Company
from models.investor import Investor

def save(company):
    sql = 'INSERT INTO companies (name, industry) VALUES (%s, %s) RETURNING id'
    values = [company.name, company.industry]
    results = run_sql (sql, values)
    company.id = results[0]['id']
    return company


