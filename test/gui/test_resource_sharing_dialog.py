# coding=utf-8
"""Dialog test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'akbargumbira@gmail.com'
__date__ = '2016-05-29'
__copyright__ = 'Copyright 2016, Akbar Gumbira'


from qgis.testing import start_app, unittest
import nose2

from PyQt4.QtGui import QDialogButtonBox, QDialog

from resource_sharing.gui.resource_sharing_dialog import ResourceSharingDialog


class QgsSymbologySharingDialogTest(unittest.TestCase):
    """Test dialog works."""
    @classmethod
    def setUpClass(cls):
        start_app()

    def setUp(self):
        """Runs before each test."""
        self.dialog = ResourceSharingDialog(None)

    def tearDown(self):
        """Runs after each test."""
        self.dialog = None

    def test_dialog_help(self):
        """Test we can click Help."""
        button = self.dialog.button_box.button(QDialogButtonBox.Help)
        button.click()
        result = self.dialog.result()
        # For now Rejected as we don't have any action for the help button
        self.assertEqual(result, QDialog.Rejected)

    def test_dialog_close(self):
        """Test we can click Close."""
        button = self.dialog.button_box.button(QDialogButtonBox.Close)
        button.click()
        result = self.dialog.result()
        self.assertEqual(result, QDialog.Rejected)

if __name__ == "__main__":
    nose2.main()