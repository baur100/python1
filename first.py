

def method(p):
    for x in p:
        if(x>2):
            print(x)

x = lambda y : y*2

print(x(11))

print(x(6))

number = lambda x,y,z : z*2+y*3+z*4

print(number(1,2,3))

spisok = [3,4,5,3,1,6]

double_it = list(map(lambda x: x-3, spisok))
print(double_it)
method(double_it)

months = ['jan', 'feb','may', 'mar', 'june','jul']
j_months = []
# j_months = list(filter(lambda z: z[0]=='j',months))
for x in months:
    if x[0]=='j':
        j_months.append(x)
m_months = list(filter(lambda v:len(v)==3,months))

print(m_months)
print(j_months)


