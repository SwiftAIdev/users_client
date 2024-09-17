# PaginationRequestPermissionSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**size** | **int** |  | 
**total** | **int** |  | 
**data** | [**List[PermissionSchema]**](PermissionSchema.md) |  | 

## Example

```python
from users_client.models.pagination_request_permission_schema import PaginationRequestPermissionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationRequestPermissionSchema from a JSON string
pagination_request_permission_schema_instance = PaginationRequestPermissionSchema.from_json(json)
# print the JSON string representation of the object
print(PaginationRequestPermissionSchema.to_json())

# convert the object into a dict
pagination_request_permission_schema_dict = pagination_request_permission_schema_instance.to_dict()
# create an instance of PaginationRequestPermissionSchema from a dict
pagination_request_permission_schema_from_dict = PaginationRequestPermissionSchema.from_dict(pagination_request_permission_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


