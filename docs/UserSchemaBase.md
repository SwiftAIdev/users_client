# UserSchemaBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID пользователя в системе | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** | Дата последнего обновления | [optional] 
**is_delete** | **bool** |  | [optional] [default to False]
**surname** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**invite_code** | **str** |  | [optional] [default to '']
**third_party_id** | **str** |  | 
**is_active** | **bool** |  | [optional] [default to True]
**is_integrator** | **bool** |  | [optional] [default to False]

## Example

```python
from users_client.models.user_schema_base import UserSchemaBase

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaBase from a JSON string
user_schema_base_instance = UserSchemaBase.from_json(json)
# print the JSON string representation of the object
print(UserSchemaBase.to_json())

# convert the object into a dict
user_schema_base_dict = user_schema_base_instance.to_dict()
# create an instance of UserSchemaBase from a dict
user_schema_base_from_dict = UserSchemaBase.from_dict(user_schema_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


