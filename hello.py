def application(env, start_response):
    status = '200 OK'
    headers = {
        ('Content-Type', 'text/plain')
    }
    body = env['QUERY_STRING'].split('&')
    resp = ''
    for each in body:
        resp += each + '\n'
    start_response(status, headers)
    return [resp]
