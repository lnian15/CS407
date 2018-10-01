def encode(input_string):
  dict_char_tmp = {i:input_string.count(i) for i in input_string} 
 return dict_char_tmp