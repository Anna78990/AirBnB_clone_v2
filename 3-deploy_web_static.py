#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static """
from datetime import datetime
from fabric.api import run, put, env, local
from os.path import exists, isdir
env.hosts = ['34.148.155.116', '34.74.13.47']


def do_pack():
    """ generates a .tgz archive from the contents of the web_static """
    data = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = 'versions/web_static_{}.tgz'.format(data)
    try:
        if isdir("versions") is False:
            local('mkdir versions')
        local('tar -cvzf {} web_static'.format(filename))
        return filename
    except Error:
        return None

def do_deploy(archive_path):
    """ generates a .tgz archive from the contents of the web_static """
    if exists(archive_path) is False:
        return False

    try:
        filename = archive_path.split('/')[-1]
        sans_ext = filename.split('.')[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, sans_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(filename, path, sans_ext))
        run('rm /tmp/{}'.format(filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, sans_ext))
        run('rm -rf {}{}/web_static'.format(path, sans_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, sans_ext))
        print("New version deployed!")
        return True

    except Exception:
        return False

def deploy():
    """ creates and distributes an archive to your web servers """
    archive = do_pack()
    if archive is None:
        return False
    dep = do_deploy(archive)
    return dep
