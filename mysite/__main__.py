import subprocess
import os
from django_sorcery.db.url import get_settings


def main():

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    print('main', get_settings('default'))
    cmd = ['py', 'alchemy.py']
    subprocess.run(cmd)


if __name__ == '__main__':
    main()
