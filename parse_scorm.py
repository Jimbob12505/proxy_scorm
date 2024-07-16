import zipfile
import os 

def extract_scorm_package(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)


extract_scorm_package("source/Effective Communication Skills.zip", "output")