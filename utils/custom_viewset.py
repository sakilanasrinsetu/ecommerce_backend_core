from rest_framework import permissions, status, views, viewsets
from utils.response_wrapper import ResponseWrapper

from django.db.models import Q
from utils.actions import send_action

# .....***..... There is Checking lookup Field both for slug and pk or ID .....***.....

def object_get(object_qs , **kwargs):
    if kwargs.get("pk"):
        pk = kwargs["pk"]

        if not pk.isdigit():
            instance = object_qs.filter(slug__iexact = str(pk)).last()
        else:
            instance = object_qs.filter(pk = pk).last()
        
        return instance
        
    elif kwargs.get("slug"):
        slug = kwargs["slug"]

        if not slug.isdigit():
            instance = object_qs.filter(slug__iexact = slug).last()
        else:
            instance = object_qs.filter(pk = int(slug)).last()

        return instance
    
    else:
        return None
    
# .....***..... END There is Checking lookup Field both for slug and pk or ID .....***.....

class CustomViewSet(viewsets.ModelViewSet):
    lookup_field = 'pk' or "slug"

    # ..........***.......... Get All Data ..........***..........
    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        serializer_class = self.get_serializer_class()

        page_qs = self.paginate_queryset(qs)
        serializer = serializer_class(instance=page_qs, many=True)

        paginated_data = self.get_paginated_response(serializer.data)
        return ResponseWrapper(data=paginated_data.data, msg="Success", status=200)

    # ..........***.......... Create ..........***..........
    def create(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            qs = serializer.save(
                **request.data, 
                created_by=self.request.user
            )

            request_method = request.method
            request_url = request.build_absolute_uri()
            request_data = request.data 
            response_data = serializer.data

            # Save Logger for Tracking 
            
            send_action(qs, request_method, request_url,request_data, response_data)

            return ResponseWrapper(data=serializer.data, msg='created', status=200)
        else:
            return ResponseWrapper(error_msg=serializer.errors, error_code=400)

    # ..........***.......... Update ..........***..........

    def update(self, request, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data, partial=True)

        if serializer.is_valid():
            object_qs = self.queryset
            qs = object_get(object_qs, **kwargs)

            qs = serializer.update(instance=qs, validated_data=serializer.validated_data)

            try:
                if qs:
                    qs.updated_by_id = self.request.user.id
                    qs.save()
            except:
                qs = qs

            serializer = self.serializer_class(instance=qs)
            return ResponseWrapper(data=serializer.data)
        else:
            return ResponseWrapper(error_msg=serializer.errors, error_code=400)

    # ..........***.......... Delete ..........***..........

    def destroy(self, request, **kwargs):
        object_qs = self.queryset
        qs = object_get(object_qs, **kwargs)

        if qs:
            qs.delete()
            return ResponseWrapper(status=200, msg='deleted')
        else:
            return ResponseWrapper(error_msg="failed to delete", error_code=400)

    # ..........***.......... Get Single Data ..........***..........

    def retrieve(self, request, *args, **kwargs):
        object_qs = self.queryset
        qs = object_get(object_qs, **kwargs)
        if qs:
            serializer = self.get_serializer(qs)
            return ResponseWrapper(data = serializer.data, msg="Success")
        
        else:
            return ResponseWrapper(error_msg="Not found", error_code=404, status=404)
