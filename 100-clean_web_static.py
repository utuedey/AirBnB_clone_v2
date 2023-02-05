#!/usr/bin/python3
""""""
from fabric.api import *

from os import path

from datetime import datetime



n = datetime.now()



env.hosts = ['34.74.140.171', '	3.95.67.118']

def do_pack():
    """"""
    fn = 'versions/web_static_{}{}{}{}{}{}.tgz'\

        .format(n.year, n.month, n.day, n.hour, n.minute, n.second)

    local('mkdir -p versions')

    command = local("tar -cvzf " + fn + " ./web_static/")

    if command.succeeded:

        return fn

    return None

def do_deploy(archive_path):
    """Deploys the static files to the host server"""
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    ret_output = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed')
        ret_output = True
    except Exception:
    ret_output = False
    return ret_output

def deploy():
    """ """
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False


def do_clean(number=0):
    """deletes out-of-date archives"""
    archives = os.listdir('versions/')
    archives.sort(reverse=True)
    start = int(number)
    if not start:
        start += 1
    if start < len(archives):
        archives = archives[start:]
    else:
        archives = []
    for archive in archives:
        os.unlink('versions/{}'.format(archive))
    cmd_parts = [
        "rm -rf $(",
        "find /data/web_static/releases/ -maxdepth 1 -type d -iregex",
        " '/data/web_static/releases/web_static_.*'",
        " | sort -r | tr '\\n' ' ' | cut -d ' ' -f{}-)".format(start + 1)
    ]
    run(''.join(cmd_parts))
