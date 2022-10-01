a = 'run stream win '
print(a)

v1 = a.replace(" ", "ing ")                             # variant1
print('v1:', v1)

v2 = a[0:3]+'ing '+a[4:10]+'ing '+a[-4:-1]+'ing '      # variant2
print('v2:', v2)

v3 = 'ing '.join(a.split()) + 'ing'                    # variant3
print('v3:', v3)
