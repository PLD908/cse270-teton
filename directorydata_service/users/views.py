from django.http import JsonResponse

MAGIC_PASSWORD = "CSE270Rocks!"

# Optional headers for CORS
HEADERS = {
    "Cross-Origin-Opener-Policy": "unsafe-none",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"
}

def index(request):
    """
    Main endpoint for validating username/password.
    Returns 200 OK if valid, 401 if invalid.
    """
    username = request.GET.get("username")
    password = request.GET.get("password")

    # Valid login conditions
    if password == MAGIC_PASSWORD or (username == "admin" and password == "qwerty"):
        response = JsonResponse({"status": "ok"}, status=200)
    else:
        response = JsonResponse({"error": "unauthorized"}, status=401)
    
    # Add headers if needed
    for k, v in HEADERS.items():
        response[k] = v
    
    return response

def ingest(request):
    """
    Simple ingest endpoint for testing. Returns 200 with headers.
    """
    response = JsonResponse({"status": "ingested"}, status=200)
    for k, v in HEADERS.items():
        response[k] = v
    return response
