import os
from datetime import datetime
import matplotlib.pyplot as plt

from app.config import *



# Ensure CHART_FOLDER exists
os.makedirs(CHART_FOLDER, exist_ok=True)

# Mapping of category IDs to specific names
CATEGORY_MAPPING = {
    '0': 'White spots',
    '1': 'Chips',
    '2': 'Scratches',
    '3': 'Stains'
}



def get_label_files(year=None, month=None):
    files = os.listdir(LABEL_FOLDER)
    filtered_files = []
    for file in files:
        if file.endswith('.txt'):
            file_date = datetime.strptime(file.split('.')[0], '%Y%m%d%H%M%S')
            if year and file_date.year != int(year):
                continue
            if month and file_date.month != int(month):
                continue
            filtered_files.append(file)
    return filtered_files

def count_labels(files):
    label_counts = {name: 0 for name in CATEGORY_MAPPING.values()}
    for file in files:
        with open(os.path.join(LABEL_FOLDER, file), 'r') as f:
            lines = f.readlines()
            for line in lines:
                label = line.split()[0]  
                label_name = CATEGORY_MAPPING.get(label, 'Unknown')
                if label_name in label_counts:
                    label_counts[label_name] += 1
                else:
                    label_counts[label_name] = 1
    return label_counts

import matplotlib.pyplot as plt
import os

def create_bar_chart(label_counts, filename):
    labels = list(label_counts.keys())
    counts = list(label_counts.values())
    total_count = sum(counts)
    
    # 创建一个颜色列表，每个条形一个颜色
    colors = ['blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'cyan']
    if len(labels) > len(colors):
        colors *= (len(labels) // len(colors)) + 1

    plt.figure(figsize=(10, 6))
    plt.bar(labels, counts, color=colors[:len(labels)])  # 使用颜色列表
    plt.xlabel('Defects')
    plt.ylabel('Counts')
    plt.title(f'Category Count Statistics (Total: {total_count})')

    for i, v in enumerate(counts):
        plt.text(i, v + 0.5, str(v), ha='center', va='bottom')

    filepath = os.path.join(CHART_FOLDER, filename)
    plt.savefig(filepath, format='png')
    plt.close()


def count_defects(files):
    defect_count = 0
    no_defect_count = 0
    for file in files:
        with open(os.path.join(LABEL_FOLDER, file), 'r') as f:
            lines = f.readlines()
            if lines:
                defect_count += 1
            else:
                no_defect_count += 1
    return defect_count, no_defect_count

def create_pie_chart(defect_count, no_defect_count, filename):
    labels = ['Defective', 'Non-Defective']
    sizes = [defect_count, no_defect_count]
    colors = ['red', 'green']
    explode = (0.1, 0)  # only "explode" the 1st slice (i.e. 'Defective')
    total_count = defect_count + no_defect_count

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=140)
    plt.title(f'Defect Proportion (Total: {total_count})')

    filepath = os.path.join(CHART_FOLDER, filename)
    plt.savefig(filepath, format='png')
    plt.close()



