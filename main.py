import os
from googletrans import Translator

def translate_text(text, src='en', dest='zh-tw'):
    translator = Translator()
    result = translator.translate(text, src=src, dest=dest)
    return result.text

def translate_rpy_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    translated_lines = []
    for line in lines:
        if line.strip().startswith('"') and line.strip().endswith('"'):
            text_to_translate = line.strip().strip('"')
            translated_text = translate_text(text_to_translate)
            translated_line = line.replace(text_to_translate, translated_text)
            translated_lines.append(translated_line)
        else:
            translated_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(translated_lines)

def translate_all_rpy_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.rpy'):
                file_path = os.path.join(root, file)
                print(f'Translating {file_path}')
                translate_rpy_file(file_path)

if __name__ == '__main__':
    directory = 'F:\\VM_VB_Share_Folder\\CorruptedKingdoms-0.21.7-pc\\game\\script'
    translate_all_rpy_files(directory)
