# coding: utf8

STROKE_COUNTS = {
  1: set(['く', 'し', 'そ', 'つ', 'て', 'の', 'ひ', 'へ', 'る', 'ろ', 'ん', 
    'ノ', 'フ', 'ヘ', 'レ', ]),
  2: set(['い', 'う', 'え', 'こ', 'す', 'ち', 'と', 'ぬ', 'ね', 'ぴ', 'ぺ', 'み', 'め', 'ゆ', 'よ', 'ら', 'り', 'れ', 'わ',
    'ア', 'イ', 'カ', 'ク', 'コ', 'ス', 'セ', 'ソ', 'ト', 'ナ', 'ニ', 'ヌ', 'ハ', 'ヒ', 'プ', 'ペ', 'マ', 'ム', 'メ', 'ヤ', 'ユ', 'ラ', 'リ', 'ル', 'ワ', 'ン', ]),
  3: set(['あ', 'お', 'か', 'け', 'ぐ', 'さ', 'せ', 'じ', 'ぞ', 'づ', 'で', 'に', 'は', 'び', 'べ', 'ま', 'む', 'も', 'や', 'を', 
    'ウ', 'エ', 'オ', 'キ', 'ケ', 'サ', 'シ', 'タ', 'チ', 'ツ', 'テ', 'ブ', 'ベ', 'パ', 'ピ', 'ミ', 'モ', 'ヨ', 'ロ', 'ヲ', ]),
  4: set(['き', 'ご', 'ず', 'た', 'ぢ', 'ど', 'な', 'ふ', 'ほ', 'ぱ', 
    'ガ', 'グ', 'ゴ', 'ズ', 'ゼ', 'ゾ', 'ド', 'ネ', 'ホ', 'バ', 'ビ', ]),
  5: set(['が', 'げ', 'ざ', 'ぜ', 'ば', 'ぷ', 'ぽ', 
    'ギ', 'ゲ', 'ザ', 'ジ', 'ダ', 'ヂ', 'ヅ', 'デ', 'ポ', ]),
  6: set(['ぎ', 'だ', 'ぶ', 'ぼ', 
    'ボ', ]),
}

TRACK_RULES = {
  # A

  # K

  # S
  'そ': [
    lambda htracks, vtracks: htracks[0][:4] == 'RLRL',
    ],

  # T
  'て': [
    lambda htracks, vtracks: htracks[0][:2] == 'RL',
    ],

  # N

  # H
  'へ': [
    lambda htracks, vtracks: vtracks[0] == 'UD',
    ],

  # M
  'め': [
    lambda htracks, vtracks: htracks[-1][-1] == 'L',
    ],
  'も': [
    lambda htracks, vtracks: vtracks[2] == 'DMU',
    ],

  # Y
  'や': [
    lambda htracks, vtracks: htracks[0] == 'RML',
    ],

  # R
  'り': [
    lambda htracks, vtracks: vtracks[1][0] == 'U',
    ],

  # W N
  'わ': [
    lambda htracks, vtracks: htracks[1][-1] == 'L',
    ],

  # G
  'ぐ': [
    lambda htracks, vtracks: htracks[0] == 'LR',
    ],

  # Z

  # D
  'で': [
    lambda htracks, vtracks: htracks[0][:2] == 'RL',
    ],

  # B
  'べ': [
    lambda htracks, vtracks: vtracks[0] == 'UD',
    ],

  # P

  'キ': [
    lambda htracks, vtracks: htracks[2] != 'L',
    ],
  'ケ': [
    lambda htracks, vtracks: htracks[0] == 'L',
    lambda htracks, vtracks: htracks[1] == 'R',
    lambda htracks, vtracks: htracks[2] == 'L',
    ],
  'ソ': [
    lambda htracks, vtracks: htracks[0] == 'R',
    ],
  'ト': [
    lambda htracks, vtracks: htracks[0] == 'M',
    ],
  'ヅ': [
    lambda htracks, vtracks: htracks[0] == 'R',
    lambda htracks, vtracks: htracks[1] == 'R',
    lambda htracks, vtracks: htracks[2] == 'L',
    ],
  'テ': [
    lambda htracks, vtracks: htracks[0] == 'R',
    lambda htracks, vtracks: htracks[1] == 'R',
    ],
  'ヌ': [
    lambda htracks, vtracks: htracks[0] == 'R',
    lambda htracks, vtracks: htracks[1] == 'L',
    ],
  'リ': [
    lambda htracks, vtracks: vtracks[0] == 'M',
    ],
  'ラ': [
    lambda htracks, vtracks: vtracks[0] == 'M',
    ],
  'レ': [
    lambda htracks, vtracks: vtracks[0] == 'DU',
    ],
  'モ': [
    lambda htracks, vtracks: vtracks[-1][-1] == 'M',
    ],

}

INTERSECT_RULES = {
  'ぶ': lambda i: i == 0,
  'ぷ': lambda i: i == 0,
}

MOVE_RULES = {
  'ヌ': [
    lambda hmoves, vmoves: hmoves[0] == 'R',
    ],
}
