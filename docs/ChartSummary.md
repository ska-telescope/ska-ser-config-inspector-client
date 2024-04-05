# ChartSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from ska_ser_config_inspector_client.models.chart_summary import ChartSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ChartSummary from a JSON string
chart_summary_instance = ChartSummary.from_json(json)
# print the JSON string representation of the object
print(ChartSummary.to_json())

# convert the object into a dict
chart_summary_dict = chart_summary_instance.to_dict()
# create an instance of ChartSummary from a dict
chart_summary_form_dict = chart_summary.from_dict(chart_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


