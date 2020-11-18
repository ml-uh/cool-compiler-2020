
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programARROW ASSIGNATION ATTRIBUTEID CASE CLASS CLASSID COLON COMMA COMPLEMENT DISPATCH DIVIDE DOT ELSE EQUAL ESAC FALSE FI GREATER GREATEREQUAL IF IN INHERITS ISVOID LBRACE LESS LESSEQUAL LET LOOP LPAREN MINUS NEW NOT NUMBER OF PLUS POOL RBRACE RPAREN SEMICOLON STRING THEN TIMES TRUE WHILEprogram : class_listclass_list : class_definition class_list\n                    | class_definitionclass_definition : CLASS CLASSID LBRACE class_feature_list RBRACE SEMICOLON\n                        | CLASS CLASSID INHERITS CLASSID LBRACE class_feature_list RBRACE SEMICOLONempty :class_feature_list : feature class_feature_list\n                            | emptyfeature : attribute_feature\n                | function_featureattribute_feature : ATTRIBUTEID COLON CLASSID SEMICOLON\n                            | ATTRIBUTEID COLON CLASSID ASSIGNATION expression SEMICOLONfunction_feature : ATTRIBUTEID LPAREN parameters_list RPAREN COLON CLASSID LBRACE expression RBRACE SEMICOLON\n                        | ATTRIBUTEID LPAREN RPAREN COLON CLASSID LBRACE expression RBRACE SEMICOLONparameters_list : parameter COMMA parameters_list\n                        | parameterparameter : ATTRIBUTEID COLON CLASSIDexpression_list : expression SEMICOLON expression_list\n                        | expression SEMICOLONlet_body : ATTRIBUTEID COLON CLASSID\n                | ATTRIBUTEID COLON CLASSID ASSIGNATION expression\n                | ATTRIBUTEID COLON CLASSID COMMA let_body\n                | ATTRIBUTEID COLON CLASSID ASSIGNATION expression COMMA let_bodycase_body : ATTRIBUTEID COLON CLASSID ARROW expression SEMICOLON case_body\n                | ATTRIBUTEID COLON CLASSID ARROW expression SEMICOLONexpression : not_form\n                    | mixed_expressionnot_form : NOT expressionmixed_expression : expression LESSEQUAL expression\n                        | expression LESS expression\n                        | expression EQUAL expression\n                        | arithmetic_expressionarithmetic_expression : expression PLUS expression\n                             | expression MINUS expression\n                             | termterm : expression TIMES expression\n            | expression DIVIDE expression\n            | isvoid_formisvoid_form : ISVOID expression\n                    | complement_formcomplement_form : COMPLEMENT expression\n                        | program_atomprogram_atom : TRUE\n                    | FALSEprogram_atom : STRINGprogram_atom : NUMBERprogram_atom : ATTRIBUTEIDprogram_atom : LPAREN expression RPARENprogram_atom : NEW CLASSIDprogram_atom : member_callprogram_atom : program_atom function_callprogram_atom : ATTRIBUTEID ASSIGNATION expressionprogram_atom : CASE expression OF case_body ESACprogram_atom : LET let_body IN expressionprogram_atom : LBRACE expression_list RBRACEprogram_atom : WHILE expression LOOP expression POOLprogram_atom : IF expression THEN expression ELSE expression FIfunction_call : DOT ATTRIBUTEID LPAREN argument_list RPAREN\n                    | DOT ATTRIBUTEID LPAREN RPAREN\n                    | DISPATCH CLASSID DOT ATTRIBUTEID LPAREN argument_list RPAREN\n                    | DISPATCH CLASSID DOT ATTRIBUTEID LPAREN RPARENargument_list : expression\n                    | expression COMMA argument_listmember_call : ATTRIBUTEID LPAREN RPAREN\n                    | ATTRIBUTEID LPAREN argument_list RPAREN'
    
