# -*- coding: utf-8 -*-
import requests
class CompletionExecutor:
    def __init__(self, host, api_key, api_key_primary_val, request_id):
        self._host = host
        self._api_key = api_key
        self._api_key_primary_val = api_key_primary_val
        self._request_id = request_id

    def execute(self, completion_request, stream=False):
        headers = {
            'X-NCP-CLOVASTUDIO-API-KEY': self._api_key,
            'X-NCP-APIGW-API-KEY': self._api_key_primary_val,
            'X-NCP-CLOVASTUDIO-REQUEST-ID': self._request_id,
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'text/event-stream' if stream else 'application/json'
        }
        response = requests.post(self._host + '/testapp/v1/chat-completions/HCX-003',
                           headers=headers, json=completion_request, stream=False)
        return response.json()


class SlidingWindowExecutor:
    def __init__(self, host, api_key, api_key_primary_val):
        self._host = host
        self._api_key = api_key
        self._api_key_primary_val = api_key_primary_val

    def execute(self, completion_request):
        endpoint = '/v1/api-tools/sliding/chat-messages/HCX-003'
        headers = {
            'X-NCP-CLOVASTUDIO-API-KEY': self._api_key,
            'X-NCP-APIGW-API-KEY': self._api_key_primary_val,
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json'
        }
        response = requests.post(self._host + endpoint, headers=headers, json=completion_request, stream=False)

        return response.json()['result']['messages']