def bencode_str(t):
    r = ''
    length = int(chr(t[0]))
    for i in range(length):
        r += chr(t[i + 2])
    return r

def bencode_int(t):
    r = ''
    count = 1
    i = chr(t[count])
    while i != 'e':
        r += i
        count += 1
        i = chr(t[count])
    return int(r)
        
t_str = b'4:spam'
t_int = b'i3e'
t_list = b'l4:spam4:eggse'
t_dict = b'd3:cow3:moo4:spam4:eggse'

# STRING
r = bencode_str(t_str)
print(type(r))
print(r)

# INTEGER
r = bencode_int(t_int)
print(type(r))
print(r)

