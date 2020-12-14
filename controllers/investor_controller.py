from flask import Flask, Blueprint, render_template, request, redirect
from models.investor import Investor
import repositories.investor_repository as investor_repository

investors_blueprint = Blueprint("investors", __name__)

@investors_blueprint.route("/investors")
def investors():
    investors = investor_repository.select_all()
    return render_template("investors/index.html", investors=investors)

@investors_blueprint.route("/investors/<id>")
def show(id):
    investor = investor_repository.select(id)
    companies = investor_repository.companies(investor)
    return render_template("investors/show.html", investor=investor, companies=companies)