"""
Insta485 utility.

URLs include:
/uploads/<filename>
"""
import flask
import insta485


@insta485.app.route('/uploads/<filename>')
def download_file(filename):
    return flask.send_from_directory(
        insta485.app.config['UPLOAD_FOLDER'], filename, as_attachment=True
    )
