from django.http import JsonResponse


def generate_json_response(is_success, data, message, status):
    response = {
        "is_success": is_success,
        "data": data,
        "message": message
    }
    return JsonResponse(response, status=status)