_lr_action_items = {'CLASS':([0,3,21,63,],[4,4,-4,-5,]),'$end':([1,2,3,5,21,63,],[0,-1,-3,-2,-4,-5,]),'CLASSID':([4,8,18,30,32,52,60,79,107,132,],[6,15,22,59,61,81,89,103,121,141,]),'LBRACE':([6,15,29,39,43,45,51,54,56,57,58,61,64,65,67,68,69,70,71,72,73,89,90,106,109,110,111,112,115,116,133,136,140,148,],[7,20,56,56,56,56,56,56,56,56,56,90,56,56,56,56,56,56,56,56,56,112,56,56,56,56,56,56,56,56,56,56,56,56,]),'INHERITS':([6,],[8,]),'RBRACE':([7,9,10,11,12,13,17,20,27,28,35,37,38,40,41,42,44,46,47,48,49,50,53,66,74,75,76,77,81,85,91,92,95,96,97,98,99,100,101,104,108,109,113,114,120,122,125,129,131,135,138,139,145,147,150,151,],[-6,16,-6,-8,-9,-10,-7,-6,34,-11,-47,-26,-27,-32,-35,-38,-40,-42,-43,-44,-45,-46,-50,-12,-28,-39,-41,-51,-49,108,-52,-64,-29,-30,-31,-33,-34,-36,-37,-48,-55,-19,126,-65,-54,-18,137,-59,-53,-56,-14,-58,-13,-61,-57,-60,]),'ATTRIBUTEID':([7,10,12,13,19,20,28,29,33,39,43,45,51,54,55,56,57,58,64,65,66,67,68,69,70,71,72,73,78,90,105,106,109,110,111,112,115,116,117,133,134,136,138,140,145,148,149,154,],[14,14,-9,-10,23,14,-11,35,23,35,35,35,35,35,84,35,35,35,35,35,-12,35,35,35,35,35,35,35,102,35,119,35,35,35,35,35,35,35,130,35,84,35,-14,35,-13,35,84,119,]),'COLON':([14,23,25,31,84,119,],[18,30,32,60,107,132,]),'LPAREN':([14,29,35,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,102,106,109,110,111,112,115,116,130,133,136,140,148,],[19,51,65,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,116,51,51,51,51,51,51,51,140,51,51,51,51,]),'SEMICOLON':([16,22,34,35,36,37,38,40,41,42,44,46,47,48,49,50,53,74,75,76,77,81,86,91,92,95,96,97,98,99,100,101,104,108,114,120,126,129,131,135,137,139,147,150,151,152,],[21,28,63,-47,66,-26,-27,-32,-35,-38,-40,-42,-43,-44,-45,-46,-50,-28,-39,-41,-51,-49,109,-52,-64,-29,-30,-31,-33,-34,-36,-37,-48,-55,-65,-54,138,-59,-53,-56,145,-58,-61,-57,-60,154,]),'RPAREN':([19,24,26,35,37,38,40,41,42,44,46,47,48,49,50,53,59,62,65,74,75,76,77,80,81,91,92,93,94,95,96,97,98,99,100,101,104,108,114,116,120,127,128,129,131,135,139,140,146,147,150,151,],[25,31,-16,-47,-26,-27,-32,-35,-38,-40,-42,-43,-44,-45,-46,-50,-17,-15,92,-28,-39,-41,-51,104,-49,-52,-64,114,-62,-29,-30,-31,-33,-34,-36,-37,-48,-55,-65,129,-54,-63,139,-59,-53,-56,-58,147,151,-61,-57,-60,]),'ASSIGNATION':([22,35,121,],[29,64,133,]),'COMMA':([26,35,37,38,40,41,42,44,46,47,48,49,50,53,59,74,75,76,77,81,91,92,94,95,96,97,98,99,100,101,104,108,114,120,121,129,131,135,139,142,147,150,151,],[33,-47,-26,-27,-32,-35,-38,-40,-42,-43,-44,-45,-46,-50,-17,-28,-39,-41,-51,-49,-52,-64,115,-29,-30,-31,-33,-34,-36,-37,-48,-55,-65,-54,134,-59,-53,-56,-58,149,-61,-57,-60,]),'NOT':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'ISVOID':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'COMPLEMENT':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'TRUE':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'FALSE':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'STRING':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'NUMBER':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'NEW':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'CASE':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'LET':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'WHILE':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'IF':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'DOT':([35,37,38,40,41,42,44,46,47,48,49,50,53,74,75,76,77,81,91,92,95,96,97,98,99,100,101,103,104,108,114,120,129,131,135,139,147,150,151,],[-47,-26,-27,-32,-35,-38,-40,78,-43,-44,-45,-46,-50,-28,-39,-41,-51,-49,-52,-64,-29,-30,-31,-33,-34,-36,-37,117,-48,-55,-65,-54,-59,-53,-56,-58,-61,-57,-60,]),'DISPATCH':([35,37,38,40,41,42,44,46,47,48,49,50,53,74,75,76,77,81,91,92,95,96,97,98,99,100,101,104,108,114,120,129,131,135,139,147,150,151,],[-47,-26,-27,-32,-35,-38,-40,79,-43,-44,-45,-46,-50,-28,-39,-41,-51,-49,-52,-64,-29,-30,-31,-33,-34,-36,-37,-48,-55,-65,-54,-59,-53,-56,-58,-61,-57,-60,]),'LESSEQUAL':([35,36,37,38,40,41,42,44,46,47,48,49,50,53,74,75,76,77,80,81,82,86,87,88,91,92,94,95,96,97,98,99,100,101,104,108,113,114,120,123,124,125,129,131,135,139,142,144,147,150,151,152,],[-47,67,-26,-27,-32,-35,-38,-40,-42,-43,-44,-45,-46,-50,67,67,67,-51,67,-49,67,67,67,67,67,-64,67,67,67,67,67,67,67,67,-48,-55,67,-65,67,67,67,67,-59,-53,-56,-58,67,67,-61,-57,-60,67,]),'LESS':([35,36,37,38,40,41,42,44,46,47,48,49,50,53,74,75,76,77,80,81,82,86,87,88,91,92,94,95,96,97,98,99,100,101,104,108,113,114,120,123,124,125,129,131,135,139,142,144,147,150,151,152,],[-47,68,-26,-27,-32,-35,-38,-40,-42,-43,-44,-45,-46,-50,68,68,68,-51,68,-49,68,68,68,68,68,-64,68,68,68,68,68,68,68,68,-48,-55,68,-65,68,68,68,68,-59,-53,-56,-58,68,68,-61,-57,-60,68,]),'EQUAL':([35,36,37,38,40,41,42,44,46,47,48,49,50,53,74,75,76,77,80,81,82,86,87,88,91,92,94,95,96,97,98,99,100,101,104,108,113,114,120,123,124,125,129,131,135,139,142,144,147,150,151,152,],[-47,69,-26,-27,-32,-35,-38,-40,-42,-43,-44,-45,-46,-50,69,69,69,-51,69,-49,69,69,69,69,69,-64,69,69,69,69,69,69,69,69,-48,-55,69,-65,69,69,69,69,-59,-53,-56,-58,69,69,-61,-57,-60,69,]),'PLUS':([35,36,37,38,40,41,42,44,46,47,48,49,50,53,74,75,76,77,80,81,82,86,87,88,91,92,94,95,96,97,98,99,100,101,104,108,113,114,120,123,124,125,129,131,135,139,142,144,147,150,151,152,],[-47,70,-26,-27,-32,-35,-38,-40,-42,-43,-44,-45,-46,-50,70,70,70,-51,70,-49,70,70,70,70,70,-64,70,70,70,70,70,70,70,70,-48,-55,70,-65,70,70,70,70,-59,-53,-56,-58,70,70,-61,-57,-60,70,]),'MINUS':([35,36,37,38,40,41,42,44,46,47,48,49,50,53,74,75,76,77,80,81,82,86,87,88,91,92,94,95,96,97,98,99,100,101,104,108,113,114,120,123,124,125,129,131,135,139,142,144,147,150,151,152,],[-47,71,-26,-27,-32,-35,-38,-40,-42,-43,-44,-45,-46,-50,71,71,71,-51,71,-49,71,71,71,71,71,-64,71,71,71,71,71,71,71,71,-48,-55,71,-65,71,71,71,71,-59,-53,-56,-58,71,71,-61,-57,-60,71,]),'TIMES':([35,36,37,38,40,41,42,44,46,47,48,49,50,53,74,75,76,77,80,81,82,86,87,88,91,92,94,95,96,97,98,99,100,101,104,108,113,114,120,123,124,125,129,131,135,139,142,144,147,150,151,152,],[-47,72,-26,-27,-32,-35,-38,-40,-42,-43,-44,-45,-46,-50,72,72,72,-51,72,-49,72,72,72,72,72,-64,72,72,72,72,72,72,72,72,-48,-55,72,-65,72,72,72,72,-59,-53,-56,-58,72,72,-61,-57,-60,72,]),'DIVIDE':([35,36,37,38,40,41,42,44,46,47,48,49,50,53,74,75,76,77,80,81,82,86,87,88,91,92,94,95,96,97,98,99,100,101,104,108,113,114,120,123,124,125,129,131,135,139,142,144,147,150,151,152,],[-47,73,-26,-27,-32,-35,-38,-40,-42,-43,-44,-45,-46,-50,73,73,73,-51,73,-49,73,73,73,73,73,-64,73,73,73,73,73,73,73,73,-48,-55,73,-65,73,73,73,73,-59,-53,-56,-58,73,73,-61,-57,-60,73,]),'OF':([35,37,38,40,41,42,44,46,47,48,49,50,53,74,75,76,77,81,82,91,92,95,96,97,98,99,100,101,104,108,114,120,129,131,135,139,147,150,151,],[-47,-26,-27,-32,-35,-38,-40,-42,-43,-44,-45,-46,-50,-28,-39,-41,-51,-49,105,-52,-64,-29,-30,-31,-33,-34,-36,-37,-48,-55,-65,-54,-59,-53,-56,-58,-61,-57,-60,]),'LOOP':([35,37,38,40,41,42,44,46,47,48,49,50,53,74,75,76,77,81,87,91,92,95,96,97,98,99,100,101,104,108,114,120,129,131,135,139,147,150,151,],[-47,-26,-27,-32,-35,-38,-40,-42,-43,-44,-45,-46,-50,-28,-39,-41,-51,-49,110,-52,-64,-29,-30,-31,-33,-34,-36,-37,-48,-55,-65,-54,-59,-53,-56,-58,-61,-57,-60,]),'THEN':([35,37,38,40,41,42,44,46,47,48,49,50,53,74,75,76,77,81,88,91,92,95,96,97,98,99,100,101,104,108,114,120,129,131,135,139,147,150,151,],[-47,-26,-27,-32,-35,-38,-40,-42,-43,-44,-45,-46,-50,-28,-39,-41,-51,-49,111,-52,-64,-29,-30,-31,-33,-34,-36,-37,-48,-55,-65,-54,-59,-53,-56,-58,-61,-57,-60,]),'POOL':([35,37,38,40,41,42,44,46,47,48,49,50,53,74,75,76,77,81,91,92,95,96,97,98,99,100,101,104,108,114,120,123,129,131,135,139,147,150,151,],[-47,-26,-27,-32,-35,-38,-40,-42,-43,-44,-45,-46,-50,-28,-39,-41,-51,-49,-52,-64,-29,-30,-31,-33,-34,-36,-37,-48,-55,-65,-54,135,-59,-53,-56,-58,-61,-57,-60,]),'ELSE':([35,37,38,40,41,42,44,46,47,48,49,50,53,74,75,76,77,81,91,92,95,96,97,98,99,100,101,104,108,114,120,124,129,131,135,139,147,150,151,],[-47,-26,-27,-32,-35,-38,-40,-42,-43,-44,-45,-46,-50,-28,-39,-41,-51,-49,-52,-64,-29,-30,-31,-33,-34,-36,-37,-48,-55,-65,-54,136,-59,-53,-56,-58,-61,-57,-60,]),'IN':([35,37,38,40,41,42,44,46,47,48,49,50,53,74,75,76,77,81,83,91,92,95,96,97,98,99,100,101,104,108,114,120,121,129,131,135,139,142,143,147,150,151,153,],[-47,-26,-27,-32,-35,-38,-40,-42,-43,-44,-45,-46,-50,-28,-39,-41,-51,-49,106,-52,-64,-29,-30,-31,-33,-34,-36,-37,-48,-55,-65,-54,-20,-59,-53,-56,-58,-21,-22,-61,-57,-60,-23,]),'FI':([35,37,38,40,41,42,44,46,47,48,49,50,53,74,75,76,77,81,91,92,95,96,97,98,99,100,101,104,108,114,120,129,131,135,139,144,147,150,151,],[-47,-26,-27,-32,-35,-38,-40,-42,-43,-44,-45,-46,-50,-28,-39,-41,-51,-49,-52,-64,-29,-30,-31,-33,-34,-36,-37,-48,-55,-65,-54,-59,-53,-56,-58,150,-61,-57,-60,]),'ESAC':([118,154,155,],[131,-25,-24,]),'ARROW':([141,],[148,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'class_list':([0,3,],[2,5,]),'class_definition':([0,3,],[3,3,]),'class_feature_list':([7,10,20,],[9,17,27,]),'feature':([7,10,20,],[10,10,10,]),'empty':([7,10,20,],[11,11,11,]),'attribute_feature':([7,10,20,],[12,12,12,]),'function_feature':([7,10,20,],[13,13,13,]),'parameters_list':([19,33,],[24,62,]),'parameter':([19,33,],[26,26,]),'expression':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[36,74,75,76,80,82,86,87,88,91,94,95,96,97,98,99,100,101,113,120,86,123,124,125,94,94,142,144,94,152,]),'not_form':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'mixed_expression':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'arithmetic_expression':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'term':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'isvoid_form':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'complement_form':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'program_atom':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'member_call':([29,39,43,45,51,54,56,57,58,64,65,67,68,69,70,71,72,73,90,106,109,110,111,112,115,116,133,136,140,148,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'function_call':([46,],[77,]),'let_body':([55,134,149,],[83,143,153,]),'expression_list':([56,109,],[85,122,]),'argument_list':([65,115,116,140,],[93,127,128,146,]),'case_body':([105,154,],[118,155,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> class_list','program',1,'p_program','parser.py',19),
  ('class_list -> class_definition class_list','class_list',2,'p_class_list','parser.py',24),
  ('class_list -> class_definition','class_list',1,'p_class_list','parser.py',25),
  ('class_definition -> CLASS CLASSID LBRACE class_feature_list RBRACE SEMICOLON','class_definition',6,'p_class_definition','parser.py',33),
  ('class_definition -> CLASS CLASSID INHERITS CLASSID LBRACE class_feature_list RBRACE SEMICOLON','class_definition',8,'p_class_definition','parser.py',34),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',42),
  ('class_feature_list -> feature class_feature_list','class_feature_list',2,'p_class_feature_list','parser.py',47),
  ('class_feature_list -> empty','class_feature_list',1,'p_class_feature_list','parser.py',48),
  ('feature -> attribute_feature','feature',1,'p_feature','parser.py',57),
  ('feature -> function_feature','feature',1,'p_feature','parser.py',58),
  ('attribute_feature -> ATTRIBUTEID COLON CLASSID SEMICOLON','attribute_feature',4,'p_attribute_feature','parser.py',63),
  ('attribute_feature -> ATTRIBUTEID COLON CLASSID ASSIGNATION expression SEMICOLON','attribute_feature',6,'p_attribute_feature','parser.py',64),
  ('function_feature -> ATTRIBUTEID LPAREN parameters_list RPAREN COLON CLASSID LBRACE expression RBRACE SEMICOLON','function_feature',10,'p_function_feature','parser.py',72),
  ('function_feature -> ATTRIBUTEID LPAREN RPAREN COLON CLASSID LBRACE expression RBRACE SEMICOLON','function_feature',9,'p_function_feature','parser.py',73),
  ('parameters_list -> parameter COMMA parameters_list','parameters_list',3,'p_parameter_list','parser.py',81),
  ('parameters_list -> parameter','parameters_list',1,'p_parameter_list','parser.py',82),
  ('parameter -> ATTRIBUTEID COLON CLASSID','parameter',3,'p_parameter','parser.py',90),
  ('expression_list -> expression SEMICOLON expression_list','expression_list',3,'p_expression_list','parser.py',95),
  ('expression_list -> expression SEMICOLON','expression_list',2,'p_expression_list','parser.py',96),
  ('let_body -> ATTRIBUTEID COLON CLASSID','let_body',3,'p_let_body','parser.py',104),
  ('let_body -> ATTRIBUTEID COLON CLASSID ASSIGNATION expression','let_body',5,'p_let_body','parser.py',105),
  ('let_body -> ATTRIBUTEID COLON CLASSID COMMA let_body','let_body',5,'p_let_body','parser.py',106),
  ('let_body -> ATTRIBUTEID COLON CLASSID ASSIGNATION expression COMMA let_body','let_body',7,'p_let_body','parser.py',107),
  ('case_body -> ATTRIBUTEID COLON CLASSID ARROW expression SEMICOLON case_body','case_body',7,'p_case_body','parser.py',121),
  ('case_body -> ATTRIBUTEID COLON CLASSID ARROW expression SEMICOLON','case_body',6,'p_case_body','parser.py',122),
  ('expression -> not_form','expression',1,'p_expression','parser.py',130),
  ('expression -> mixed_expression','expression',1,'p_expression','parser.py',131),
  ('not_form -> NOT expression','not_form',2,'p_not_form','parser.py',136),
  ('mixed_expression -> expression LESSEQUAL expression','mixed_expression',3,'p_mixed_expression','parser.py',144),
  ('mixed_expression -> expression LESS expression','mixed_expression',3,'p_mixed_expression','parser.py',145),
  ('mixed_expression -> expression EQUAL expression','mixed_expression',3,'p_mixed_expression','parser.py',146),
  ('mixed_expression -> arithmetic_expression','mixed_expression',1,'p_mixed_expression','parser.py',147),
  ('arithmetic_expression -> expression PLUS expression','arithmetic_expression',3,'p_arithmetic_expression','parser.py',161),
  ('arithmetic_expression -> expression MINUS expression','arithmetic_expression',3,'p_arithmetic_expression','parser.py',162),
  ('arithmetic_expression -> term','arithmetic_expression',1,'p_arithmetic_expression','parser.py',163),
  ('term -> expression TIMES expression','term',3,'p_term','parser.py',174),
  ('term -> expression DIVIDE expression','term',3,'p_term','parser.py',175),
  ('term -> isvoid_form','term',1,'p_term','parser.py',176),
  ('isvoid_form -> ISVOID expression','isvoid_form',2,'p_isvoid_form','parser.py',187),
  ('isvoid_form -> complement_form','isvoid_form',1,'p_isvoid_form','parser.py',188),
  ('complement_form -> COMPLEMENT expression','complement_form',2,'p_complement_form','parser.py',196),
  ('complement_form -> program_atom','complement_form',1,'p_complement_form','parser.py',197),
  ('program_atom -> TRUE','program_atom',1,'p_program_atom_boolean','parser.py',205),
  ('program_atom -> FALSE','program_atom',1,'p_program_atom_boolean','parser.py',206),
  ('program_atom -> STRING','program_atom',1,'p_program_atom_string','parser.py',211),
  ('program_atom -> NUMBER','program_atom',1,'p_program_atom_int','parser.py',216),
  ('program_atom -> ATTRIBUTEID','program_atom',1,'p_program_atom_id','parser.py',221),
  ('program_atom -> LPAREN expression RPAREN','program_atom',3,'p_program_atom_parentesis','parser.py',226),
  ('program_atom -> NEW CLASSID','program_atom',2,'p_program_atom_new','parser.py',231),
  ('program_atom -> member_call','program_atom',1,'p_program_atom_member','parser.py',236),
  ('program_atom -> program_atom function_call','program_atom',2,'p_program_atom_function','parser.py',241),
  ('program_atom -> ATTRIBUTEID ASSIGNATION expression','program_atom',3,'p_program_atom_assign','parser.py',246),
  ('program_atom -> CASE expression OF case_body ESAC','program_atom',5,'p_program_atom_case','parser.py',251),
  ('program_atom -> LET let_body IN expression','program_atom',4,'p_program_atom_let','parser.py',256),
  ('program_atom -> LBRACE expression_list RBRACE','program_atom',3,'p_program_atom_block','parser.py',261),
  ('program_atom -> WHILE expression LOOP expression POOL','program_atom',5,'p_program_atom_while','parser.py',266),
  ('program_atom -> IF expression THEN expression ELSE expression FI','program_atom',7,'p_program_atom_if','parser.py',271),
  ('function_call -> DOT ATTRIBUTEID LPAREN argument_list RPAREN','function_call',5,'p_function_call','parser.py',276),
  ('function_call -> DOT ATTRIBUTEID LPAREN RPAREN','function_call',4,'p_function_call','parser.py',277),
  ('function_call -> DISPATCH CLASSID DOT ATTRIBUTEID LPAREN argument_list RPAREN','function_call',7,'p_function_call','parser.py',278),
  ('function_call -> DISPATCH CLASSID DOT ATTRIBUTEID LPAREN RPAREN','function_call',6,'p_function_call','parser.py',279),
  ('argument_list -> expression','argument_list',1,'p_argument_list','parser.py',294),
  ('argument_list -> expression COMMA argument_list','argument_list',3,'p_argument_list','parser.py',295),
  ('member_call -> ATTRIBUTEID LPAREN RPAREN','member_call',3,'p_member_call','parser.py',303),
  ('member_call -> ATTRIBUTEID LPAREN argument_list RPAREN','member_call',4,'p_member_call','parser.py',304),
]
