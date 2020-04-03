### GRPC Playground

Commands run generate stubs:

```bash
python -m grpc_tools.protoc -I . --python_out=mypy_way/ --mypy_out=mypy_way/ --python_grpc_out=mypy_way/ api.proto
python -m grpc_tools.protoc -I . --purerpc_out=purerpc_way/ --python_out=purerpc_way api.proto
python -m grpc_tools.protoc -I . --purerpc_out=. --python_out=. --python_betterproto_out=. api.proto
```

It is recommended to verify imports in generated files, e.g.
```python
# the line
import api_pb2

# should be
from purerpc_way import api_pb2
```