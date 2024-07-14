from flask import render_template, Blueprint

bp = Blueprint('auth', __name__,template_folder='templates')

@bp.route('/auth')
def authentic():
    return render_template('autnentic.html')
