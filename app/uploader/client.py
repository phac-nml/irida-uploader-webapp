from iridauploader.core import upload as uploader

from app.uploader import util


def upload_run(run_dir):
    full_run_dir = util.get_full_run_dir(run_dir)
    uploader.upload_run_single_entry(full_run_dir, True)
