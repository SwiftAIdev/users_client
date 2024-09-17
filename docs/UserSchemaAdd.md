# UserSchemaAdd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**third_party_id** | **str** |  | 
**domain** | **str** |  | 
**is_integrator** | **bool** |  | [optional] [default to False]

## Example

```python
from users_client.models.user_schema_add import UserSchemaAdd

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaAdd from a JSON string
user_schema_add_instance = UserSchemaAdd.from_json(json)
# print the JSON string representation of the object
print(UserSchemaAdd.to_json())

# convert the object into a dict
user_schema_add_dict = user_schema_add_instance.to_dict()
# create an instance of UserSchemaAdd from a dict
user_schema_add_from_dict = UserSchemaAdd.from_dict(user_schema_add_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


