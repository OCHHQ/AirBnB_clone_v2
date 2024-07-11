#!/usr/bin/env python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static folder
"""
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Packs the web_static content into a .tgz file"""
    now = datetime.now()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)
    local("mkdir -p versions")
    result = local("tar -cvzf versions/{} web_static".format(archive_name))
    if result.failed:
        return None
    else:
        return os.path.abspath("versions/{}".format(archive_name))
