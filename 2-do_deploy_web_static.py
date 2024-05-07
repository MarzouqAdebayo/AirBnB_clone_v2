#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder and deploys it to web server
"""
from fabric.api import *
import os.path
import tarfile
from datetime import datetime


env.hosts = ['54.242.192.138', '3.90.85.81']
env.user = 'ubuntu'

def do_pack():
    """
    Generates a .tgz file
    """
    local("mkdir -p versions")
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = f'web_static_{timestamp}.tgz'
    archive_path = os.path.join('versions', archive_name)
    local(f'tar -czf {archive_path} web_static/')

    if os.path.exists(archive_path):
        return archive_path
    else:
        return None


def do_deploy(archive_path):
    """ function distrubtes an archive to my web servers
    """
    path_existence = os.path.exists(archive_path)
    if path_existence is False:
        return False
    try:
        path_split = archive_path.replace('/', ' ').replace('.', ' ').split()
        just_directory = path_split[0]
        no_tgz_name = path_split[1]
        full_filename = path_split[1] + '.' + path_split[2]
        folder = '/data/web_static/releases/{}/'.format(no_tgz_name)
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(folder))
        run('tar -xzf /tmp/{} -C {}'.format(full_filename, folder))
        run('rm /tmp/{}'.format(full_filename))
        run('mv {}web_static/* {}'.format(folder, folder))
        run('rm -rf {}web_static'.format(folder))
        current = '/data/web_static/current'
        run('rm -rf {}'.format(current))
        run('ln -s {} {}'.format(folder, current))
        print("New version deployed!")
        return True
    except Exception:
        return False
