import re
import os
import traceback


def create_certbot_command(command=None, *options, **args):
    '''生成certbot指令
    command 增加參數
    args 輸入有值參數 範例:c=["config.ini"]
    option 選項 範例: --dns-cloudflare
    '''
    if command == None:
        command = "certbot "

    for option in options:
        command += f"{option} "

    for key, values in args.items():
        for value in values:
            if len(key) > 1:
                command += f"--{key} {value} "
            else:
                command += f"-{key} {value} "
    return command


def create_file_with_refer(domain, refer_domain, refer_file_path, extension=None, result_dir='result/'):
    '''根據參照檔案建立新檔案 將refer_domain替換domain
    file_ex: 輸出檔案副檔名 預設為參照檔案
    '''
    # 建立輸出資料夾
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    # 取得副檔名
    if extension == None:
        extension = os.path.splitext(refer_file_path)[1]

    # 讀取參照檔案
    with open(refer_file_path, 'r') as f:
        content = f.read()

    # 建立輸出檔案 並更改內容
    result_path = f"{result_dir}/{domain}{extension}"
    with open(result_path, "w") as f:
        new_content = re.sub(refer_domain, domain, content)
        f.write(new_content)
    
    return os.path.abspath(result_path)


def ssh_to_host_input_command():
    pass


def scp_to_host(file_path, username, host, host_path, remove_file=False):
    '''scp到目的主機的資料夾'''
    try:
        command = f"scp {file_path} {username}@{host}:{host_path}"
        print(command)
        os.system(command)
        if remove_file:
            os.remove(file_path)
    except:
        traceback.print_exc()


def scp_to_local(path, username, host, host_path):
    '''scp目的主機到本地位置'''
    try:
        command = f"scp {username}@{host}:{host_path} {path}"
        print(command)
        os.system(command)
    except:
        traceback.print_exc()
