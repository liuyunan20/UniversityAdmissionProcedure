my_str = list(input())
key_num = int(input())
key_bytes = key_num.to_bytes(2, byteorder="little")
key = sum(key_bytes)
str_bytes = [chr(ord(x) + key) for x in my_str]
print("".join(str_bytes))
