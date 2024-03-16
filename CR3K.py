import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from XRF64_XF import Main
 
        Main()
 
 
 
elif bit == "32bit":
 
        from XRF32_XF import Main
 
 
        Main()
 
