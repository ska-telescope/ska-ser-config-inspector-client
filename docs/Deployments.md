# Deployments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overall_health** | **str** |  | 
**instances** | [**Dict[str, DeploymentInstance]**](DeploymentInstance.md) |  | 

## Example

```python
from ska_ser_config_inspector_client.models.deployments import Deployments

# TODO update the JSON string below
json = "{}"
# create an instance of Deployments from a JSON string
deployments_instance = Deployments.from_json(json)
# print the JSON string representation of the object
print(Deployments.to_json())

# convert the object into a dict
deployments_dict = deployments_instance.to_dict()
# create an instance of Deployments from a dict
deployments_form_dict = deployments.from_dict(deployments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


