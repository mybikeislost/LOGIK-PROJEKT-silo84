#

# -------------------------------------------------------------------------- #

# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 man-made-mekanyzms
                
#                   LOGIK-PROJEKT creates directories, files, scripts & tools
#                   for use with Autodesk Flame and other software.

#                   LOGIK-PROJEKT is free software.

#                   You can redistribute it and/or modify it under the terms
#                   of the GNU General Public License as published by the
#                   Free Software Foundation, either version 3 of the License,
#                   or any later version.
 
#                   This program is distributed in the hope that it will be
#                   useful, but WITHOUT ANY WARRANTY; without even the
#                   implied warranty of MERCHANTABILITY or FITNESS FOR A
#                   PARTICULAR PURPOSE.

#                   See the GNU General Public License for more details.

#                   You should have received a copy of the GNU General
#                   Public License along with this program.

#                   If not, see <https://www.gnu.org/licenses/>.
                
#                   Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #

# File Name:        sync_editorial_tree_premiere.py
# Version:          0.0.1
# Created:          2024-10-31
# Modified:         2024-10-31

# ========================================================================== #
# This section defines the import statements and directory paths.
# ========================================================================== #

# Standard library imports
import argparse
import ast
import base64
import collections
import datetime
import getpass
import grp
import importlib
import io
import json
import os
import platform
import re
import shutil
import socket
import subprocess
import sys
import unittest
import xml

# -------------------------------------------------------------------------- #

def get_base_path():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    else:
        return os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '..', '..', '..'
            )
        )
    
# -------------------------------------------------------------------------- #

def get_resource_path(relative_path):
    base_path = get_base_path()
    return os.path.join(
        base_path,
        relative_path
    )

# -------------------------------------------------------------------------- #

# Set the path to the 'modules' directory
modules_dir = get_resource_path('modules')
# Set the path to the 'resources' directory
resources_dir = get_resource_path('resources')
# Append the modules path to the system path
if modules_dir not in sys.path:
    sys.path.append(modules_dir)

# ========================================================================== #
# This section defines third party imports.
# ========================================================================== #

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines environment specific variables.
# ========================================================================== #

# These paths should be passed from the main app.
the_hostname = "delta"
the_projekt_os = "Linux"
the_software_version = "flame_2025.1.pr199"
the_sanitized_version = "2025_1"
the_framestore = "stonefs"

'''
Print the variables for debugging
print(f"  Debug: the_hostname:              {the_hostname}")
print(f"  Debug: the_projekt_os:            {the_projekt_os}")
print(f"  Debug: the_software_version:      {the_software_version}")
print(f"  Debug: the_sanitized_version:     {the_sanitized_version}")
'''

# ========================================================================== #
# This section defines common paths.
# ========================================================================== #

projekt_roots_config_path = os.path.join(
    resources_dir,
    'cfg',
    'projekt_configuration',
    'roots',
    'projekt_roots.json'
)

# Read the JSON configuration file
try:
    with open(projekt_roots_config_path, 'r') as config_file:
        config = json.load(config_file)
except Exception as e:
    print(f"  Error reading JSON configuration file: {e}")
    config = {}

# Define common directory paths
the_projekts_dir = config.get(
    'the_projekts_dir',
    "/PROJEKTS"
)

the_projekt_flame_dirs = config.get(
    'the_projekt_flame_dirs',
    "/opt/Autodesk/project"
)

the_adsk_dir = config.get(
    'the_adsk_dir',
    "/opt/Autodesk"
)

the_adsk_dir_linux = config.get(
    'the_adsk_dir_linux',
    "/opt/Autodesk"
)

the_adsk_dir_macos = config.get(
    'the_adsk_dir_macos',
    "/Applications/Autodesk"
)

'''
Print the variables for debugging
print(f"  Debug: projekt_roots_config_path: {projekt_roots_config_path}")
print(f"  Debug: the_projekts_dir:          {the_projekts_dir}")
print(f"  Debug: the_projekt_flame_dirs:    {the_projekt_flame_dirs}")
print(f"  Debug: the_adsk_dir:              {the_adsk_dir}")
print(f"  Debug: the_adsk_dir_linux:        {the_adsk_dir_linux}")
print(f"  Debug: the_adsk_dir_macos:        {the_adsk_dir_macos}")
'''

# ========================================================================== #
# This section defines projekt specific paths.
# ========================================================================== #

# These paths should be passed from the main app.
the_projekt_name = "8888_new_job"
the_projekt_flame_name = f"{the_projekt_name}_{the_sanitized_version}_{the_hostname}"

separator = '# ' + '-' * 75 + ' #'

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #
