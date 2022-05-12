#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static """
from datetime import datetime
from fabric.api import run, put, env
from os.path import exists
env.hosts = ['34.148.155.116', '34.74.13.47']


def do_deploy(archive_path):
    """ generates a .tgz archive from the contents of the web_static """
    if exists(archive_path) is False:
        return False

    try:
        filename = archive_path.split('/')[-1]
        sans_ext = filename.split('.')[0]
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}/'.format(sans_ext))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(filename, sans_ext))
        run('rm /tmp/{}'.format(filename))
        run('mv /data/web_static/releases/{0}/web_static/* /data/web_static/releases/{0}/'.format(sans_ext))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(sans_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(sans_ext))
        print("New version deployed!")
        return True

    except Exception:
        return False
