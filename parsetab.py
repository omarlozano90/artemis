
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'\x89\xbc,\xdba\xab\xc5\xb7\xdd\xa14\xaf+\xe9\xd7\x98'
    
_lr_action_items = {'TIMES':([4,5,6,10,11,],[-4,8,-5,-3,8,]),'$end':([2,4,6,7,10,11,],[0,-4,-5,-1,-3,-2,]),'NUMBER':([3,8,9,],[6,6,6,]),'PLUS':([4,5,6,10,],[-4,9,-5,-3,]),'EQUALS':([1,],[3,]),'NAME':([0,],[1,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'factor':([3,8,9,],[4,10,4,]),'expr':([3,],[7,]),'term':([3,9,],[5,11,]),'assign':([0,],[2,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> assign","S'",1,None,None,None),
  ('assign -> NAME EQUALS expr','assign',3,'p_assign','/Users/Macintosh/PycharmProjects/artemis/parsecon.py',10),
  ('expr -> term PLUS term','expr',3,'p_expr_plus','/Users/Macintosh/PycharmProjects/artemis/parsecon.py',14),
  ('term -> term TIMES factor','term',3,'p_term_mul','/Users/Macintosh/PycharmProjects/artemis/parsecon.py',18),
  ('term -> factor','term',1,'p_term_factor','/Users/Macintosh/PycharmProjects/artemis/parsecon.py',22),
  ('factor -> NUMBER','factor',1,'p_factor','/Users/Macintosh/PycharmProjects/artemis/parsecon.py',26),
]
