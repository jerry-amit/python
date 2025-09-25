def http_status(status):
    match status:
        case 200:
            return "OK"
        
        case 404:
            return "not Found"
        
        case 500:
            return "Internal server error"
        
        case _:
            
           return "unknown status"
       
print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(501 ))