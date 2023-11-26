import bencodepy, hashlib, requests

f = open("cold_fish.torrent", "rb")

t_all = bencodepy.decode(f.read())
t_announce = t_all[b'announce'].decode('utf-8')
t_info = t_all[b'info']
t_piece_length = t_info[b'piece length']
t_files = t_info[b'files']
t_total_size = 0

#print(f"IDENTIFIED {len(t_files)} FILES:", end='\n\n')
for file_ in t_files:
    #print(f"PATH: {file_[b'path']}")
    #print(f"LENGTH: {file_[b'length']} BYTES", end='\n\n')
    t_total_size += file_[b'length']

#print(f"PIECE LENGTH: {t_piece_length}")
#print(f"TOTAL SIZE: {t_total_size}")

info_hash = hashlib.sha1(bencodepy.encode(t_info)).digest()
peer_id = '0123456789testeteste'
port = 40459
uploaded = 0
downloaded = 0
left = t_total_size
corrupt = 0 # ?
key = 'D5A0B428' # ?
event = 'started'
numwant = 50
compact = 1
no_peer_id = 1
supportcrypto = 1 # ?????
redundant = 0 # ?

#response = requests.get(f'{t_announce}?info_hash={info_hash}&peer_id={peer_id}&port={port}&uploaded={uploaded}&downloaded={downloaded}&left={left}&corrupt={corrupt}&key={key}&event={event}&numwant={numwant}&compact={compact}&no_peer_id={no_peer_id}&supportcrypto={supportcrypto}&redundant={redundant}')
response = requests.get(t_announce, params={'info_hash':info_hash,'peer_id':peer_id,'port':port,'uploaded':uploaded,'downloaded':downloaded,'left':left,'corrupt':corrupt,'key':key,'event':event,'numwant':numwant,'compact':compact,'no_peer_id':no_peer_id,'supportcrypto':supportcrypto,'redundant':redundant})
print(response)
print(info_hash)
print(f'{t_announce}?info_hash={info_hash}&peer_id={peer_id}&port={port}&uploaded={uploaded}&downloaded={downloaded}&left={left}&corrupt={corrupt}&key={key}&event={event}&numwant={numwant}&compact={compact}&no_peer_id={no_peer_id}&supportcrypto={supportcrypto}&redundant={redundant}')
#print(response)
#print(response.text)