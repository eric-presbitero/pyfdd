
import sys
import os
import warnings

from PyQt5 import QtCore, QtGui, QtWidgets, uic
# from PySide2 import QtCore, QtGui, QtWidgets, uic

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT #as NavigationToolbar
from matplotlib.widgets import RectangleSelector
from pyfdd.core.datapattern.plot_widgets import AngleMeasurement
import matplotlib.pyplot as plt  # do not use pyplot
import matplotlib as mpl
import seaborn as sns
import numpy as np

import pyfdd

# Load the ui created with PyQt creator
# First, convert .ui file to .py with,
# pyuic5 datapattern_widget.ui -o datapattern_widget.py
# import with absolute import locations
from pyfdd.gui.qt_designer.simexplorer_widget import Ui_SimExplorerWidget
from pyfdd.gui.datapattern_interface import DataPatternControler
import pyfdd.gui.config as config


class SimExplorer_window(QtWidgets.QMainWindow):
    """ Class to use the data pattern widget in a separate window"""
    def __init__(self, *args, **kwargs):
        super(SimExplorer_window, self).__init__(*args, **kwargs)

        # Load configuration
        if config.parser is None:
            config.filename = 'simexplorer_config.ini'
            config.read()

        # Setup the window
        self.setWindowTitle("Simulations Explorer")
        self.statusBar()

        # Set a DataPattern widget as central widget
        dp_w = SimExplorer_widget(mainwindow=self)
        self.setCentralWidget(dp_w)
        self.resize(1150, 670)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        config.write()


