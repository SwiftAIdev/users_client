# PermissionSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID пользователя в системе | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** | Дата последнего обновления | [optional] 
**is_delete** | **bool** |  | [optional] [default to False]
**name** | **str** | Название разрешения | 

## Example

```python
from users_client.models.permission_schema import PermissionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionSchema from a JSON string
permission_schema_instance = PermissionSchema.from_json(json)
# print the JSON string representation of the object
print(PermissionSchema.to_json())

# convert the object into a dict
permission_schema_dict = permission_schema_instance.to_dict()
# create an instance of PermissionSchema from a dict
permission_schema_from_dict = PermissionSchema.from_dict(permission_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


