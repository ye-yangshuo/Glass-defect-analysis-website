from flask import Blueprint, jsonify, request, send_file
from app.services.labels_service import *
from flask_cors import *


bp = Blueprint('labels', __name__, url_prefix='/api')

@bp.route('/labels/bar_chart', methods=['GET'])
def get_labels_bar_chart():
    year = request.args.get('year')
    month = request.args.get('month')
    files = get_label_files(year, month)
    label_counts = count_labels(files)
    filename = f"bar_chart_{year}_{month}.png"
    create_bar_chart(label_counts, filename)
    return jsonify({"filename": filename})

@bp.route('/labels/pie_chart', methods=['GET'])
def get_labels_pie_chart():
    year = request.args.get('year')
    month = request.args.get('month')
    files = get_label_files(year, month)
    defect_count, no_defect_count = count_defects(files)
    filename = f"pie_chart_{year}_{month}.png"
    create_pie_chart(defect_count, no_defect_count, filename)
    return jsonify({"filename": filename})

@bp.route('/labels/show_image/<filename>', methods=['GET'])
def show_image(filename):
    return send_file(os.path.join(CHART_FOLDER, filename), mimetype='image/png')