from .matching import MentorMentee
from .csv_utils import extract_dict
from .csv_utils import write_results

import os

from flask import Flask, request, render_template, send_file
from flask.ext.scss import Scss

app = Flask(__name__)

Scss(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    '''
    # this is to verify that folder to upload to exists.
    if os.path.isdir(os.path.join(APP_ROOT, 'files/{}'.format(folder_name))):
        print("folder exist")
    '''
    target = os.path.join(APP_ROOT, 'files/')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist("file"))

    mentee_file = request.files.getlist("file")[0]
    print(mentee_file)
    print("{} is the file name".format(mentee_file.filename))
    filename = mentee_file.filename
    # This is to verify files are supported
    ext = os.path.splitext(filename)[1]
    if (ext == ".csv"):
        print("File supported moving on...")
    else:
        render_template("Error.html", message="Files uploaded are not supported...")
    mentee_destination = "/".join([target, filename])
    print("Accept incoming file:", filename)
    print("Save it to:", mentee_destination)
    mentee_file.save(mentee_destination)

    mentor_file = request.files.getlist("file")[1]
    print(mentor_file)
    print("{} is the file name".format(mentor_file.filename))
    filename = mentor_file.filename
    # This is to verify files are supported
    ext = os.path.splitext(filename)[1]
    if (ext == ".csv"):
        print("File supported moving on...")
    else:
        render_template("Error.html", message="Files uploaded are not supported...")
    mentor_destination = "/".join([target, filename])
    print("Accept incoming file:", filename)
    print("Save it to:", mentor_destination)
    mentor_file.save(mentor_destination)

    menteeDict, mentorDict, capDict = extract_dict(mentee_destination, mentor_destination)
    game = MentorMentee.create_from_dictionaries(menteeDict, mentorDict, capDict)
    res_data = game.solve()
    write_results(res_data, "result_test")

    csv_path = "files/result_test.csv"
    return send_file(csv_path, as_attachment=True, attachment_filename="matching_results.csv")

if __name__ == "__main__":
    app.run(port=4555, debug=True)