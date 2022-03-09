import os
from genral.function import scp_to_host, scp_to_local
from genral.function import create_certbot_command
from genral.function import create_file_with_refer
from genral import HOST, USERNAME, INI_FILE
from genral import REFER_DOMAIN_NGINX_CONF_PATH, REFER_DOMAIN
from genral import TARGET_DOMAIN, REFER_NGINX_CONF
from genral import DOWNLOAD_CONF, UPLOAD_CONF, CREATE_CONF, DOMAIN_DNS_RECORD
from genral import REFER_CLOUDFLARE_DOMAIN_DNS_RECORD_PATH, SHOW_CERTBOT_COMMAND

# 確認TARGET_DOMAIN存在
if not os.path.exists(TARGET_DOMAIN):
    print(f"請輸入域名在{TARGET_DOMAIN}，多個域名請分行")
    with open(TARGET_DOMAIN, 'w') as f:
        pass
elif HOST == None:
    print('請在設定檔填寫 HOST')
elif REFER_DOMAIN == None:
    print('請在設定檔填寫 REFER_DOMAIN')
elif DOMAIN_DNS_RECORD and not os.path.exists(REFER_CLOUDFLARE_DOMAIN_DNS_RECORD_PATH):
    print(f'{REFER_CLOUDFLARE_DOMAIN_DNS_RECORD_PATH} 不存在')
else:
    # 讀取目標域名
    with open(TARGET_DOMAIN, 'r') as f:
        domains = f.read().splitlines()

    for domain in domains:
        # 建立指令
        if SHOW_CERTBOT_COMMAND:

            if INI_FILE:
                command = create_certbot_command(None, c=[INI_FILE])

            command = create_certbot_command(
                command,
                "certonly --dns-cloudflare",
                "--no-autorenew",
                d=[f"{domain}", f"*.{domain}"]
            )

            print(command)

        # 建立指向紀錄上傳文檔
        if DOMAIN_DNS_RECORD:
            create_file_with_refer(
                domain,
                REFER_DOMAIN,
                REFER_CLOUDFLARE_DOMAIN_DNS_RECORD_PATH,
                result_dir='result/cloudflare'
            )

        # 建立每個域名的nginx.conf檔案
        if CREATE_CONF:

            # 下載參照域名 並 建立 refer.conf
            if DOWNLOAD_CONF:
                scp_to_local(
                    REFER_NGINX_CONF,
                    USERNAME,
                    HOST,
                    f"{REFER_DOMAIN_NGINX_CONF_PATH}/{REFER_DOMAIN}.conf"
                )

            file_path = create_file_with_refer(
                domain,
                REFER_DOMAIN,
                REFER_NGINX_CONF,
                result_dir='result/nginx'
            )

        # 傳送nginx 各個域名的conf 到主機
        if not CREATE_CONF:
            file_path = os.path.abspath(f"result/nginx/{domain}.conf")

        if UPLOAD_CONF:
            scp_to_host(
                file_path,
                USERNAME,
                HOST,
                REFER_DOMAIN_NGINX_CONF_PATH
            )
