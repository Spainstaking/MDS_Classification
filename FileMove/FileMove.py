'''
@File    : FileMove.py
@Time    : 2019/12/14 
@Author  : SureY
'''

import os
import shutil


def windows_to_linux(path):
    return path.replace('\\', '/')


# 当前文件夹下的 同一‘归类’的文档，合并到同一文件夹下
def similiar_move(file_path, key_list):
    file_names = os.listdir(file_path)
    src_path = file_path
    for key in key_list:
        dst_path = windows_to_linux(src_path + '\\' + key)
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)  # 如果path存在，python会报错无法创建文件夹
        # 该文件夹的文件（除文件夹）
        names = [name for name in os.listdir(file_path)
                 if os.path.isfile(os.path.join(file_path, name))]
        for fname in names:
            src_file = windows_to_linux(src_path + '\\' + fname)
            dst_file = windows_to_linux(dst_path + '\\' + fname)
            if key in fname:
                shutil.move(src_file, dst_file)

if __name__ == '__main__':
    file_path = r'E:\hznu1009_Sure\PycharmTest\MDS-past\PPI_PCCS_edge'
    key_list = ['BRCA', 'COAD', 'HNSC', 'KIRC', 'LUAD', 'LUSC', 'THCA', 'UCEC', 'READ', 'SKCM']
    similiar_move(file_path, key_list)