#!/usr/bin/python3
"""
Deploys static to the web server
"""
from fabric.api import env, put, sudo
import os

env.hosts = ['54.242.192.138', '3.90.85.81']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not os.path.exists(archive_path):
        return False

    put(archive_path, '/tmp/')
    archive_filename = os.path.basename(archive_path)
    archive_folder = os.path.splittext(archive_filename)[0]

    sudo(f'tar -xzf /tmp/{archive_filename} -C /data/web_static/releases/')
    sudo(f'rm /tmp/{archive_filename}')
    sudo(f'rm -rf /data/web_static/current')
    sudo(f'ln -s /data/web_static/releases/{archive_folder} /data/web_static/current')

    return True
