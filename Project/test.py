from PyQt5 import QtWidgets, uic, 
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog, QWidget
import sys
import re

email_patern = re.compile(r"[^@]+@[^@]+\.[^@.]+")

class 