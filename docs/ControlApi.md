# ska_ser_config_inspector_client.ControlApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping_server_and_get_current_time_on_server_ping_get**](ControlApi.md#ping_server_and_get_current_time_on_server_ping_get) | **GET** /ping | Ping Server And Get Current Time On Server


# **ping_server_and_get_current_time_on_server_ping_get**
> PingResponse ping_server_and_get_current_time_on_server_ping_get()

Ping Server And Get Current Time On Server

Get a response from server to indicate it is available.  :return: the current time on the server. :rtype: *schema.PingResponse*

### Example


```python
import ska_ser_config_inspector_client
from ska_ser_config_inspector_client.models.ping_response import PingResponse
from ska_ser_config_inspector_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ska_ser_config_inspector_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ska_ser_config_inspector_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ska_ser_config_inspector_client.ControlApi(api_client)

    try:
        # Ping Server And Get Current Time On Server
        api_response = api_instance.ping_server_and_get_current_time_on_server_ping_get()
        print("The response of ControlApi->ping_server_and_get_current_time_on_server_ping_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ControlApi->ping_server_and_get_current_time_on_server_ping_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PingResponse**](PingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

