from iridauploader.core import upload as uploader

from app.uploader import util


def upload_run(run_dir, continue_upload=False):
    print('uploading run with continue=' + str(continue_upload))
    full_run_dir = util.get_full_run_dir(run_dir)
    # Use force when not doing a continue upload, and vice versa
    uploader.upload_run_single_entry(
        directory=full_run_dir,
        force_upload= not continue_upload,
        continue_upload=continue_upload
    )
