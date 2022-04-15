key = int(input())
n = int(input())
end_str = ""
for i in range (n):
    char_decrypt = chr(ord(input())+key)
    end_str +=char_decrypt
print(end_str)
