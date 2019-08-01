import os
import datetime

from flask import abort, Flask, jsonify, request
from pizzacalendar import pizza_next

app = Flask(__name__)

def is_request_valid(request):
    is_token_valid = request.form['token'] == os.environ['SLACK_VERIFICATION_TOKEN']
    return is_token_valid

@app.route('/pizza-week', methods=['POST'])
def pizza_week():
    if not is_request_valid(request):
        abort(400)

    return jsonify(
        response_type='in_channel',
        text='Pizza!!'
    )