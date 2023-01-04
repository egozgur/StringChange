import fileinput
with fileinput.FileInput('line_wmkl_sonuc.xml', inplace=True) as file: #girdi olucak dosyanın tanımlandığı kısım  
    def my_function():
        for line in file:
          idas =  print('a',line.replace('LineStringSegment', 'LineString'))  #'LineStringSegment'= değiştirilmesi istenen kelime . 'LineString'=yerine gelmesi istenen kelime  
        return idas
my_function()

#herhangi bi text formatında olan dosyanın içerisindeki stringi, seçilen başka bir kelimeye çevirmeyi sağlar 