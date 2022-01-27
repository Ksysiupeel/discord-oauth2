from flask import jsonify

def page_not_found(e):
    return jsonify(
        {
            "msg": "Page does not exist!"
        }
    )