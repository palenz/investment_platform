# Here goes the mini apps for each section of the website. They will be created and then
# exported using the blueprint method.

from flask import Flask, Blueprint

company_blueprint = Blueprint("companies", __name__)