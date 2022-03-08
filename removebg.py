# RemoveBG V1.0
# Karjok Pangesty
# March 8th, 2022 12:12 PM


# importing required modules
from requests import get, Session
from base64 import b64decode as decode
import re
import time
import random
import json
import os

# setting up the Session class
s = Session()
# if using local machine, use your custom proxy, otherwise, just comment code line bellow.
# s.proxies.update({"http":"http://165.22.59.84:8080"})

# setting Session headers
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
s.headers["x-requested-with"] = "XMLHttpRequest"
s.headers["origin"] = "https://www.remove.bg"

def download(new_img, path=None, filename=None):
    # If filename is not specified
    if filename is None:
        # Getting the default filename
        filename = new_img.split("/")[-1]

    # Send GET request to the result URL
    r = get(new_img, allow_redirects=True)
    
    # If path is not specified
    if path is None:
        path = os.path.join(os.getcwd(), filename)

    # Write to file
    with open (os.path.join(path, filename), 'wb') as image_file:
        image_file.write(r.content)
    

# Main function
def removeBg(file_source,delay=1):
    # get required csrf token for next process and then add it and referer to the session headers
    get_csrf = s.get("https://www.remove.bg/upload")
    time.sleep(delay)
    csrf = re.search(r"name\=\"csrf\-token\"\ content\=\"(.*?)\"",get_csrf.text).group(1)
    s.headers["x-csrf-token"] = csrf
    s.headers["referer"] = "https://www.remove.bg/upload"
    
    # requesting 'trust_token' from remove.bg server
    r = s.post("https://www.remove.bg/trust_tokens")
    use_token = re.search(r"ken\(\'(.*?)\'\)",r.text)
    
    # if remove.bg server allowing us to the next step of removing image background, it will give us the fucking 'trust_token'
    if use_token:
        # if source file is from url
        if "http" in file_source:
            file = get(file_source).content
        # and this is if file source is from local storage
        else:
            file = open(file_source,"rb")
        
        # get file name from file source
        filename = file_source.split("/")[-1] #"".join([random.choice(list("anjaymabarskuy1234567890")) for _ in range(1,15)])
        # preparing post forms
        form_data = {"trust_token":use_token.group(1)}
        form_files = {"image[original]":(filename,file,"multipart/form-data")}
        
        # sending the data & file, to get next process url
        time.sleep(delay)
        r = s.post("https://www.remove.bg/images",data=form_data,files=form_files)
        res_url = r.json()["url"]
        
        # get result url
        time.sleep(3)
        res = r = get(f"https://www.remove.bg{res_url}")
        
        # the final result (as json)
        result_json = json.loads(decode(res.json()["pl"]).decode("utf-8"))

        return result_json
    # if not, the fucking captcha will block us
    else:
        print("Invalid csrf or detected as spam")
        # print(r.text)

        return None

if __name__=="__main__":

    # delay paramenter is optional, default is 1
    # to reduce or avoid the risk of being blocked by fucking captcha

    # file source can be from local storage or url
    file_input = input("input image file source: ")
    remove = removeBg(file_input)
    print(remove)
