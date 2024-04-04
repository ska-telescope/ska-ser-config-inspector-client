# DeploymentInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** |  | 
**phase** | **str** |  | 

## Example

```python
from ska_ser_config_inspector_client.models.deployment_instance import DeploymentInstance

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentInstance from a JSON string
deployment_instance_instance = DeploymentInstance.from_json(json)
# print the JSON string representation of the object
print(DeploymentInstance.to_json())

# convert the object into a dict
deployment_instance_dict = deployment_instance_instance.to_dict()
# create an instance of DeploymentInstance from a dict
deployment_instance_form_dict = deployment_instance.from_dict(deployment_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


