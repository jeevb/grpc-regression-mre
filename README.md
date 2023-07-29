# GRPC Regression Minimal Reproducible Example

## Usage

```
$ make up
$ make -C echo .venv
$ source echo/.venv/bin/activate
$ SERVER_URL=localhost:8443 python echo/client.py
```

#### Expected

Using `grpcio==1.51.3`

```
E0728 20:36:16.829609000 8093441536 hpack_parser.cc:1218]              Error parsing metadata: error=invalid value key=content-type value=text/html
Traceback (most recent call last):
  File "/Users/jeev/Workspace/repos/personal/grpc-regression-mre/echo/client.py", line 27, in <module>
    main()
  File "/Users/jeev/Workspace/repos/personal/grpc-regression-mre/echo/client.py", line 22, in main
    response = stub.Echo(request)
  File "/Users/jeev/Workspace/repos/personal/grpc-regression-mre/echo/.venv/lib/python3.10/site-packages/grpc/_channel.py", line 946, in __call__
    return _end_unary_response_blocking(state, call, False, None)
  File "/Users/jeev/Workspace/repos/personal/grpc-regression-mre/echo/.venv/lib/python3.10/site-packages/grpc/_channel.py", line 849, in _end_unary_response_blocking
    raise _InactiveRpcError(state)
grpc._channel._InactiveRpcError: <_InactiveRpcError of RPC that terminated with:
  status = StatusCode.UNAUTHENTICATED
  details = "Received http2 header with status: 401"
  debug_error_string = "UNKNOWN:Error received from peer ipv6:%5B::1%5D:8443 {created_time:"2023-07-28T20:36:16.829747-07:00", grpc_status:16, grpc_message:"Received http2 header with status: 401"}"
```

#### Observed

Using `grpcio==1.56.2`

```
E0728 19:54:05.103107000 8093441536 hpack_parser.cc:991]               Error parsing 'content-type' metadata: invalid value
Traceback (most recent call last):
  File "/Users/jeev/Workspace/repos/personal/grpc-regression-mre/echo/client.py", line 27, in <module>
    main()
  File "/Users/jeev/Workspace/repos/personal/grpc-regression-mre/echo/client.py", line 22, in main
    response = stub.Echo(request)
  File "/Users/jeev/Workspace/repos/personal/grpc-regression-mre/echo/.venv/lib/python3.10/site-packages/grpc/_channel.py", line 1030, in __call__
    return _end_unary_response_blocking(state, call, False, None)
  File "/Users/jeev/Workspace/repos/personal/grpc-regression-mre/echo/.venv/lib/python3.10/site-packages/grpc/_channel.py", line 910, in _end_unary_response_blocking
    raise _InactiveRpcError(state)  # pytype: disable=not-instantiable
grpc._channel._InactiveRpcError: <_InactiveRpcError of RPC that terminated with:
    status = StatusCode.UNKNOWN
    details = "Stream removed"
    debug_error_string = "UNKNOWN:Error received from peer  {grpc_message:"Stream removed", grpc_status:2, created_time:"2023-07-28T19:54:05.10316-07:00"}"
```
