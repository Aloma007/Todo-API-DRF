from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomTodoPagination(PageNumberPagination):
    page_size = 10 # Default limit required by your guide
    page_size_query_param = 'limit' # Allows the client to request ?limit=20
    page_query_param = 'page' # Allows the client to request ?page=2

    def get_paginated_response(self, data):
        return Response({
            'data': data,
            'page': self.page.number,
            'limit': self.page.paginator.per_page,
            'total': self.page.paginator.count
        })