    """
    base_url = "watchout4snakes.com"
    #base_url = "http://www.watchout4snakes.com"
    action_url = "/wo4snakes/Random/RandomWordPlus"
    params = urllib.urlencode({'Pos': 'n', 'Level': 20})
    #f = urllib.urlopen("http://www." + base_url + action_url, params)
    #f = urllib.urlopen(base_url + action_url, params)
    #print f.read()

    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    conn = httplib.HTTPConnection(base_url)
    conn.request("POST", action_url, params, headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    print data
    """


