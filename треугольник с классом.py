class Check_sum:                                                                  
    def __init__(self, X):                                                        
        self.summ = X                                                             
    def check(self, a, b, c):                                                     
            return ((a + b + c) == self.summ)                                     
tri = Check_sum(float(180))                                                       
print('Введите числа')                                                            
num1 = float(input())                                                             
num2 = float(input())                                                             
num3 = float(input())                                                             
if tri.check(num1, num2, num3) == True:                                           
    print('Это могут быть углы треугольника')                                     
else:                                                                             
    print('Это не могут быть углы треугольника')                                  
