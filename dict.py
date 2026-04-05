sportdict = {'cricket':'Sri lanka',
             'football':'Brazil',
             'vollyball':'Argentina'}
print(sportdict)

sportdict.pop('football')
print(sportdict)
sportdict['football'] = 'America'
sportdict['football'] = 'USA'
print(sportdict)
iterator = 0
for item,value in sportdict.items():
    print(item, 'famous in' , value)
for a in sportdict.keys():

  iterator +=   1
  sportdict[a] = f'test ,{iterator}'

print(sportdict)
print()

class Median:
    
    marks = 0

    def __init__(self,examName):
       self.examName = examName
    
    def calculateMedian(self,**marks):
      self.marks = marks
      count = 0
      counter = 0
      for key, value in marks.items():
          count += value
          counter += 1
      return count/counter , self.examName

obj = Median('Python')
median = obj.calculateMedian(maths= 90, science = 79, english = 96)
#median = obj.calculateMedian(maths= 90, science = 79, english = 96)
print(median)
print(obj.examName)

print()

class MedianT:
    
    marks = 0

    def __init__(self,examName):
       self.examName = examName
    
    def calculateMedian(self,*marks):
      self.marks = marks
      count = 0
      counter = 0
      for value in marks:
          count += value
          counter += 1
      return count/counter , self.examName

obj = MedianT('Python')
median = obj.calculateMedian(90, 98,  97)
#median = obj.calculateMedian(maths= 90, science = 79, english = 96)
print(median)
print(obj.examName)