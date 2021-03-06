# 配列：データを一列に並べた変数

# data type
値の型整数型(int), 浮動小数点型(float), 文字列型(str)
# float can not be implicitedly converted to be string.
print("Median height of goalkeepers: " + str(np.median(gk_heights)))
print("Median height of goalkeepers: {0}".format(np.median(gk_heights)))

# データ構造
リスト、タプル、集合、辞書

"""list"""
city = ["Tokyo", "Kyoto", "Saporo", "Naha", "Sendai", "Hakata", "Nagoya"]
# show third one
print(city[2])
# change sixth one to "matuyama"
city[5] = "matuyama"
# add another list, should plus "[]"
city = city + ["hiroshima", "kanazawa"]
# repeat this list
city = city * 2
# retrieve a part of list
print(city[2:5])
# add an element to the end of list
print(city.append("Shibuya"))
# delete the last element of list
print(city.pop())
# delete a element of list by "index" and "same thing"
del city[1]
city.remove("Tokyo")
# Align this list
align = sorted(city)
print(align)


"""Tuple: a list cannot change element."""
# create tuple use "()" rather than "[]"
grade_tuple = (10,20,30)
# リストと相互に交換できる。convert tuple to list.
grade_list = list(grade_tuple)
# grade_tuple[0] = 89 will be "TypeError: 'tuple' object does not support item assignment"
# this is called immutable.


"""Set: a list have no same value"""
# create a set use "{}"
rank = {"A", "B"}
# also can convert from list


"""Dictionary: a list designate by "key" rather than "Index""""
# create a dictionary
joho_score = {"E0123":60, "T2468":90, "M8901":45}
print(joho_score["E0123"])


"""homework"""
# create a dictionary
flight = {"JL813":"TAIBEI", "CX567":"HONGKONG", "KE722":"SEOUL",
          "MU730":"SHANGHAI", "NH873":"HONGKONG", "MM23":"TAIBEI",
          "SQ619":"SINGAPORE", "BR131":"TAIBEI"}

print(flight["CX567"])

#convert dictionary to list
flight_list = list(flight.values())
#convert list to set
flight_set = set(flight_list)
print(flight_set)
