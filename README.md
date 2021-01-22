# IRIDA-Uploader-WebApp

This application is a flask app that runs the irida uploader to monitor a directory containing sequencing runs.

## This project is in a work in progress state


### Planned Features
* View list of sequencing runs
  * Can see Status and Error messages at a glance
* View and edit the SampleSheet file for a run
  * Creates a backup timestamped SampleSheet when making changes
* Upload a run
* Continue a stalled upload

### Development Road Map (Everything is a work in progress)
* View runs [DONE]
* See status and errors easily [DONE]
* View sample sheets [DONE]
* Edit sample sheets [DONE]
* Create backups of sample sheets when edited [DONE]
* Add uploading functionality [DONE]
* Get Continue Upload feature working [DONE]
* Add a way to refresh page when an upload finishes, to show the user that it is in fact done.
    * would this need to be async?
    * Could we have the route that runs the upload only return on completion of the python function?
* Add security layer
* Make it not ugly
* Add error catching and general code cleanup
* Have it build sensibly (setup.py / Makefile)
* Make it pretty

To setup:
```bash
# make a new venv
python3 -m venv .virtualenv
source .virtualenv/bin/activate
# Go copy the requirements.txt file from irida-uploader
pip install -r requirements.txt
# install test branch of uploader
pip install -i https://test.pypi.org/simple/ iridauploader==0.6.0
# install flask
pip install flask
```

edit `app/config.py` to match your monitor directory and uploader config file

To run:
```bash
export FLASK_APP=app/
flask run
```

Flask primer https://flask.palletsprojects.com/en/1.1.x/quickstart/

## Legal


Copyright Government of Canada 2021

Written by: National Microbiology Laboratory, Public Health Agency of Canada

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this work except in compliance with the License. You may obtain a copy of the
License at:

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.


## Contact

**Gary van Domselaar**: gary.vandomselaar@phac-aspc.gc.ca
