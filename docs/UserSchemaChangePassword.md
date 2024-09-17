# UserSchemaChangePassword


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_password** | **str** |  | 
**new_password** | **str** |  | 
**repeat_password** | **str** |  | 

## Example

```python
from users_client.models.user_schema_change_password import UserSchemaChangePassword

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaChangePassword from a JSON string
user_schema_change_password_instance = UserSchemaChangePassword.from_json(json)
# print the JSON string representation of the object
print(UserSchemaChangePassword.to_json())

# convert the object into a dict
user_schema_change_password_dict = user_schema_change_password_instance.to_dict()
# create an instance of UserSchemaChangePassword from a dict
user_schema_change_password_from_dict = UserSchemaChangePassword.from_dict(user_schema_change_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


