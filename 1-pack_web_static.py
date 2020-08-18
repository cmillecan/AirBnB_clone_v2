#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from web_static """
    local('mkdir -p versions')
    time = datetime.now()
    fname = """'versions/web_static_{}{}{}{}{}{}.tgz'.format(time.year,
           time.month, time.day, time.hour, time.minute, time.second)"""
    archive = local('tar -cvzf' + fname + 'web_static')
    if archive.failed:
        return None
    else:
        return fname
