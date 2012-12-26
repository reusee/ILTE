from PyQt4.QtCore import *
from PyQt4.QtGui import *

class CharView(QGraphicsView):
  def __init__(self, strokes, scale):
    super(CharView, self).__init__()

    self.setRenderHint(QPainter.Antialiasing)
    self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.setDragMode(self.NoDrag)

    scene = QGraphicsScene()
    self.setScene(scene)

    pen = QPen()
    pen.setCapStyle(Qt.RoundCap)
    pen.setJoinStyle(Qt.RoundJoin)
    pen.setWidth(5)

    for stroke in strokes:
      for p1, p2 in zip(stroke[:-1], stroke[1:]):
        scene.addLine(
            p1[0] * scale,
            p1[1] * scale,
            p2[0] * scale,
            p2[1] * scale,
            pen
            )
