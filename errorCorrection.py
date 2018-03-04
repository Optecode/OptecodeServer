import keyword
import re

def func_while(l):
  temp = l.replace(" ","")
  line = temp[0:5]+" "+temp[5:]
  if(temp[5] == '('):
    if(temp[-2:] != '):'):
      line = line[:-2] + "):"
    elif(temp[-1:] == ":" and temp[-2:-1] != ')'):
      line = line[:-2] + "):"
  elif(temp[-2:-1] == ")" and temp[5] != "("):
    line = line[:5]+"("+line[5:]
    if(line[-1:] != ":"):
      line = line + ":"
  elif(temp[5] != "(" and temp[-2:-1] != ")"):
    if(temp[-1:] != ":"):
      line = line + ":"
  return line

def func_def(l):
  temp = l.replace(" ","")
  if(temp[0:3] == "def"):
    line = l[0:3]+" "+temp[3:]
  if(l[-3:-1] != "()"):
    line = line + "()"
  if(l[-1:] != ":"):
    line = line + ":"
  if(l[-1:] == "("):
    line = line + "):"
  return line

def func_return(l):
  temp = l.replace(" ","")
  line = temp[0:6]+" "+temp[6:]
  return line

def func_print(line):
  temp = line.replace(" ","")
  word = temp[0:5]

  if(line[6:].isalnum()):
    return line
  elif(line[6] == "\""):
    if(line[-1] == "\'"):
      line[-1] = "\""
    if(line[-1] != "\"" ):
      line = line + "\""
  return line

def error_correction(lines):
  tab_prefix = 0
  keyword_terms = ["for","while","if","else","def"]
  for i in range(len(lines)):
    lines[i] = lines[i].lower()
    a = lines[i].replace(" ","")
    #while loop
    if a.startswith('while'):
      lines[i] = func_while(lines[i])
    elif a.startswith('for'):
      pass
    elif a.startswith('if'):
      pass
    elif a.startswith('elif'):
      pass
    elif a.startswith('else'):
      pass
    #def function
    elif a.startswith('def'):
      lines[i] = func_def(lines[i])
    #def return function
    elif a.startswith('return'):
      tab_prefix = 0
      lines[i] = func_return(lines[i])
    #print function
    elif a.startswith("print"):
      lines[i] = func_print(lines[i])
    elif(i != 0):
      if(" " in lines[i-1]):
        index = lines[i-1].index(" ")
        if(lines[i-1][:index] in keyword_terms):
          tab_prefix += 1
        tab=0
        while(tab < tab_prefix):
          lines[i] = "  "+lines[i]
          tab += 1
  return lines

def has_operator(line):
  # recognizes operator sanitizes operands, returns line (else return line)
  pass

def has_fun_call(line):
  # recognizes function call sanitizes parameters, returns line (else return line)
  pass
