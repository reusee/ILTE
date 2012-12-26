#!/usr/bin/env python

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from sexp import parse
import sys
from char_view import CharView
import math
from flowlayout import FlowLayout

DEFAULT_TRAINING_SET_FILE = 'jp.train'
CHAR_WIDTH = 300
CHAR_HEIGHT = 300
CHAR_VIEW_WIDTH = 150

class Manager(QWidget):
  def __init__(self):
    super(Manager, self).__init__()

    # layout
    self.layout = QVBoxLayout()
    self.setLayout(self.layout)

    # training set viewer
    self.trainning_set_view = QWidget()
    self.training_set_view_layout = QVBoxLayout()
    self.trainning_set_view.setLayout(self.training_set_view_layout)

    scrollarea = QScrollArea()
    scrollarea.setWidgetResizable(True)
    scrollarea.setEnabled(True)

    scrollarea.setWidget(self.trainning_set_view)
    self.layout.addWidget(scrollarea)

    self.char_views = []
    self.view_layouts = []
    self.view_widgets = []

    # load training set
    self.training_set = {}
    self.parse_training_set(DEFAULT_TRAINING_SET_FILE)

    self.view_training_set()

  def parse_training_set(self, filename):
    with open(filename, 'r') as f:
      data = parse(f.read())
      for entry in data:
        if len(entry) != 5: continue
        _, value, width, height, strokes = entry
        value = value[1]
        width = width[1]
        height = height[1]
        strokes = strokes[1:]
        if width != CHAR_WIDTH or height != CHAR_HEIGHT:
          pass #TODO scale
        self.training_set.setdefault(value, [])
        self.training_set[value].append(strokes)

  def view_training_set(self):
    column_per_row = self.width() / CHAR_VIEW_WIDTH
    for key in sorted(self.training_set.keys()):
      layout = FlowLayout()
      self.view_layouts.append(layout)
      c_count = len(self.training_set[key])
      widget = QWidget()
      self.view_widgets.append(widget)
      widget.setLayout(layout)
      self.training_set_view_layout.addWidget(widget)
      for i, strokes in enumerate(self.training_set[key]):
        char_view = CharView(strokes, (CHAR_VIEW_WIDTH - 10) / float(CHAR_WIDTH))
        self.char_views.append(char_view)
        char_view.setFixedSize(CHAR_VIEW_WIDTH, CHAR_VIEW_WIDTH)
        layout.addWidget(char_view)

def main():
  app = QApplication(sys.argv)
  manager = Manager()
  manager.show()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()
