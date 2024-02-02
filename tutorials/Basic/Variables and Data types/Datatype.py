# primitive
_boolean = True
print(type(_boolean))
_string = 'b'
print(type(_string))
_integer = 43
print(type(_integer))
_float = 34.43
print(type(_float))

#------------------------------------------------------------------------------------------------#
# not primitive or derived
_list = [_boolean, _string, _integer, _float] # dokan khata / chitha
_listOfList = ['string', _list]               # dokan khata with group
print(type(_list))
print(_list)
print(_listOfList)
_list.append("adding new item at the very end")# insert at end
_list.insert(2, "inserting at 2")              # insert at the given position
_list.pop()                                    # remove from end
_list.remove("inserting at 2")                 # remove all occurances of "inserting at 2"
_list.sort()
_list.reverse()
print(_list)


#------------------------------------------------------------------------------------------------#
_dictionary = {
    _boolean: "hello",
    "a": "A",
    "list": _list,
    "anotherDict": {
        "key": "value"
    },
    "listOfList": _listOfList
}
print(type(_dictionary))
print(_dictionary)
print(_dictionary["a"]) # get value of a respective key
_dictionary["a"] = "B"  # Modifying value of the respective key
_dictionary["c"] = "C"  # Adding a new key value pair to the dictionary
_dictionary["anotherDict"]["key"] = "Modified" # multi level access (ignore for now)
print(_dictionary)
# oxford dictionary - if there is a word in the dictionary it has to contain a meaning
# key in the dictionary can not be a list or a tuple or another dictionary

#------------------------------------------------------------------------------------------------#
_tuple = (_string, _dictionary, _string, _list, _listOfList)
print(type(_tuple))
print(_tuple)
# Immutatable datatype
# You can not chage its value at all