#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder and deploys it to web server
"""
from fabric.api import *
import os.path
import tarfile
from datetime import datetime


env.hosts = ['54.90.56.152', '18.208.120.166']
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
    """Distributes an archive to your web servers."""
    if not os.path.exists(archive_path):
        return False

    archive_filename = os.path.basename(archive_path)
    archive_name_without_ext = archive_filename.split('.')[0]

    put(archive_path, f'/tmp/')

    release_dir = f"/data/web_static/releases/{archive_name_without_ext}"
    run(f'mkdir -p {release_dir}')
    run(f'tar -xzf /tmp/{archive_filename} -C {release_dir}/')

    run(f'rm /tmp/{archive_filename}')
    # Move uncompressed file's content
    run(f'mv {release_dir}/web_static/* {release_dir}/')
    # Remove uncompressed folder
    run(f'rm -rf {release_dir}/web_static/')
    # Remove old symlink
    run('rm -rf /data/web_static/current')
    # Create new symlink
    run(f'ln -s {release_dir}/ /data/web_static/current')

    return True
