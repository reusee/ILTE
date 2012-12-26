# coding: utf8

from string import whitespace
from pprint import pprint

atom_end = set('()') | set(whitespace)

def parse(sexp):
  stack, i, length = [[]], 0, len(sexp)
  while i < length:
    c = sexp[i]
    if isinstance(stack[-1], list):
      if c == '(':
        stack.append([])
      elif c == ')':
        stack[-2].append(stack.pop())
      elif c in whitespace:
        pass
      else:
        stack.append(c)
    elif isinstance(stack[-1], str):
      if c in atom_end:
        atom = stack.pop()
        if atom[0].isdigit():
          stack[-1].append(eval(atom))
        else:
          stack[-1].append(atom)
        continue
      else:
        stack[-1] = stack[-1] + c
    i += 1
  return stack.pop()

if __name__ == '__main__':
  pprint(parse('''\
(character (value あ) (width 300) (height 300) (strokes ( ( 0 36 ) ( 151 28 ) ) ( ( 40 0 ) ( 69 183 ) ) ( ( 105 58 ) ( 95 115 ) ( 80 148 ) ( 59 163 ) ( 41 165 ) ( 22 146 ) ( 28 115 ) ( 66 88 ) ( 127 84 ) ( 168 100 ) ( 175 121 ) ( 165 145 ) ( 106 207 ) ) ))
(character (value い) (width 300) (height 300) (strokes ( ( 25 0 ) ( 1 83 ) ( 0 156 ) ( 9 180 ) ( 23 193 ) ( 49 195 ) ( 69 185 ) ) ( ( 133 33 ) ( 183 180 ) ) ))
(character (value う) (width 300) (height 300) (strokes ( ( 32 0 ) ( 64 38 ) ) ( ( 0 102 ) ( 45 89 ) ( 82 91 ) ( 114 107 ) ( 125 130 ) ( 121 157 ) ( 105 184 ) ( 29 261 ) ) ))
(character (value え) (width 300) (height 300) (strokes ( ( 67 1 ) ( 76 0 ) ( 90 15 ) ) ( ( 23 68 ) ( 105 54 ) ( 118 61 ) ( 111 81 ) ( 0 224 ) ( 57 156 ) ( 99 133 ) ( 113 135 ) ( 117 184 ) ( 134 206 ) ( 158 216 ) ( 204 212 ) ) ))
(character (value お) (width 300) (height 300) (strokes ( ( 22 19 ) ( 106 14 ) ) ( ( 56 0 ) ( 61 90 ) ( 55 117 ) ( 30 137 ) ( 11 127 ) ( 0 105 ) ( 9 81 ) ( 39 64 ) ( 81 63 ) ( 129 82 ) ( 143 102 ) ( 140 126 ) ( 121 148 ) ( 85 165 ) ) ( ( 136 6 ) ( 162 57 ) ) ))
(character (value か) (width 300) (height 300) (strokes ( ( 0 56 ) ( 101 49 ) ( 136 66 ) ( 142 98 ) ( 134 124 ) ( 101 170 ) ( 80 184 ) ) ( ( 86 0 ) ( 19 175 ) ) ( ( 169 17 ) ( 183 98 ) ) ))
(character (value き) (width 300) (height 300) (strokes ( ( 0 28 ) ( 18 32 ) ( 107 20 ) ) ( ( 10 88 ) ( 129 70 ) ) ( ( 43 0 ) ( 97 146 ) ) ( ( 25 163 ) ( 42 188 ) ( 69 199 ) ( 113 201 ) ( 141 194 ) ) ))
(character (value く) (width 300) (height 300) (strokes ( ( 77 0 ) ( 82 3 ) ( 65 36 ) ( 0 123 ) ( 38 164 ) ( 108 219 ) ) ))
(character (value け) (width 300) (height 300) (strokes ( ( 0 11 ) ( 0 189 ) ) ( ( 29 85 ) ( 42 90 ) ( 190 83 ) ) ( ( 108 0 ) ( 101 16 ) ( 104 151 ) ( 80 211 ) ) ))
(character (value こ) (width 300) (height 300) (strokes ( ( 27 0 ) ( 132 8 ) ) ( ( 21 62 ) ( 0 112 ) ( 3 126 ) ( 18 138 ) ( 71 146 ) ( 158 139 ) ) ))
(character (value が) (width 300) (height 300) (strokes ( ( 24 46 ) ( 90 42 ) ( 112 47 ) ( 128 62 ) ( 130 90 ) ( 121 117 ) ( 64 203 ) ) ( ( 75 0 ) ( 0 177 ) ) ( ( 147 23 ) ( 159 168 ) ) ( ( 178 18 ) ( 178 45 ) ) ( ( 192 9 ) ( 197 49 ) ) ))
(character (value ぎ) (width 300) (height 300) (strokes ( ( 4 56 ) ( 97 49 ) ) ( ( 0 105 ) ( 127 82 ) ) ( ( 48 0 ) ( 79 152 ) ) ( ( 14 157 ) ( 27 193 ) ( 47 208 ) ( 79 205 ) ( 118 187 ) ) ( ( 128 34 ) ( 131 59 ) ) ( ( 141 30 ) ( 150 60 ) ) ))
(character (value ぐ) (width 300) (height 300) (strokes ( ( 79 3 ) ( 0 103 ) ( 96 224 ) ) ( ( 107 4 ) ( 107 32 ) ) ( ( 124 0 ) ( 128 30 ) ) ))
(character (value げ) (width 300) (height 300) (strokes ( ( 1 9 ) ( 0 173 ) ) ( ( 27 67 ) ( 160 70 ) ) ( ( 102 1 ) ( 97 121 ) ( 78 181 ) ) ( ( 164 12 ) ( 165 34 ) ) ( ( 183 0 ) ( 189 29 ) ) ))
(character (value ご) (width 300) (height 300) (strokes ( ( 40 18 ) ( 124 30 ) ) ( ( 20 102 ) ( 0 148 ) ( 4 198 ) ( 154 240 ) ) ( ( 170 16 ) ( 182 58 ) ) ( ( 216 0 ) ( 228 52 ) ) ))
(character (value さ) (width 300) (height 300) (strokes ( ( 0 59 ) ( 23 60 ) ( 104 39 ) ) ( ( 60 0 ) ( 86 125 ) ) ( ( 22 134 ) ( 60 168 ) ( 89 172 ) ( 130 165 ) ) ))
(character (value し) (width 300) (height 300) (strokes ( ( 16 0 ) ( 0 72 ) ( 8 143 ) ( 35 168 ) ( 68 169 ) ( 103 156 ) ) ))
(character (value す) (width 300) (height 300) (strokes ( ( 0 27 ) ( 17 34 ) ( 151 38 ) ) ( ( 72 0 ) ( 64 108 ) ( 43 126 ) ( 29 108 ) ( 35 97 ) ( 51 92 ) ( 63 97 ) ( 72 116 ) ( 73 151 ) ( 52 214 ) ) ))
(character (value せ) (width 300) (height 300) (strokes ( ( 0 39 ) ( 124 38 ) ( 168 45 ) ) ( ( 103 3 ) ( 108 62 ) ( 102 95 ) ( 84 112 ) ( 66 105 ) ) ( ( 44 0 ) ( 30 53 ) ( 30 101 ) ( 39 138 ) ( 76 160 ) ( 134 157 ) ) ))
(character (value そ) (width 300) (height 300) (strokes ( ( 54 0 ) ( 130 6 ) ( 100 33 ) ( 0 92 ) ( 75 78 ) ( 165 77 ) ( 103 105 ) ( 82 141 ) ( 85 153 ) ( 105 165 ) ( 162 168 ) ) ))
(character (value ざ) (width 300) (height 300) (strokes ( ( 0 48 ) ( 104 38 ) ( 135 27 ) ) ( ( 51 0 ) ( 52 17 ) ( 92 107 ) ) ( ( 25 123 ) ( 72 155 ) ( 118 156 ) ( 148 144 ) ) ( ( 150 7 ) ( 153 30 ) ) ( ( 163 6 ) ( 168 20 ) ) ))
(character (value じ) (width 300) (height 300) (strokes ( ( 24 0 ) ( 0 79 ) ( 2 123 ) ( 18 151 ) ( 45 168 ) ( 79 172 ) ( 115 159 ) ( 140 138 ) ) ( ( 106 13 ) ( 110 55 ) ) ( ( 126 13 ) ( 128 38 ) ) ))
(character (value ず) (width 300) (height 300) (strokes ( ( 0 45 ) ( 180 37 ) ) ( ( 100 0 ) ( 82 105 ) ( 70 117 ) ( 57 116 ) ( 50 106 ) ( 62 80 ) ( 93 74 ) ( 108 90 ) ( 109 125 ) ( 90 173 ) ( 52 229 ) ) ( ( 196 10 ) ( 195 37 ) ) ( ( 208 6 ) ( 208 32 ) ) ))
(character (value ぜ) (width 300) (height 300) (strokes ( ( 0 55 ) ( 25 61 ) ( 174 46 ) ) ( ( 122 14 ) ( 115 105 ) ( 97 120 ) ( 80 115 ) ) ( ( 49 0 ) ( 40 83 ) ( 47 162 ) ( 75 170 ) ( 153 164 ) ) ( ( 190 13 ) ( 190 33 ) ) ( ( 206 11 ) ( 208 24 ) ) ))
'''))
