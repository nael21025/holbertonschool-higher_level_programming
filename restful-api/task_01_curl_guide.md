# Task 1: API Consumption using cURL

## Installing cURL

cURL is usually pre-installed on Linux/Mac. For Windows, you can use PowerShell or WSL.

To verify installation:
```bash
curl --version
```

## Basic cURL Syntax

```bash
curl [OPTIONS] [URL]
```

## Common cURL Flags

| Flag | Description |
|------|-------------|
| `-X METHOD` | Specify HTTP method (GET, POST, PUT, DELETE, etc.) |
| `-H "Header: value"` | Add custom header |
| `-d "data"` | Send data (usually with POST) |
| `-i` | Include response headers in output |
| `-I` | Show only response headers (no body) |
| `-o filename` | Save response to file |
| `-u username:password` | Basic authentication |
| `-b "cookie"` | Send cookies |
| `-L` | Follow redirects |
| `-w "%{http_code}"` | Show HTTP status code |

## Example Commands

### 1. Simple GET Request
```bash
curl https://jsonplaceholder.typicode.com/posts
```

### 2. Show Only Headers
```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

### 3. POST Request with Data
```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

### 4. POST with JSON Data
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"title":"foo","body":"bar","userId":1}' \
  https://jsonplaceholder.typicode.com/posts
```

### 5. GET with Custom Headers
```bash
curl -H "Authorization: Bearer token123" https://jsonplaceholder.typicode.com/posts/1
```

### 6. Pretty Print JSON Response
```bash
curl https://jsonplaceholder.typicode.com/posts/1 | python3 -m json.tool
```

### 7. Save Response to File
```bash
curl https://jsonplaceholder.typicode.com/posts -o posts.json
```

### 8. Show Status Code
```bash
curl -w "\nStatus: %{http_code}\n" https://jsonplaceholder.typicode.com/posts
```

## Example Output

When fetching from JSONPlaceholder:
```bash
$ curl https://jsonplaceholder.typicode.com/posts/1
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut et ipsa pecunia more..."
}
```

## Practice Exercises

1. Fetch all posts: `curl https://jsonplaceholder.typicode.com/posts`
2. Fetch specific post: `curl https://jsonplaceholder.typicode.com/posts/1`
3. Fetch comments: `curl https://jsonplaceholder.typicode.com/comments`
4. Fetch user data: `curl https://jsonplaceholder.typicode.com/users/1`
5. Create new post: `curl -X POST -d "title=test&body=test&userId=1" https://jsonplaceholder.typicode.com/posts`

## Key Points

- cURL is command-line tool for transferring data via URLs
- It supports HTTP, HTTPS, FTP, and other protocols
- Useful for testing APIs without writing code
- Can be integrated into scripts for automation
- Essential for debugging API issues
