#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your
AirBnB Clone repo, using
the function do_pack."""

from datetime import datetime
from fabric.api import local


def do_pack():
    """generate a .tgz archive from the contents of the web_static
    folder"""

    local("mkdir -p versions")

    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(time_stamp)

    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.failed:
        return None
    else:
        return archive_path
