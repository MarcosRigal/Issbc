#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Jan 18 11:29:53 2014

@author: acalvo
"""

import sys
from PyQt5 import QtWidgets
import ckVtsClasificacion as vts

app =  QtWidgets.QApplication(sys.argv)
form = vts.ClasificacionDlg()
sys.exit(app.exec_())



