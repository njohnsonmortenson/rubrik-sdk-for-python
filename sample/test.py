import rubrik_cdm

node_ip = '[NODE]'
username = '[USERNAME]'
password = '[PASSWORD]'

rubrik = rubrik_cdm.Connect(node_ip, username, password)
print("Setting vars")
hostId = '[HostID]'
shareType = '[NFS/SMB]'
exportPoint = '[EXPORTPOINT]'

print("testing")
result = rubrik.new_NasShare(hostId, shareType, exportPoint)

print(result)