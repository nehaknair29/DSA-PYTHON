#dictionaries

info={"name":"John", "age":30, "city":"New York", "hobbies":"reading"}
print(info["name"])
print(info["age"])  
print(info["city"])
print(info["hobbies"])
#updating values
info["age"]=31
#update()
info.update({"age": 32})
print(info["age"])
#adding new key-value pair
info["country"]="USA"
print(info)
#removing key-value pair
del info["hobbies"]
print(info)
#pop()
info.pop("city")
print(info)
#popitem()
info.popitem()
print(info)
#clear()
info.clear()
print(info)
