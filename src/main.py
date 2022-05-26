import sys

from PyQt5.QtWidgets import QApplication

from view.main import AppWindow

def main():
  app = QApplication(sys.argv)
  window = AppWindow()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()
