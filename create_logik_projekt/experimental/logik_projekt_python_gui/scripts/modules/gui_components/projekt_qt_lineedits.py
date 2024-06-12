'''
# -------------------------------------------------------------------------- #

# File Name:        projekt_qt_lineedits.py
# Version:          1.0.0
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-06-07
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program is part of LOGIK-PROJEKT.
#                   LOGIK-PROJEKT is a library of custom functions and
#                   modules for autodesk flame.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #
'''

# ========================================================================== #
# This section defines the import staements.
# ========================================================================== #

from PySide6.QtWidgets import QLineEdit

# ========================================================================== #
# This section defines the main functions.
# ========================================================================== #

'''
def create_lineedit():
    lineedit = QLineEdit()
    # Set placeholder text if needed
    # lineedit.setPlaceholderText("Enter text here")
    # Set text if needed
    # lineedit.setText("Enter text here")
    return lineedit
'''

def create_serial_id_lineedit():
    lineedit = QLineEdit()
    lineedit.setPlaceholderText("Enter the Serial Number")
    # lineedit.setText("Enter the Serial Number")
    return lineedit

def create_client_name_lineedit():
    lineedit = QLineEdit()
    lineedit.setPlaceholderText("Enter the name of the Client")
    # lineedit.setText("Enter the name of the Client")
    return lineedit

def create_campaign_name_lineedit():
    lineedit = QLineEdit()
    lineedit.setPlaceholderText("Enter the name of the Campaign")
    # lineedit.setText("Enter the name of the Campaign")
    return lineedit

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #
'''
# -------------------------------------------------------------------------- #

# Disclaimer:       This program is part of LOGIK-PROJEKT.
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
# -------------------------------------------------------------------------- #
'''
# -------------------------------------------------------------------------- #
# Changelist:       
# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2024-06-07 - 16:22:45
# comments:              Working program
