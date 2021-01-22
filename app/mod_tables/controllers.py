from flask import Blueprint, jsonify, request
from app import table_builder, text_builder

from app.uploader import client


tables = Blueprint('tables', __name__, url_prefix='/tables')


@tables.route("/clientside_table", methods=['GET'])
def clientside_table_content():
    data = table_builder.collect_data_clientside()
    return jsonify(data)


@tables.route("/run_table", methods=['GET'])
def run_table_content():
    run_dir = request.args.get('run', '')
    print("run_table_content: " + run_dir)
    data = table_builder.collect_data_run(run_dir)
    return jsonify(data)


@tables.route("/run_sample_sheet", methods=['GET', 'POST'])
def run_sample_sheet():
    if request.method == 'GET':
        run_dir = request.args.get('run', '')
        print("run_sample_sheet: " + run_dir)
        data = text_builder.collect_sample_sheet(run_dir)
        print("text data")
        print(data)
        return jsonify(data)
    elif request.method == 'POST':
        run_dir = request.args.get('run', '')
        print("run_sample_sheet: " + run_dir)
        # todo should decode be checked somehow??
        sample_sheet_text = request.get_data().decode("utf-8")
        text_builder.write_sample_sheet(run_dir, sample_sheet_text)
        return jsonify(success=True)


@tables.route("/upload_run", methods=['POST'])
def upload_run():
    run_dir = request.args.get('run', '')
    print("run_sample_sheet: " + run_dir)
    client.upload_run(run_dir)
    return jsonify(success=True)


@tables.route("/continue_run", methods=['POST'])
def continue_run():
    run_dir = request.args.get('run', '')
    print("run_sample_sheet: " + run_dir)
    client.upload_run(run_dir=run_dir, continue_upload=True)
    return jsonify(success=True)
