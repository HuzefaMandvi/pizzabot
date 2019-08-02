import os
from datetime import datetime
from flask import abort, Flask, jsonify, request
from pizzacalendar import get_pizza_date

app = Flask(__name__)

def is_request_valid(request):
    is_token_valid = request.form['token'] == os.environ['SLACK_VERIFICATION_TOKEN']
    return is_token_valid

@app.route('/pizza-next', methods=['POST'])
def pizza_week():
    if not is_request_valid(request):
        abort(400)

    pizza_date = get_pizza_date()
    now = datetime.now()

    pizza_message = "The next pizza day is on " + pizza_date.strftime("%Y-%m-%d") + ". 'til then, keep it cheesy!"

    return jsonify(
        response_type='in_channel',
        text=pizza_message
    )