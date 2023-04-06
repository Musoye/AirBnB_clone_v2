#!/usr/bin/python3
"""using Fabric to generate archive"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """The function to configure the archive"""
    local("mkdir versions")
    pat = "versions/web_static_{}.tgz".format(
           datetime.strftime(datetime.now(), "%Y%m%d%H%M%s"))
    result = local("tar -czvf {} web_static".format(pat))
    if (result.failed):
        return (None)
    else:
        return (pat)
