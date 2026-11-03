
# HTTP (Hypertext Transfer Protocol)

HTTP is an application-layer protocol used for communication between clients and servers.

## Request and response

An HTTP communication typically consists of:

1. A client sends a request.
2. The server processes it.
3. The server returns a response.

## HTTP methods

| Method | Description |
|---|---|
| GET | Retrieve a resource |
| POST | Submit data |
| PUT | Replace a resource |
| PATCH | Partially modify a resource |
| DELETE | Remove a resource |
| HEAD | Retrieve headers without the response body |

## Status codes

| Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 301 | Moved Permanently |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |
| 503 | Service Unavailable |

## Example request

```http
GET / HTTP/1.1
Host: example.com
Accept: text/html
```

Example response:

```http
HTTP/1.1 200 OK
Content-Type: text/html
```

## Useful commands

Make a GET request:

```bash
curl https://example.com
```

Display response headers:

```bash
curl -I https://example.com
```

## HTTP vs HTTPS

- HTTP transmits application data without transport encryption.
- HTTPS uses TLS to protect communication between client and server.

!!! tip "Remember"
    HTTPS normally uses TCP port 443, while HTTP traditionally uses TCP port 80.

## References

- [RFC 9110 — HTTP Semantics](https://datatracker.ietf.org/doc/html/rfc9110)
- [MDN — HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)

