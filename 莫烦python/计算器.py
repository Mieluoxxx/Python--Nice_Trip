class Calculator:
    def subtract(self, a, b):
        return a - b
    
    def batch_subtract(self, a_list, b_list):
        res_list = []
        for i in range(len(a_list)):
            res_list.append(self.subtract(a_list[i], b_list[i]))
        return res_list

c = Calculator()
print(c.subtract(2,1))
print(c.batch_subtract([3,2,1], [2,3,4]))
