class WebServerBadResponseError(Exception):
    def __init__(self, server, status_code):
        super().__init__(
            f'Server {server} returned bad status code.\nStatus code: {status_code}')


class WebServerBadContentError(Exception):
    def __init__(self, server, content):
        super().__init__(
            f'Server {server} returned bad date.\nReturned content: {content}')
