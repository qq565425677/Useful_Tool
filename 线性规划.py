from scipy import optimize as op
import numpy as np
c=np.array([2,3,-5])                      #定义目标函数系数矩阵
A_ub=np.array([[-2,5,-1],[1,3,1]])        #定义不等式约束系数矩阵
B_ub=np.array([-10,12])                   #定义不等式约束右端项矩阵
A_eq=np.array([[1,1,1]])                  #定义等式约束系数矩阵
B_eq=np.array([7])                        #定义等式约束右端项矩阵
x1=(0,7)								  #定义变量x_1的范围
x2=(0,7)								  #定义变量x_2的范围
x3=(0,7)								  #定义变量x_3的范围
res=op.linprog(-c,A_ub,B_ub,A_eq,B_eq,bounds=(x1,x2,x3))   #调用函数进行求解
print(res)

'''https://blog.csdn.net/baidu_26746963/article/details/93903211'''