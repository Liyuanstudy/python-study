arr = []
count = 0
sum = 0.0
while 1:
       val = input('请输入一个数：')
       try:
            if val == 'done':
                 for i in arr:
                       sum = sum + float(i)
                 print('total:' + str(sum))
                 print('count:' + str(count))
                 print('ave:' + str(sum/cpunt))pt
                 exit()
            else:
                  float(val)
                  arr.append(float(val))
                  count = count + 1
        except ValuaError:
            print('非法输入')
            print(ValueError)
pass
