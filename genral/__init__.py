from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')

HOST = config.get('SSL', 'HOST', fallback=None)

USERNAME = config.get('SSL', 'USERNAME', fallback='root')

CERT_DIR_PATH = config.get(
    'SSL', 'CERT_DIR_PATH', fallback='/etc/letsencrypt/')

CLOUDFLARE = config.get('SSL', 'CLOUDFLARE', fallback=None)

if CLOUDFLARE:
    INI_FILE = f"cli-{CLOUDFLARE}.ini"
else:
    INI_FILE = None

REFER_DOMAIN = config.get('SSL', 'REFER_DOMAIN', fallback=None)

REFER_DOMAIN_NGINX_CONF_PATH = config.get(
    'SSL', 'REFER_DOMAIN_NGINX_CONF_PATH', fallback='/etc/nginx/conf.d/')

REFER_NGINX_CONF = config.get(
    'SSL', 'REFER_NGINX_CONF', fallback='refer.conf')

REFER_CLOUDFLARE_DOMAIN_DNS_RECORD_PATH = config.get(
    'SSL', 'REFER_CLOUDFLARE_DOMAIN_DNS_RECORD_PATH', fallback=f'{REFER_DOMAIN}.txt'
)

TARGET_DOMAIN = config.get(
    'SSL', 'TARGET_DOMAIN', fallback='domains.txt')

DOWNLOAD_CONF = config.getint('SSL', 'DOWNLOAD_CONF', fallback=0)

UPLOAD_CONF = config.getint('SSL', 'UPLOAD_CONF', fallback=0)

CREATE_CONF = config.getint('SSL', 'CREATE_CONF', fallback=0)

DOMAIN_DNS_RECORD = config.getint('SSL', 'CREATE_CONF', fallback=0)
