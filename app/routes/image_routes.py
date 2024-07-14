from flask import Blueprint, jsonify, request, send_file
from app.services.image_service import *



bp = Blueprint('images', __name__, url_prefix='/api')

@bp.route('/images', methods=['GET'])
def get_images():
    page = int(request.args.get('page', 1))
    return jsonify(get_image_list(page))

@bp.route('/image/<image_name>', methods=['GET'])
def get_image(image_name):
    image_path = get_image_file(image_name)
    if image_path:
        return send_file(image_path, mimetype='image/png')
    else:
        return jsonify({"error": "Image not found"}), 404

@bp.route('/image/<image_name>', methods=['DELETE'])
def delete_image_route(image_name):
    image_deleted, txt_deleted = delete_image(image_name)
    
    if image_deleted and txt_deleted:
        return jsonify({"message": "Image and corresponding text file deleted successfully"}), 200
    elif image_deleted:
        return jsonify({"message": "Image deleted successfully, but no corresponding text file found"}), 200
    elif txt_deleted:
        return jsonify({"message": "Text file deleted successfully, but no corresponding image found"}), 200
    else:
        return jsonify({"error": "Image and corresponding text file not found"}), 404