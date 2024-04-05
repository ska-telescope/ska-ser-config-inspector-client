# Devices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overall_health** | **str** |  | 
**states** | **Dict[str, str]** |  | 
**names** | **List[str]** |  | 

## Example

```python
from ska_ser_config_inspector_client.models.devices import Devices

# TODO update the JSON string below
json = "{}"
# create an instance of Devices from a JSON string
devices_instance = Devices.from_json(json)
# print the JSON string representation of the object
print(Devices.to_json())

# convert the object into a dict
devices_dict = devices_instance.to_dict()
# create an instance of Devices from a dict
devices_form_dict = devices.from_dict(devices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


