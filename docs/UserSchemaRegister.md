# UserSchemaRegister


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from users_client.models.user_schema_register import UserSchemaRegister

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaRegister from a JSON string
user_schema_register_instance = UserSchemaRegister.from_json(json)
# print the JSON string representation of the object
print(UserSchemaRegister.to_json())

# convert the object into a dict
user_schema_register_dict = user_schema_register_instance.to_dict()
# create an instance of UserSchemaRegister from a dict
user_schema_register_from_dict = UserSchemaRegister.from_dict(user_schema_register_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


