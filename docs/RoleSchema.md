# RoleSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID пользователя в системе | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** | Дата последнего обновления | [optional] 
**is_delete** | **bool** |  | [optional] [default to False]
**name** | **str** |  | [optional] 
**permissions** | [**List[PermissionSchema]**](PermissionSchema.md) |  | 

## Example

```python
from users_client.models.role_schema import RoleSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RoleSchema from a JSON string
role_schema_instance = RoleSchema.from_json(json)
# print the JSON string representation of the object
print(RoleSchema.to_json())

# convert the object into a dict
role_schema_dict = role_schema_instance.to_dict()
# create an instance of RoleSchema from a dict
role_schema_from_dict = RoleSchema.from_dict(role_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


