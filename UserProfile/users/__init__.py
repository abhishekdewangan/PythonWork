from flask import Blueprint

blueprint1 = Blueprint('users',__name__)

@blueprint1.route('/admin')
def admin():
    return 'Hello World'
