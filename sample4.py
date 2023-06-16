def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
status=int(input("enter a valid staus, 403,404,418"))
a=http_error(status)
print(a)
