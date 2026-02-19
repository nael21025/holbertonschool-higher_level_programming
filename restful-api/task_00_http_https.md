# Task 0: Basics of HTTP/HTTPS

## Differences between HTTP and HTTPS

### HTTP (Hypertext Transfer Protocol)
- **Unencrypted**: Data is transmitted in plain text, visible to anyone eavesdropping
- **Port**: Typically uses port 80
- **Security**: No security mechanisms, vulnerable to man-in-the-middle attacks
- **Speed**: Slightly faster due to no encryption overhead
- **Use Case**: Non-sensitive information, public websites

### HTTPS (HTTP Secure)
- **Encrypted**: Uses SSL/TLS encryption to secure data
- **Port**: Typically uses port 443
- **Security**: Protected with certificates, verifies server identity
- **Speed**: Slightly slower due to encryption/decryption overhead
- **Use Case**: Sensitive data (banking, email, passwords, personal information)

### Key Security Differences
| Aspect | HTTP | HTTPS |
|--------|------|-------|
| Encryption | No | Yes (SSL/TLS) |
| Data Visibility | Plain text | Encrypted |
| Certificate | Not required | Required |
| Man-in-the-Middle Attack | Vulnerable | Protected |
| SEO Impact | Lower ranking | Better ranking |

---

## Structure of HTTP Request and Response

### HTTP Request Structure
```
METHOD /path HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: */*
Content-Length: 0

[Optional Body]
```

**Components:**
1. **Request Line**: METHOD PATH HTTP/VERSION
2. **Headers**: Key-value pairs providing metadata
3. **Blank Line**: Separates headers from body
4. **Body**: Optional data (usually for POST/PUT)

### HTTP Response Structure
```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234
Set-Cookie: sessionId=abc123

<html>
  <body>Response content here</body>
</html>
```

**Components:**
1. **Status Line**: HTTP/VERSION STATUS_CODE STATUS_MESSAGE
2. **Headers**: Key-value pairs with metadata
3. **Blank Line**: Separates headers from body
4. **Body**: Response data (HTML, JSON, etc.)

---

## Common HTTP Methods

| Method | Description | Use Case | Idempotent |
|--------|-------------|----------|-----------|
| **GET** | Retrieves data | Fetching a web page or API data | Yes |
| **POST** | Creates new resource | Submitting a form, creating new data | No |
| **PUT** | Replaces entire resource | Updating user profile completely | Yes |
| **PATCH** | Partially updates resource | Updating specific fields only | No |
| **DELETE** | Removes resource | Deleting a user or post | Yes |
| **HEAD** | Like GET but without body | Checking if resource exists, file size | Yes |
| **OPTIONS** | Describes communication options | CORS preflight requests | Yes |

---

## Common HTTP Status Codes

### 1xx - Informational (Request received, continuing process)
- **100 Continue**: Server received headers, continue sending body
- **101 Switching Protocols**: Switching to WebSocket or HTTP/2

### 2xx - Success (Request succeeded)
| Code | Name | Scenario |
|------|------|----------|
| **200** | OK | Request succeeded, data returned (GET) |
| **201** | Created | Resource created successfully (POST) |
| **202** | Accepted | Request accepted, processing (async jobs) |
| **204** | No Content | Success but no content to return (DELETE) |

### 3xx - Redirection (Further action needed)
| Code | Name | Scenario |
|------|------|----------|
| **301** | Moved Permanently | Resource permanently moved to new URL |
| **302** | Found | Temporary redirect to different URL |
| **304** | Not Modified | Cached resource is still valid |
| **307** | Temporary Redirect | Similar to 302 but preserves method |

### 4xx - Client Error (Request invalid or cannot be fulfilled)
| Code | Name | Scenario |
|------|------|----------|
| **400** | Bad Request | Invalid request syntax or parameters |
| **401** | Unauthorized | Authentication required but not provided |
| **403** | Forbidden | Authenticated but lacks permission |
| **404** | Not Found | Resource doesn't exist on server |
| **409** | Conflict | Request conflicts with existing resource |
| **429** | Too Many Requests | Rate limit exceeded |

### 5xx - Server Error (Server failed to fulfill valid request)
| Code | Name | Scenario |
|------|------|----------|
| **500** | Internal Server Error | Server encountered unexpected condition |
| **502** | Bad Gateway | Invalid response from upstream server |
| **503** | Service Unavailable | Server temporarily unavailable (maintenance) |
| **504** | Gateway Timeout | Upstream server didn't respond in time |

---

## Key Takeaways

1. **Always use HTTPS** for any sensitive information or production APIs
2. **HTTP methods** indicate the action: GET (fetch), POST (create), PUT/PATCH (update), DELETE (remove)
3. **Status codes** tell you the result: 2xx (success), 3xx (redirect), 4xx (client error), 5xx (server error)
4. **HTTP is stateless**: Each request is independent; use cookies/tokens for sessions
5. **Security first**: Encrypt sensitive data, validate inputs, authenticate users
