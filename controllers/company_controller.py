# Here goes the mini apps for each section of the website. They will be created and then
# exported using the blueprint method.

from flask import Flask, Blueprint, render_template, request, redirect
from models.company import Company
import repositories.company_repository as company_repository
import repositories.investment_repository as investment_repository

companies_blueprint = Blueprint("companies", __name__)

@companies_blueprint.route("/companies")
def companies():
    companies = company_repository.select_all()
    # company_valuation = investment_repository.valuation()
    return render_template("companies/index.html", companies = companies)

@companies_blueprint.route("/companies/<id>")
def show(id):
    company = company_repository.select(id)
    investors = company_repository.investors(company)
    valuations = company_repository.investments(id)
    # company_valuation = investment_repository.valuation()
    return render_template("companies/show.html", company=company, investors=investors, valuations=valuations)

@companies_blueprint.route("/companies/<id>/delete", methods=['POST'])
def delete_company(id):
    company_repository.delete(id)
    return redirect('/companies')

@companies_blueprint.route("/companies/new", methods=['GET'])
def new_investment():
    return render_template("companies/new.html")

@companies_blueprint.route("/companies", methods=['POST'])
def create_company():
    company_name = request.form['name']
    company_industry = request.form['industry']
    
    company = Company(company_name, company_industry)
    company_repository.save(company)

    return redirect('/companies')