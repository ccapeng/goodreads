from django.shortcuts import render
from django.http import JsonResponse
from books import connector
from books import data_util

# Create your views here.
def search(request):
    query = request.GET.get("query")
    page = request.GET.get("page")
    status, result = connector.search_book(query, page)
    if status:
        data = data_util.parse_text(result)
        data['response'] = 'true'
        data['query'] = query
        data['page'] = page
        return JsonResponse(data)
    else:
        return JsonResponse({'response':'false'})


def page_not_found(request, Exception):
    response = render_to_response(
        '404.html',
        context_instance=RequestContext(request)
    )
    response.status_code = 404

    return response


def server_error(request):
    response = render_to_response(
        '500.html',
        context_instance=RequestContext(request)
    )
    response.status_code = 500

    return response