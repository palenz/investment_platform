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

@investors_blueprint.route("/investors/<id>/delete", methods=['POST'])
def delete_investor(id):
    investor_repository.delete(id)
    return redirect('/investors')

@investors_blueprint.route("/investors/new", methods=['GET'])
def new_investor():
    return render_template("investors/new.html")

@investors_blueprint.route("/investors", methods=['POST'])
def create_investr():
    investor_name = request.form['name']
    investor_email = request.form['email']
    
    investor = Investor(investor_name, investor_email)
    investor_repository.save(investor)

    return redirect('/investors')