# RoleSchemaAddPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | **List[str]** |  | 

## Example

```python
from users_client.models.role_schema_add_permission import RoleSchemaAddPermission

# TODO update the JSON string below
json = "{}"
# create an instance of RoleSchemaAddPermission from a JSON string
role_schema_add_permission_instance = RoleSchemaAddPermission.from_json(json)
# print the JSON string representation of the object
print(RoleSchemaAddPermission.to_json())

# convert the object into a dict
role_schema_add_permission_dict = role_schema_add_permission_instance.to_dict()
# create an instance of RoleSchemaAddPermission from a dict
role_schema_add_permission_from_dict = RoleSchemaAddPermission.from_dict(role_schema_add_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


