import os
import subprocess


def get_pids(name):
    try:
        pids = subprocess.check_output(['pidof', name]).split()
        return list(map(int, pids))
    except:
        return []

def webpack_dev_server():
    already_running = False
    processes = get_pids('node')
    if processes:
        psax = subprocess.check_output(['ps', 'ax']).split(b'\n')
        for line in psax:
            if already_running: break
            for p in processes:
                if already_running: break
                p = str(p)
                line = line.decode('utf-8')
                line = line.strip()
                if p == line[:len(p)]:
                    if 'webpack-dev-server' in line:
                        already_running = True
    if not already_running:
        from django.conf import settings
        if settings.DEBUG and not bool(os.environ.get('WEBPACK_RUNNING')):
            os.environ['WEBPACK_RUNNING'] = 'True'
            subprocess.Popen(['npm', 'run', 'dev'])
