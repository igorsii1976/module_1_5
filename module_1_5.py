print()
immutable_var = (1,5,"name","Igor",True)
print("Immutable_var:",immutable_var)
#immutable_var [-1]= False
#TypeError: 'tuple' object does not support item assignment
#Ошибка сообщает, что кортеж не поддерживает изменение элементов, кортеж относится к неизменяемым типам данных
mutable_list = ([1,5,"name","Igor",True])
mutable_list [-1] = False
print("Mutable_list:",mutable_list)