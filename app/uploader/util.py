from app import config

import os
import time


monitor_directory = config.MONITOR_DIRECTORY


def fix_status_obj_list(data):
    fix_data = []
    for status_obj in data:
        fix_data.append(
            fix_status_obj_data(status_obj)
        )
    return fix_data


def fix_status_obj_data(status_obj):
    return {"directory": remove_prefix(status_obj.directory, monitor_directory),
            'status': status_obj.status,
            'message': status_obj.message}


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


# TODO: these helper functions need try catches
def get_full_run_dir(run_dir):
    return os.path.join(monitor_directory, run_dir)


def backup_sample_sheet(file_path):
    # timestamp = time.ctime(time.time())
    timestamp = time.strftime("%Y-%m-%d %H:%M")
    path, filename = os.path.split(file_path)
    filename = os.path.splitext(filename)[0] + "." + timestamp + ".csv"
    new_file_path = os.path.join(path, filename)
    print("backing up data directory:")
    print(new_file_path)
    os.rename(file_path, new_file_path)


def delete_file(file_path):
    os.remove(file_path)


def write_file(file_path, data):
    with open(file_path, 'w') as f:
        f.write(data)
