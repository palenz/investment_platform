# This class will be the bridge between companies and investors. When an investor invests in
# a company, a new investment object is created and an entry in the investment table is
# saved. When we look up the investments that one investor has made, or the investments that
# one company has received, we will be reading the investment table.

from db.run_sql import run_sql
from models.investment import Investment
from models.company import Company
from models.investor import Investor
import pdb

import repositories.investor_repository as investor_repository
import repositories.company_repository as company_repository

def save(investment):
    # pdb.set_trace()
    sql = 'INSERT INTO investments (investor_id, company_id, equity, payment, date_of_investment) VALUES (%s, %s, %s, %s, %s) RETURNING id'
    values = [investment.investor.id, investment.company.id, float(investment.equity), investment.payment, investment.date_of_investment]
    results = run_sql (sql, values)
    investment.id = results[0]['id']
    return investment

def select_all():
    investments = []

    sql = 'SELECT * FROM investments'
    results = run_sql(sql)

    for row in results:
        investor = investor_repository.select(row['investor_id'])
        company = company_repository.select(row['company_id'])
        investment = Investment(investor, company, row['equity'], row['payment'], row['date_of_investment'], row['id'])
        investments.append(investment)
    
    return investments

def delete_all():
    sql = 'DELETE FROM investments'
    run_sql(sql)

def investor(investment):
    sql = 'SELECT * FROM investors WHERE id = %s'
    values = [investment.investor.id]
    results = run_sql(sql, values)[0]
    investor = Investor(results['name'], results['email'], results['id'])
    return investor

def company(investment):
    sql = 'SELECT * FROM companies WHERE id = %s'
    values = [investment.company.id]
    results = run_sql(sql, values)[0]
    company = Company(results['name'], results['industry'], results['id'])
    return company

def delete(id):
    sql = 'DELETE FROM investments WHERE id=%s'
    values = [id]
    run_sql(sql, values)

def total_invested():
    total_invested = 0
    sql ='SELECT * FROM investments'

    results = run_sql(sql)

    for row in results:
        total_invested += row['payment']

    return total_invested