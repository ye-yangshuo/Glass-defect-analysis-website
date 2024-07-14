from flask import render_template, Blueprint

bp = Blueprint('analyze', __name__,template_folder='templates')

@bp.route('/analyze')
def gallery():
    return render_template('analyze.html')

