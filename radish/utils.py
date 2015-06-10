# -*- coding: utf-8 -*-

"""
    This module provides several utility functions
"""

import os
import re
import fnmatch


from radish.terrain import world


def console_write(text):
    """
        Writes the given text to the console

        If the --no-colors flag is given all colors are removed from the text
    """
    if world.config.no_ansi:
        text = re.sub(r"\x1b[^m]*m", "", text)

    print(text)


def expandpath(path):
    """
        Expands a path

        :param string path: the path to expand
    """
    return os.path.expanduser(os.path.expandvars(path))


def recursive_glob(root, pattern):
    matches = []
    for root, dirnames, filenames in os.walk(root):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    return matches


def get_debugger():
    """
        Returns a debugger instance
    """
    try:
        from IPython.core.debugger import Pdb
        pdb = Pdb()
    except ImportError:
        try:
            from IPython.Debugger import Pdb
            from IPython.Shell import IPShell

            IPShell(argv=[""])
            pdb = Pdb()
        except ImportError:
            import pdb

    return pdb


def datetime_to_str(datetime):
    """
        Returns the datetime object in a defined human readable format.

        :param Datetime datetime: the datetime object
    """
    if not datetime:
        return ""

    return datetime.strftime("%Y-%m-%dT%H:%M:%S")