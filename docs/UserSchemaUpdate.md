# UserSchemaUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**surname** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from users_client.models.user_schema_update import UserSchemaUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaUpdate from a JSON string
user_schema_update_instance = UserSchemaUpdate.from_json(json)
# print the JSON string representation of the object
print(UserSchemaUpdate.to_json())

# convert the object into a dict
user_schema_update_dict = user_schema_update_instance.to_dict()
# create an instance of UserSchemaUpdate from a dict
user_schema_update_from_dict = UserSchemaUpdate.from_dict(user_schema_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


