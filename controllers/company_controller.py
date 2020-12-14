# Here goes the mini apps for each section of the website. They will be created and then
# exported using the blueprint method.

from flask import Flask, Blueprint, render_template, request, redirect
from models.company import Company
import repositories.company_repository as company_repository

companies_blueprint = Blueprint("companies", __name__)

@companies_blueprint.route("/companies")
def companies():
    companies = company_repository.select_all() # adds a new company
    return render_template("companies/index.html", companies = companies)

@companies_blueprint.route("/companies/<id>")
def show(id):
    company = company_repository.select(id)
    investors = company_repository.investors(company)
    return render_template("companies/show.html", company=company, investors=investors)