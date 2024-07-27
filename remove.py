import os

def delete_rpyc_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.rpyc'):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f'Deleted {file_path}')

if __name__ == '__main__':
    directory = 'F:\\VM_VB_Share_Folder\\CorruptedKingdoms-0.21.7-pc\\game\\script'
    delete_rpyc_files(directory)
