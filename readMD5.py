import os,hashlib
path=input('path:')
file_name=input('filename:')
with open(os.path.join(path,file_name),'rb') as f:
    md5obj = hashlib.md5()
    md5obj.update(f.read())
    hash = md5obj.hexdigest()
    print('MD5:',hash)
input()