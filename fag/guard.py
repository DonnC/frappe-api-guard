import frappe

def _is_desk_request():
    referer = frappe.request.headers.get("Referer", "")
    csrf_token = frappe.request.headers.get("X-Frappe-CSRF-Token")
    sid_cookie = frappe.request.cookies.get("sid")
    return ("/app/" in referer and sid_cookie) or csrf_token

def endpoint_guard():
    request_path = frappe.request.path  # e.g. '/api/method/myapp.api.fetch_res'

    if _is_desk_request():
        return
    
    guard = frappe.get_single("Endpoint Guard")
    if not guard.enabled:
        return
    
    allowed_paths = [row.endpoint.strip() for row in guard.endpoints]

    if request_path not in allowed_paths:
        frappe.local.response["http_status_code"] = 403
        frappe.local.response["message"] = "Access Denied: Endpoint not allowed"
        frappe.response.update(frappe.local.response)
        frappe.local.flags.stop_execution = True
        frappe.throw("Access Denied: Endpoint not allowed", frappe.PermissionError)
