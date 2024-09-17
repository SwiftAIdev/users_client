# InviteUserSchemaAdd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**invite_code** | **str** |  | 

## Example

```python
from users_client.models.invite_user_schema_add import InviteUserSchemaAdd

# TODO update the JSON string below
json = "{}"
# create an instance of InviteUserSchemaAdd from a JSON string
invite_user_schema_add_instance = InviteUserSchemaAdd.from_json(json)
# print the JSON string representation of the object
print(InviteUserSchemaAdd.to_json())

# convert the object into a dict
invite_user_schema_add_dict = invite_user_schema_add_instance.to_dict()
# create an instance of InviteUserSchemaAdd from a dict
invite_user_schema_add_from_dict = InviteUserSchemaAdd.from_dict(invite_user_schema_add_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


