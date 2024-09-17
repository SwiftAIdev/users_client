# UserSchemaLogin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from users_client.models.user_schema_login import UserSchemaLogin

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaLogin from a JSON string
user_schema_login_instance = UserSchemaLogin.from_json(json)
# print the JSON string representation of the object
print(UserSchemaLogin.to_json())

# convert the object into a dict
user_schema_login_dict = user_schema_login_instance.to_dict()
# create an instance of UserSchemaLogin from a dict
user_schema_login_from_dict = UserSchemaLogin.from_dict(user_schema_login_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


