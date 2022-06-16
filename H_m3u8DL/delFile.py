from shutil import rmtree
import os

def del_file(temp_dir):
    """ 删除多余文件

    :param temp_dir: 文件路径
    :return:
    """
    if os.path.exists(temp_dir+'.mp4'):
        rmtree(rf'{temp_dir}', ignore_errors=True)