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

    if not pizza_date:
        pizza_message = "Couldn't find the next pizza day...either @hmandviwala forgot to update the calendar, or the Pizzapocalypse is upon us. Either way, good luck and keep it cheesy!"
    elif pizza_date:
        pizza_date = pizza_date.strftime("%Y-%m-%d")
        now = datetime.now().strftime("%Y-%m-%d")
        if pizza_date == now:
            pizza_message = "It is Pizza Wednesday my dudes!!"
        else:
            pizza_message = "The next pizza day is on " + pizza_date.strftime("%Y-%m-%d") + ". 'til then, keep it cheesy!"

    return jsonify(
        response_type='in_channel',
        text=pizza_message
    )