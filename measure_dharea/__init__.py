# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AreaHeight
                                 A QGIS plugin
 measure area and delta H
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-06-06
        copyright            : (C) 2024 by Adam Lostowski
        email                : 01179174@pw.edu.pl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load AreaHeight class from file AreaHeight.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .measure_dharea import AreaHeight
    return AreaHeight(iface)
