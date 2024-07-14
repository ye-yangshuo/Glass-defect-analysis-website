import os
import math

from app.config import *


IMAGES_PER_PAGE = 20

def get_image_list(page):
    all_images = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    total_pages = math.ceil(len(all_images) / IMAGES_PER_PAGE)
    start_index = (page - 1) * IMAGES_PER_PAGE
    end_index = start_index + IMAGES_PER_PAGE
    current_page_images = all_images[start_index:end_index]
    
    return {
        "images": current_page_images,
        "page": page,
        "total_pages": total_pages,
        "total_images": len(all_images)
    }

def get_image_file(image_name):
    image_path = os.path.join(IMAGE_FOLDER, image_name)
    if os.path.exists(image_path):
        return image_path
    return None

def delete_image(image_name):
    image_path = os.path.join(IMAGE_FOLDER, image_name)
    txt_file_path = os.path.join(LABEL_FOLDER, os.path.splitext(image_name)[0] + '.txt')
    image_deleted = False
    txt_deleted = False

    if os.path.exists(image_path):
        os.remove(image_path)
        image_deleted = True

    if os.path.exists(txt_file_path):
        os.remove(txt_file_path)
        txt_deleted = True

    return image_deleted, txt_deleted