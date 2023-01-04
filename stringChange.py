#it allows to translate the string inside the file, which is in any text format, into another selected word
import fileinput
with fileinput.FileInput('<input_filename>', inplace=True) as file: #the part where the input file is defined  
    def my_function():
        for line in file:
          idas =  print('a',line.replace('<word_to_replace> ', '<replacement_word>'))  #'word_to_replace'= The word which wanted to change . 'replacement_word'=the word that is requested to come in its place  
        return idas

if __name__ == "__main__":
  my_function()
 