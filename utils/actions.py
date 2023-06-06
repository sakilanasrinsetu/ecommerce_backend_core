import requests
from actstream import action
from actstream.models import Action
from rest_framework.request import Request

def send_action(qs, request_method, request_url, request_data, response_data, *args, **kwargs):
    if qs:
        public_ip = None
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            data = response.json()
            public_ip = data['ip']
            
        action.send(qs, verb=f"{public_ip}", action_object=qs, target=qs, description=f"Method: {request_method} URL-{request_url} \n\n Request Body is- \n {request_data} \n\n Response Body is- {response_data} \n\n Request from {public_ip}", url=request_url)

