def is_informational(code):
    return code >= 100 and code <=199

def is_success(code):
    return code >= 200 and code <= 299

def is_redirect(code):
    return code >= 300 and code <= 399

def is_client_error(code):
    return code >= 400 and code <= 499

def is_server_error(code):
    return code >= 500 and code <= 599