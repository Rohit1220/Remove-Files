import  os, shutil
path = 'C:\\Users\\Admin\\PythonProjects\\testFolder'
days = 30
SecondsPerDay = 86400
TotalSeconds = days * SecondsPerDay
print(TotalSeconds)
doespathexist = os.path.exists(path)
print(doespathexist)
if(doespathexist == 'True'):
    gotopath = os.walk(path)
    print(gotopath)
    os.path.join(path,gotopath)
    st_ctime = os.stat(path)
    print(st_ctime)
if (st_ctime > TotalSeconds):
    pathExist = os.path.exists(path)
    if(pathExist == True):
        os.remove(path)
    else:
        print("path not found")