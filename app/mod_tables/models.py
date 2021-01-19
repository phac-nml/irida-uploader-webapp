from app.uploader import parse

"""
example_data = [
    {'directory': 'my_run_dir', 'status': 'complete', 'message': ''},
    {'directory': 'my_run_dir2', 'status': 'invalid', 'message': 'missing whatever file'},
]
"""


class TableBuilder(object):

    @staticmethod
    def collect_data_clientside():
        data = parse.get_runs()
        return {'data': data}

    @staticmethod
    def collect_data_run(run_dir):
        print("collect_data_run: " + run_dir)
        data = parse.get_single_run(run_dir)
        return {'data': data}


class TextBuilder(object):

    @staticmethod
    def collect_sample_sheet(run_dir):
        print("collect_sample_sheet: " + run_dir)
        data = parse.get_sample_sheet(run_dir)
        return {'data': data}

    @staticmethod
    def write_sample_sheet(run_dir, data):
        parse.write_sample_sheet(run_dir, data)

