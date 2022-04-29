#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static """
from datetime import datetime
from fabric.api import run, local
from os.path import isdir


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
