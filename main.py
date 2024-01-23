import bencodepy, hashlib, requests
from torrent_file import TorrentFile

# Read and decode all info from the desired .torrent file into t_all
f = open("test_torrent.torrent", "rb")
t_all = bencodepy.decode(f.read())
f.close()

# Create a TorrentFile object to store the decoded info from the file
torrent1 = TorrentFile(t_all)

# Parameters that will be sent when contacting the tracker
info_hash = hashlib.sha1(bencodepy.encode(torrent1.t_info)).digest()
peer_id = '0123456789testeteste'    # Unique ID for the client. Can be any 20-byte string
port = 6881                         # Desired port. Typically in 6881-6889 range
uploaded = 0                        # Bytes uploaded
downloaded = 0                      # Bytes downloaded
left = torrent1.t_total_size        # Total size - downloaded. Bytes
corrupt = 0                         # Not in specification. Found on qBitTorrent's GET when testing on Wireshark
key = 'D5A0B428'                    # Optional. Allows the client to prove it's identity
event = 'started'                   # started/stopped/completed. ?If none does not need to be specified?
numwant = 1                         # Desired number of peers
compact = 1                         # Indicates that the client accepts a compact response
no_peer_id = 1                      # Indicates that the tracker can omit the peer id field
supportcrypto = 1                   # Not in specification. Found on qBitTorrent's GET when testing on Wireshark
redundant = 0                       # Not in specification. Found on qBitTorrent's GET when testing on Wireshark

torrent1.print_all_info()

# Contacts the tracker
response = requests.get(torrent1.t_announce, params={'info_hash':info_hash,'peer_id':peer_id,'port':port,'uploaded':uploaded,'downloaded':downloaded,'left':left,'corrupt':corrupt,'key':key,'event':event,'numwant':numwant,'compact':compact,'no_peer_id':no_peer_id,'supportcrypto':supportcrypto,'redundant':redundant})
print(response)
print(response.text)

# Stores the tracker response containg the peers
response_decoded = bencodepy.decode(response.text)
print(response_decoded)