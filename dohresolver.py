import requests
from urllib.parse import urlsplit, urlunsplit

DOHRESOLVER = 'https://9.9.9.9:5053/dns-query' # this is quad9; also can use https://dns.google.com/resolve or cloudflare-dns.com (1.1.1.1:443)

def doh_resolve(host):
    rtis = requests.get(DOHRESOLVER, params={'name': host, 'type': 'A'}, headers={'accept': 'application/dns-json'})
    rtis.raise_for_status()
    tis = rtis.json()
    if 'Answer' in tis:
        return tis['Answer'][-1]['data']
    else:
        return None


class doh_session(requests.Session):
    def request(self, method, url, **kwargs):
        urlc = urlsplit(url)
        ip = doh_resolve(urlc.hostname)
        if urlc.port:
            new_netloc = ':'.join([ip, urlc.port])
        else:
            new_netloc = ip
        new_urlc = (urlc.scheme, new_netloc, urlc.path, urlc.query, urlc.fragment)
        new_url = urlunsplit(new_urlc)
        if 'headers' in kwargs:
            new_headers = kwargs['headers'].copy()
            if 'Host' in new_headers or 'host' in new_headers:
                pass
            else:
                new_headers['Host'] = urlc.hostname
            del kwargs['headers']
        else:
            new_headers = {'Host': urlc.hostname}
        #print(new_url)
        #print(new_headers)
        return super().request(method, new_url, headers = new_headers, **kwargs)


