import time, os, shutil
path = 'C:\\Users\\Admin\\PythonProjects\\testFolder'
days = 30
print(days)
days = time.time()
print(days)
os.path.exists(path)
os.walk(path)
os.path.join(path)
st_ctime = os.stat(path)
if st_ctime > days:
    os.remove(path)