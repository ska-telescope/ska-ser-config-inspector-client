# ReleaseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart** | **str** |  | 
**version** | **str** |  | 
**sub_charts** | [**List[ChartSummary]**](ChartSummary.md) |  | 

## Example

```python
from ska_ser_config_inspector_client.models.release_response import ReleaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseResponse from a JSON string
release_response_instance = ReleaseResponse.from_json(json)
# print the JSON string representation of the object
print(ReleaseResponse.to_json())

# convert the object into a dict
release_response_dict = release_response_instance.to_dict()
# create an instance of ReleaseResponse from a dict
release_response_form_dict = release_response.from_dict(release_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


