from flask import render_template, Blueprint

bp = Blueprint('gallery', __name__,template_folder='templates')

@bp.route('/gallery')
def gallery():
    return render_template('gallery.html')
