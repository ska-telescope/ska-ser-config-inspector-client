# ChartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart** | **str** |  | 
**version** | **str** |  | 
**health** | **str** |  | 
**deployments** | [**Deployments**](Deployments.md) |  | 
**devices** | [**Devices**](Devices.md) |  | 

## Example

```python
from ska_ser_config_inspector_client.models.chart_response import ChartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChartResponse from a JSON string
chart_response_instance = ChartResponse.from_json(json)
# print the JSON string representation of the object
print(ChartResponse.to_json())

# convert the object into a dict
chart_response_dict = chart_response_instance.to_dict()
# create an instance of ChartResponse from a dict
chart_response_form_dict = chart_response.from_dict(chart_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


