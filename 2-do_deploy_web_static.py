#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder and deploys it to web server
"""
from fabric.api import *
import os.path
import tarfile
from datetime import datetime


env.hosts = []
env.name = 'ubuntu'


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
    """
    Deploys archive to all web servers
    """
    if os.path.exists(archive_path) is False:
        return False

    try:
        archive_filename = archive_path.split('/')[-1]
        put(archive_path, '/tmp/')
        release_dir = '/data/web_static/releases/{}'.format(
            archive_filename.split('.')[0])
        run('mkdir -p {}').format(release_dir)
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_dir))
        run('rm /tmp/{}'.format(archive_filename))
        run('mv {}web_static/* {}'.format(release_dir, release_dir))
        run('rm -rf {}web_static'.format(release_dir))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(release_dir))
        return True
    except Exception:
        return False
