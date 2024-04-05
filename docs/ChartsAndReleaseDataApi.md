# ska_ser_config_inspector_client.ChartsAndReleaseDataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_release_get**](ChartsAndReleaseDataApi.md#get_release_get) | **GET** / | Get Release
[**get_sub_chart_chart_name_get**](ChartsAndReleaseDataApi.md#get_sub_chart_chart_name_get) | **GET** /{chart_name} | Get Sub Chart
[**search_for_sub_charts_search_charts_get**](ChartsAndReleaseDataApi.md#search_for_sub_charts_search_charts_get) | **GET** /search-charts | Search For Sub Charts


# **get_release_get**
> ReleaseResponse get_release_get()

Get Release

Get main chart (Release) info and summary info for it's constituent sub charts.  :return: data about the current release :rtype: *schema.ReleaseResponse*

### Example


```python
import ska_ser_config_inspector_client
from ska_ser_config_inspector_client.models.release_response import ReleaseResponse
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
    api_instance = ska_ser_config_inspector_client.ChartsAndReleaseDataApi(api_client)

    try:
        # Get Release
        api_response = api_instance.get_release_get()
        print("The response of ChartsAndReleaseDataApi->get_release_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChartsAndReleaseDataApi->get_release_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ReleaseResponse**](ReleaseResponse.md)

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

# **get_sub_chart_chart_name_get**
> ChartResponse get_sub_chart_chart_name_get(chart_name)

Get Sub Chart

Get detail information about a given chart.  :param chart_name: the sub chart requiring more information :type chart_name: str :raises HTTPException: if the chart is not found :return: detail information about a given chart :rtype: schema.ChartResponse

### Example


```python
import ska_ser_config_inspector_client
from ska_ser_config_inspector_client.models.chart_response import ChartResponse
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
    api_instance = ska_ser_config_inspector_client.ChartsAndReleaseDataApi(api_client)
    chart_name = 'chart_name_example' # str | 

    try:
        # Get Sub Chart
        api_response = api_instance.get_sub_chart_chart_name_get(chart_name)
        print("The response of ChartsAndReleaseDataApi->get_sub_chart_chart_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChartsAndReleaseDataApi->get_sub_chart_chart_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart_name** | **str**|  | 

### Return type

[**ChartResponse**](ChartResponse.md)

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

# **search_for_sub_charts_search_charts_get**
> List[ChartResponse] search_for_sub_charts_search_charts_get(patterns=patterns)

Search For Sub Charts

Search the release's sub charts for any charts whose name fit the given pattern/s.  The pattern is a regex pattern and can be multiple instances if separated by \", \".  **Note**: if no arguments are given the server will return all the sub charts.  :param patterns: the subcharts matching the pattern/s     defaults to \"\" indicating all subcharts must be returned. :rtype patterns: str :return: a set of charts containing detail information for each chart. :rtype: set[schema.ChartResponse]

### Example


```python
import ska_ser_config_inspector_client
from ska_ser_config_inspector_client.models.chart_response import ChartResponse
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
    api_instance = ska_ser_config_inspector_client.ChartsAndReleaseDataApi(api_client)
    patterns = '' # str |  (optional) (default to '')

    try:
        # Search For Sub Charts
        api_response = api_instance.search_for_sub_charts_search_charts_get(patterns=patterns)
        print("The response of ChartsAndReleaseDataApi->search_for_sub_charts_search_charts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChartsAndReleaseDataApi->search_for_sub_charts_search_charts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patterns** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[ChartResponse]**](ChartResponse.md)

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

