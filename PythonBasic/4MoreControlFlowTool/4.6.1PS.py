def http_error(status):
    match status:
        case 401 | 403 | 404:
            return "Not allowed"
        
http = http_error

print(http(403))