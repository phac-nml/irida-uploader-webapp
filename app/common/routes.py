from flask import Blueprint, render_template, request


main = Blueprint('main', __name__, url_prefix='')


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/clientside_table")
def clientside_table():
    return render_template("clientside_table.html")


@main.route("/run_table")
def run_table():
    # run = request.args.get('run', '')
    # print("run_table: " + run)
    return render_template("run_table.html")
