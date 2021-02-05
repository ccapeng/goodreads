import http.client
import os
import urllib

HOST = 'www.goodreads.com'
GOODREADS_KEY = os.environ.get("GOODREADS_KEY")

def search_book(query, page):

    method = 'GET'
    url = '/search/index.xml'

    result = ''
    status = False
    try:
        data = {
            'q': query,
            'page': page,
            'key': GOODREADS_KEY
        }
        url += "?" + urllib.parse.urlencode(data)
        conn = http.client.HTTPSConnection(HOST)
        conn.request(method, url)
        response = conn.getresponse()

        data = response.read()
        result = data.decode("utf-8")
        respStatus = response.status
        conn.close()

        if respStatus == 200:
            status = True
        else:
            status = False

    except Exception as e:
        print(e)
        #print("Err: {0} {1}".format(query, page))

    return status, result


if __name__ == "__main__": 
    status, result = search_book("holiday", 1)
    print(status)
    print(result)