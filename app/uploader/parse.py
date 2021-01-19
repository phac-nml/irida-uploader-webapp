from app import config
from app.uploader import util

import iridauploader.core.parsing_handler as parsing_handler

monitor_directory = config.MONITOR_DIRECTORY


def get_runs():
    data = parsing_handler.get_run_status_list(monitor_directory)
    return util.fix_status_obj_list(data)


def get_single_run(run_dir):
    full_run_dir = util.get_full_run_dir(run_dir)
    data = parsing_handler.get_run_status(full_run_dir)
    return [util.fix_status_obj_data(data)]


def get_sample_sheet(run_dir):
    full_run_dir = util.get_full_run_dir(run_dir)
    sample_sheet_path = parsing_handler.get_parser_from_config().get_sample_sheet(full_run_dir)
    f = open(sample_sheet_path, "r")
    lines = "".join(f.readlines())
    print("lines:")
    print(lines)
    return lines


def write_sample_sheet(run_dir, data):
    full_run_dir = util.get_full_run_dir(run_dir)
    sample_sheet_path = parsing_handler.get_parser_from_config().get_sample_sheet(full_run_dir)
    print("sample_sheet_path:")
    print(sample_sheet_path)
    print("creating sample sheet backup")
    util.backup_sample_sheet(sample_sheet_path)
    print("writing")
    util.write_file(sample_sheet_path, data)
