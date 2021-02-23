def parse_input_data(data):
    result = {}
    if data:
        params = data.split('&')
        for item in params:
            k, v = item.split('=')
            result[k] = v
    return result


def get_wsgi_input_data(env) -> bytes:
    content_length_data = env.get('CONTENT_LENGTH')
    content_length = int(content_length_data) if content_length_data else 0
    data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
    return data


def parse_wsgi_input_data(data: bytes) -> dict:
    result = {}
    if data:
        data_str = data.decode(encoding='utf-8')
        result = parse_input_data(data_str)
    return result


def application(environ, start_response):
    data = get_wsgi_input_data(environ)
    data = parse_wsgi_input_data(data)
    print(data)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Hello from wsgi']
