#!/usr/bin/env python
# coding: utf8

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import canvas
import random

class Canvas(canvas.Canvas):
  def __init__(self):
    super(Canvas, self).__init__()

    self.recognized.connect(self.on_recognized)

    self.out = open('jp.train', 'a')

    self.font = QFont()
    self.font.setPointSize(256)
    self.brush = QBrush(QColor(0, 0, 0, 32))

    self.candidate_font = QFont()
    self.candidate_font.setPointSize(48)
    self.candidate_brush = QBrush(QColor(0, 0, 128, 196))
    self.candidate_text = None
    def _on_reset():
      if self.candidate_text:
        self.scene.removeItem(self.candidate_text)
        self.candidate_text = None
    self.reseted.connect(_on_reset)

    self.chars = [
        #'あ', 'い', 'う', 'え', 'お', 
        #'か', 'き', 'く', 'け', 'こ', 
        #'が', 'ぎ', 'ぐ', 'げ', 'ご', 
        #'さ', 'し', 'す', 'せ', 'そ', 
        #'ざ', 'じ', 'ず', 'ぜ', 'ぞ', 
        #'た', 'ち', 'つ', 'て', 'と', 
        #'だ', 'ぢ', 'づ', 'で', 'ど', 
        #'な', 'に', 'ぬ', 'ね', 'の', 
        #'は', 'ひ', 'ふ', 'へ', 'ほ', 
        #'ば', 'び', 'ぶ', 'べ', 'ぼ', 
        #'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ', 
        #'ま', 'み', 'む', 'め', 'も', 
        #'や', 'ゆ', 'よ', 
        'ら', 'り', 'る', 'れ', 'ろ', 
        'わ', 'を', 'ん', 

        ##'ア', 'イ', 'ウ', 'エ', 'オ', 
        #'カ', 'キ', 'ク', 'ケ', 'コ', 
        #'ガ', 'ギ', 'グ', 'ゲ', 'ゴ', 
        #'サ', 'シ', 'ス', 'セ', 'ソ', 
        #'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ', 
        #'タ', 'チ', 'ツ', 'テ', 'ト', 
        #'ダ', 'ヂ', 'ヅ', 'デ', 'ド', 
        #'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 
        #'ハ', 'ヒ', 'フ', 'ヘ', 'ホ', 
        #'バ', 'ビ', 'ブ', 'ベ', 'ボ', 
        #'パ', 'ピ', 'プ', 'ペ', 'ポ', 
        #'マ', 'ミ', 'ム', 'メ', 'モ', 
        #'ヤ', 'ユ', 'ヨ', 
        #'ラ', 'リ', 'ル', 'レ', 'ロ', 
        #'ワ', 'ヲ', 'ン', 

        ]

    self.train_text_item = None
    self.index = -1
    self.cur_char = None
    self.show_next()

  def next_char(self):
    self.index += 1
    if self.index == len(self.chars):
      self.index = 0
    self.cur_char = self.chars[self.index]

  def show_char(self):
    self.reset()
    if self.train_text_item:
      self.scene.removeItem(self.train_text_item)
    text = self.scene.addSimpleText(QString(self.cur_char.decode('utf8')), self.font)
    text.setBrush(self.brush)
    self.train_text_item = text

  def show_next(self):
    self.next_char()
    self.show_char()

  def keyPressEvent(self, event):
    if event.key() == Qt.Key_Tab:
      self.show_next()
    elif event.key() == Qt.Key_Space:
      if self.strokes:
        self.output_train_data()
      self.show_next()

  def mousePressEvent(self, event):
    if event.button() == Qt.RightButton:
      self.undo_stroke()

  def output_train_data(self):
    print >>self.out, '(character (value %s) (width %d) (height %d) (strokes' % (
        self.cur_char, self.CHAR_WIDTH, self.CHAR_HEIGHT
        ),
    for stroke in self.transform_strokes:
      print >>self.out, '(',
      for point in stroke:
        x, y = point
        print >>self.out, '(', x, y, ')',
      print >>self.out, ')',
    print >>self.out, '))'

  def on_recognized(self):
    if self.candidate_text:
      self.scene.removeItem(self.candidate_text)
    text = self.scene.addSimpleText(QString(' '.join(
      x.value.decode('utf8') for x in self.result)), self.candidate_font)
    text.setBrush(self.candidate_brush)
    text.setPos(self.mapToScene(20, self.CHAR_HEIGHT + 20))
    self.candidate_text = text

def main():
  app = QApplication(sys.argv)
  canvas = Canvas()
  canvas.show()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()
