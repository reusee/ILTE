from PyQt4.QtCore import *
from PyQt4.QtGui import *
from dp import simplify_points
import zinnia
import random
from rules import *
import math

class Result:
  def __init__(self, score, value):
    self.score = score
    self.value = value

class Canvas(QGraphicsView):
  BRUSH_SIZE = 50
  CHAR_WIDTH = 300
  CHAR_HEIGHT = 300
  MINIMUM_PRESSURE = 0.005
  MIDDLE_RATIO = math.tan(math.pi / 12)

  def __init__(self):
    super(Canvas, self).__init__()
    self.scene = QGraphicsScene()
    self.setScene(self.scene)

    self.setRenderHint(QPainter.Antialiasing)
    self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.setDragMode(self.NoDrag)
    self.setSceneRect(0, 0, 1, 1)

    self.pen = QPen(QColor(0, 144, 192, 128))
    self.pen.setCapStyle(Qt.RoundCap)
    self.pen.setJoinStyle(Qt.RoundJoin)
    self.pen.setWidth(10)

    self.helper_pen = QPen(QColor(255, 0, 0, 64))
    self.helper_pen.setCapStyle(Qt.RoundCap)
    self.helper_pen.setJoinStyle(Qt.RoundJoin)
    self.helper_pen.setWidth(10)

    self.recognizer = zinnia.Recognizer()
    self.recognizer.open('jp.model')
    self.char = zinnia.Character()
    self.char.set_width(self.CHAR_WIDTH)
    self.char.set_height(self.CHAR_HEIGHT)

    self.result = []
    self.strokes = []
    self.transform_strokes = []
    self.points = []
    self.group = None

  def reset(self):
    self.scene.clear()
    self.strokes = []
    self.transform_strokes = []
    self.points = []
    self.group = None
    self.on_reset()

  def on_reset(self): pass

  def tabletEvent(self, event):
    if event.type() == event.TabletMove:
      event.accept()
      if event.pressure() > self.MINIMUM_PRESSURE:
        self.draw_point(event)
        self.points.append((event.x(), event.y()))
      elif event.pressure() == 0 and self.points:
        simplified = simplify_points(self.points, 5)
        for p1, p2 in zip(simplified[:-1], simplified[1:]):
          self.draw_line(p1, p2)

        self.strokes.append(simplified)
        result = self.recognize()

        self.points = []

  def draw_point(self, event):
    size = self.BRUSH_SIZE * event.pressure()
    rect = self.scene.addRect(-size / 2.0, -size / 2.0, size, size)
    rect.setPos(self.mapToScene(event.pos()))
    rect.setRotation(random.randint(0, 90))

  def draw_line(self, p1, p2):
    p1 = self.mapToScene(p1[0], p1[1])
    p2 = self.mapToScene(p2[0], p2[1])
    self.scene.addLine(QLineF(p1, p2), self.pen)

  def recognize(self):
    min_x = min_y = 2 ** 32
    max_x = max_y = 0
    for stroke in self.strokes:
      for point in stroke:
        x, y = point
        if x < min_x: min_x = x
        if x > max_x: max_x = x
        if y < min_y: min_y = y
        if y > max_y: max_y = y
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    x_transform = y_transform = None
    if width > height:
      aspect = self.CHAR_WIDTH / width
      x_transform = lambda x: (x - min_x) * aspect
      y_transform = lambda y: (y - min_y) * aspect
    else:
      aspect = self.CHAR_HEIGHT / height
      x_transform = lambda x: (x - min_x) * aspect
      y_transform = lambda y: (y - min_y) * aspect

    self.char.clear()
    self.transform_strokes = []
    for i, stroke in enumerate(self.strokes):
      self.transform_strokes.append([])
      for pi, point in enumerate(stroke):
        x, y = point
        nx = x_transform(x)
        ny = y_transform(y)
        self.char.add(i, nx, ny)
        self.transform_strokes[i].append((nx, ny))

    if self.group:
      for item in self.group:
        self.scene.removeItem(item)
    self.group = []
    for stroke in self.transform_strokes:
      for p1, p2 in zip(stroke[:-1], stroke[1:]):
        p1 = self.mapToScene(p1[0], p1[1]) + QPoint(20, 20)
        p2 = self.mapToScene(p2[0], p2[1]) + QPoint(20, 20)
        line = self.scene.addLine(QLineF(p1, p2), self.helper_pen)
        self.group.append(line)

    htracks = []
    vtracks = []
    for i, stroke in enumerate(self.strokes):
      htrack = vtrack = ''
      last_hdir = last_vdir = None
      for p1, p2 in zip(stroke[:-1], stroke[1:]):
        hdir, vdir = self.get_line_direction(p1, p2)
        if hdir != last_hdir:
          htrack += hdir
        if vdir != last_vdir:
          vtrack += vdir
        last_hdir = hdir
        last_vdir = vdir
      htracks.append(htrack)
      vtracks.append(vtrack)
    print 'htracks', ' '.join(htracks)
    print 'vtracks', ' '.join(vtracks)

    stroke_count = len(self.strokes)

    intersect_count = 0
    for i, stroke1 in enumerate(self.strokes):
      for stroke2 in self.strokes[i + 1:]:
        for p11, p12 in zip(stroke1[:-1], stroke1[1:]):
          for p21, p22 in zip(stroke2[:-1], stroke2[1:]):
            #if QLineF(p11, p12).intersect(QLineF(p21, p22)):
            intersect = QLineF(p11[0], p11[1], p12[0], p12[1]).intersect(
                QLineF(p21[0], p21[1], p22[0], p22[1]), None)
            if intersect == QLineF.BoundedIntersection:
              intersect_count += 1
    print 'intersect', intersect_count

    hmoves = []
    vmoves = []
    for s1, s2 in zip(self.strokes[:-1], self.strokes[1:]):
      p1 = s1[-1]
      p2 = s2[0]
      hdir, vdir = self.get_line_direction(p1, p2)
      hmoves.append(hdir)
      vmoves.append(vdir)
    print 'hmoves', hmoves
    print 'vmoves', vmoves

    result = self.recognizer.classify(self.char, 10)
    self.result = []
    for i in range(result.size()):
      value = result.value(i)
      if STROKE_COUNTS[value] != stroke_count: continue
      for rule in TRACK_RULES.get(value, []):
        print value, rule, htracks, vtracks
        if not rule(htracks, vtracks): continue
      if not INTERSECT_RULES.get(value, lambda i: True)(intersect_count):
        continue
      for rule in MOVE_RULES.get(value, []):
        print value, rule, hmoves, vmoves
        if not rule(hmoves, vmoves): continue
      self.result.append(Result(result.score(i), value))
    if result.size() > 0:
      self.on_result()

  def on_result(self): pass

  def get_line_direction(self, p1, p2):
    vx = p2[0] - p1[0]
    vy = p2[1] - p1[1]
    hdir = 'L'
    if vx > 0: hdir = 'R'
    if vy > 0 and abs(vx) / float(abs(vy)) < self.MIDDLE_RATIO:
      hdir = 'M'
    vdir = 'U'
    if vy > 0: vdir = 'D'
    if vx > 0 and abs(vy) / float(abs(vx)) < self.MIDDLE_RATIO:
      vdir = 'M'
    return hdir, vdir
