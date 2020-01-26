'''
@File    : logging_output.py
@Time    : 2019/12/13 
@Author  : SureY
'''
import logging
' Output log to file and console '


# Define a Handler and set a format which output to file

logging.basicConfig(
    level=logging.DEBUG,  # 定义输出到文件的log级别，大于此级别(DEBUG)的都被输出
    format='%(asctime)s----%(filename)s : %(levelname)s  %(message)s',  # 定义输出log的格式
    datefmt='%Y-%m-%d %A %H:%M:%S',  # 时间
    filename='B2.log',  # log文件名
    filemode='w')  # 写入模式“w”或“a”
# Define a Handler and set a format which output to console
console = logging.StreamHandler()  # 定义console handler
console.setLevel(logging.INFO)  # 定义该handler级别
formatter = logging.Formatter('%(asctime)s-%(filename)s : %(levelname)s  %(message)s')  # 定义该handler格式
console.setFormatter(formatter)  # 告诉handler使用这个格式
# Create an instance
logging.getLogger().addHandler(console)  # 实例化添加handler
