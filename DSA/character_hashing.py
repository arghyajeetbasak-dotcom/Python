s="azyxyyzaaaa"
q=["d","a","y","x"]
# Method 1
# freq_map={}
# for char in s:
#     if(char in freq_map):
#         freq_map[char]+=1
#     else:
#         freq_map[char]=1
# for item in q:
#     if(item in freq_map):
#         print(freq_map[item])
#     else:
#         print(0)
# Method 2
hash_list=[0]*26
for char in s:
    ascii=ord(char)
    index=ascii-97
    hash_list[index]+=1
for item in q:
    ascii=ord(item)
    index=ascii-97
    print(hash_list[index])