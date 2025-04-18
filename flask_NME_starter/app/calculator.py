from flask import (
    Blueprint, render_template, request, redirect, g, flash
)
from app.model import solve_linprog
from app.db import get_db
import sqlite3

bp = Blueprint("calculator", __name__)

@bp.route("/addition", methods = ("GET", "POST"))
def addition():
    #TODO

@bp.route("/history")
def history():
    #TODO
    