class SimExplorer_widget(QtWidgets.QWidget, Ui_SimExplorerWidget):
    """ Data pattern widget class"""

    simlibrary_opened = QtCore.pyqtSignal()

    def __init__(self, *args, mainwindow=None, **kwargs):
        """
        Init method for the data pattern widget
        :param args:
        :param mainwindow: Main window object
        :param kwargs:
        """

        super(SimExplorer_widget, self).__init__(*args, **kwargs)

        # Alternative way to load the ui created with PyQt creator
        # uic.loadUi('qt_designer/datapattern_widget.ui', self)

        self.setupUi(self)
        self.mainwindow = mainwindow

        # Set config section
        if not config.parser.has_section('simexplorer'):
            config.parser.add_section('simexplorer')

        # set the mpl widget background colour
        self.mplwindow.setStyleSheet('background: palette(window);')

        # Instantiate datapattern controler
        self.dpcontroler = DataPatternControler(parent_widget=self)#, mpl_layout=self.mplvl, infotext_box=None)
        self.mainwindow = mainwindow
        self.mpl_layout = self.mplvl
        self.dpcontroler.set_widgets_and_layouts(mpl_layout=self.mplvl, mainwindow=self.mainwindow)
        self.dpcontroler.percentiles = [0, 1]  # Force [0, 1] percentiles

        # Create a menubar entry for the datapattern
        self.menubar = self.mainwindow.menuBar()
        self.dp_menu = self.setup_menu()

        # Variables
        self.simlib = None
        self.current_row = None
        self.simlib_filename = ''

        # Connect signals
        # List
        self.simlist.itemSelectionChanged.connect(self.update_datapattern)

        # Pattern visualization
        self.pb_colorscale.clicked.connect(self.dpcontroler.call_pb_colorscale)
        self.pb_setlabels.clicked.connect(self.dpcontroler.call_pb_setlabels)

    def setup_menu(self):
        dp_menu = self.menubar.addMenu('&Sim. Library')

        # Open 2dl
        open_act = QtWidgets.QAction('&Open', self)
        open_act.setStatusTip('Open a .2dl simulations file')
        open_act.triggered.connect(self.open_2dl_call)
        dp_menu.addAction(open_act)

        # Separate input from output
        dp_menu.addSeparator()

        # Export pattern matrix
        export_act = QtWidgets.QAction('&Export pattern', self)
        export_act.setStatusTip('Export as an .txt .csv or .2db file')
        export_act.triggered.connect(self.dpcontroler.export_dp_call)
        dp_menu.addAction(export_act)

        # Save as image
        saveimage_act = QtWidgets.QAction('&Save Image', self)
        saveimage_act.setStatusTip('Save pattern as an image')
        saveimage_act.triggered.connect(self.dpcontroler.saveasimage_dp_call)
        dp_menu.addAction(saveimage_act)

        # Copy to clipboard
        copy_act = QtWidgets.QAction('&Copy to clipboard', self)
        copy_act.setStatusTip('Copy simulation image to clipboard')
        copy_act.triggered.connect(self.dpcontroler.call_copy_to_clipboard)
        dp_menu.addAction(copy_act)

        return dp_menu

    def open_2dl_call(self):
        """
        Open a 2dl library file
        :return:
        """

        open_path = '' if not config.parser.has_option('simexplorer', 'open_path') else \
            config.get('simexplorer', 'open_path')

        lib_path = QtWidgets.QFileDialog.getOpenFileName(self,
                                                         'Open .2dl library',
                                                         directory=open_path,
                                                         filter='library (*.2dl)',
                                                         options=QtWidgets.QFileDialog.DontUseNativeDialog)
        if lib_path == ('', ''):  # Cancel
            return

        try:
            self.simlib = pyfdd.Lib2dl(lib_path[0])
        except:
            QtWidgets.QMessageBox.warning(self.parent_widget, 'Warning message',
                                          'Error while opening the library file.')
        else:
            # update info text, simlist and datapattern
            self.update_infotext()
            self.update_simlist()
            self.update_datapattern()
            self.simlib_filename = lib_path[0]

            # Emit opened signal
            self.simlibrary_opened.emit()

            # update config
            open_path = os.path.dirname(lib_path[0])
            config.parser['simexplorer']['open_path'] = open_path

    def get_simlibrary(self):
        if self.simlib is not None:
            return self.simlib.copy()
        else:
            return None

    def update_infotext(self):
        if self.infotext is None:
            warnings.warn('Info text box is not set')
            return

        base_text = 'Pattern dimentions (nx, ny): {:d}, {:d}\n' \
                    'Angular step (x, y): {:.2f}, {:.2f}\n' \
                    'Angular range (x, y): {:.2f}, {:.2f}\n' \
                    'Number of simulations: {:d}'
        dict_2dl = self.simlib.dict_2dl
        nx, ny = self.simlib.nx_mirror, self.simlib.ny_mirror
        xstep, ystep = self.simlib.xstep, self.simlib.ystep
        xfirst, yfirst = self.simlib.xfirst, self.simlib.yfirst
        xlast, ylast = self.simlib.xlast, self.simlib.ylast
        xrange = xlast - xfirst
        yrange = ylast - yfirst
        num_sim = len(dict_2dl['Spectrums'])

        text = base_text.format(nx, ny, xstep, ystep, xrange, yrange, num_sim)

        self.infotext.setText(text)

    def update_simlist(self):
        # Disconnect signal to make changes and reconnect after.
        self.simlist.itemSelectionChanged.disconnect()
        self.simlist.clear()

        # Set up table columns
        column_labels = ["Number", "Description", "Factor", "u1", "Sigma"]
        self.simlist.setColumnCount(len(column_labels))
        self.simlist.setHorizontalHeaderLabels(column_labels)
        self.lib2dl_sim_list = self.simlib.get_simulations_list()
        num_rows = len(self.lib2dl_sim_list)

        # Set the number of rows in the table
        self.simlist.setRowCount(num_rows)

        for row, line in enumerate(self.lib2dl_sim_list):
            # Create table items and set their values
            items = []
            for column, value in enumerate(line):
                item = QtWidgets.QTableWidgetItem(str(value).strip())
                items.append(item)
                self.simlist.setItem(row, column, item)

            # Adjust column widths to content
            self.simlist.resizeColumnsToContents()

        # Set selection behavior to select entire rows
        #self.simlist.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.current_row = 1
        self.simlist.setCurrentCell(self.current_row - 1, 0)
        self.simlist.itemSelectionChanged.connect(self.update_datapattern)

    def update_datapattern(self):
        self.current_row = self.simlist.currentRow() + 1
        self.dpcontroler.set_datapattern(self.simlib.get_simulation_patt_as_dp(self.current_row))


def main():
    app = QtWidgets.QApplication(sys.argv)
    # window = DataPattern_widget()
    window = SimExplorer_window()
    window.show()
    print(window.size())
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
