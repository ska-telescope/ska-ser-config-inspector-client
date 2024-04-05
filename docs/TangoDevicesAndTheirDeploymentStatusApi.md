# ska_ser_config_inspector_client.TangoDevicesAndTheirDeploymentStatusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_from_a_given_sub_chart_chart_name_device_name_get**](TangoDevicesAndTheirDeploymentStatusApi.md#get_device_from_a_given_sub_chart_chart_name_device_name_get) | **GET** /{chart_name}/{device_name} | Get Device From A Given Sub Chart
[**search_release_for_devices_search_devices_get**](TangoDevicesAndTheirDeploymentStatusApi.md#search_release_for_devices_search_devices_get) | **GET** /search-devices | Search Release For Devices
[**search_sub_chart_for_devices_chart_name_search_devices_get**](TangoDevicesAndTheirDeploymentStatusApi.md#search_sub_chart_for_devices_chart_name_search_devices_get) | **GET** /{chart_name}/search-devices | Search Sub Chart For Devices


# **get_device_from_a_given_sub_chart_chart_name_device_name_get**
> DeviceResponse get_device_from_a_given_sub_chart_chart_name_device_name_get(chart_name, device_name)

Get Device From A Given Sub Chart

Get a know device from a given subchart as defined in the path structure.  :param chart_name: the sub chart that contains the device :type chart_name: str :param device_name: the device name to be returned :type device_name: str :raises HTTPException: if the chart could not be found :return: the information about the given device (None if not found) :rtype: *Union[schema.DeviceResponse, None]

### Example


```python
import ska_ser_config_inspector_client
from ska_ser_config_inspector_client.models.device_response import DeviceResponse
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
    api_instance = ska_ser_config_inspector_client.TangoDevicesAndTheirDeploymentStatusApi(api_client)
    chart_name = 'chart_name_example' # str | 
    device_name = 'device_name_example' # str | 

    try:
        # Get Device From A Given Sub Chart
        api_response = api_instance.get_device_from_a_given_sub_chart_chart_name_device_name_get(chart_name, device_name)
        print("The response of TangoDevicesAndTheirDeploymentStatusApi->get_device_from_a_given_sub_chart_chart_name_device_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TangoDevicesAndTheirDeploymentStatusApi->get_device_from_a_given_sub_chart_chart_name_device_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart_name** | **str**|  | 
 **device_name** | **str**|  | 

### Return type

[**DeviceResponse**](DeviceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_release_for_devices_search_devices_get**
> List[DeviceResponse] search_release_for_devices_search_devices_get(patterns=patterns)

Search Release For Devices

Search a release for any devices whose name fit the given pattern/s.  :param patterns: the devices matching the pattern/s     defaults to \"\", indicating **all** devices must be returned. :type patterns: str :return: the information about the searched devices     (None if not found and all if no pattern given) :rtype: set[schema.DeviceResponse]

### Example


```python
import ska_ser_config_inspector_client
from ska_ser_config_inspector_client.models.device_response import DeviceResponse
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
    api_instance = ska_ser_config_inspector_client.TangoDevicesAndTheirDeploymentStatusApi(api_client)
    patterns = '' # str |  (optional) (default to '')

    try:
        # Search Release For Devices
        api_response = api_instance.search_release_for_devices_search_devices_get(patterns=patterns)
        print("The response of TangoDevicesAndTheirDeploymentStatusApi->search_release_for_devices_search_devices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TangoDevicesAndTheirDeploymentStatusApi->search_release_for_devices_search_devices_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patterns** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[DeviceResponse]**](DeviceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_sub_chart_for_devices_chart_name_search_devices_get**
> List[DeviceResponse] search_sub_chart_for_devices_chart_name_search_devices_get(chart_name, patterns=patterns)

Search Sub Chart For Devices

Search a given subchart for any devices whose name fit the given pattern/s.  The pattern is a regex pattern and can be multiple instances if separated by \", \".  **Note**: if no arguments are given the server will return all the devices.  :param chart_name: the sub chart that should contain the device :type chart_name: str :param patterns: the devices matching the pattern/s     defaults to \"\" indicating all devices must be returned. :rtype patterns: str, optional :return: the information about the searched devices     (None if not found and all if no pattern given) :rtype: set[schema.DeviceResponse]

### Example


```python
import ska_ser_config_inspector_client
from ska_ser_config_inspector_client.models.device_response import DeviceResponse
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
    api_instance = ska_ser_config_inspector_client.TangoDevicesAndTheirDeploymentStatusApi(api_client)
    chart_name = 'chart_name_example' # str | 
    patterns = '' # str |  (optional) (default to '')

    try:
        # Search Sub Chart For Devices
        api_response = api_instance.search_sub_chart_for_devices_chart_name_search_devices_get(chart_name, patterns=patterns)
        print("The response of TangoDevicesAndTheirDeploymentStatusApi->search_sub_chart_for_devices_chart_name_search_devices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TangoDevicesAndTheirDeploymentStatusApi->search_sub_chart_for_devices_chart_name_search_devices_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart_name** | **str**|  | 
 **patterns** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[DeviceResponse]**](DeviceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

