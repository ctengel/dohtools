
#import requests_cache
import datetime
import time
#import requests
import dohresolver
import collections
import random
import re
import os
import urllib

def get_json(url):
    #requests_cache.install_cache('zzz_cache', expire_after=datetime.timedelta(hours=12))
    #start = time.time()
    #data = requests.get(url).json()
    #print('Got API in {} seconds.'.format(time.time() - start))
    #requests_cache.uninstall_cache()
    data = dohresolver.doh_session().get(url).json()
    return data

def split_data(data, by='bonusGroup'):
    result = collections.defaultdict(list)
    for d in data:
        result[d[by]].append(d)
    return result

def attempt_download(item, baseurl, dest):
    # TODO base_name from item
    file_name = dest + '/' + re.sub('[^\w.]', '_', base_name)
    if os.path.isfile(file_name):
        return -1
    url = '{}{}'.format(baseurl, urllib.parse.quote(base_name))
    print(url)
    r = requests.get(url, stream=True)
    if not r.ok or int(r.headers['content-length']) < 1024*1024:
        return 0
    with open(file_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1073741824):
            if chunk:
                f.write(chunk)
    return 1

def try_sub(subarea, base, dest, over=False):
    total = 0
    random.shuffle(subarea)
    for i in subarea:
        result = attempt_download(i, base, dest)
        if not result and not total and not over:
            return 0
        if result == 1:
            total = total + 1
    return total
    

def do_it(api, base, dest):
    data = split_data(get_json(api))
    total = 0
    for k, v in data.items():
        print(k)
        num_dl = try_sub(v, base, dest)
        total = total + num_dl
    return total



