# Satellite API Microservices 

## Setup
```
$ git clone git@github.com:Satellite-App/SatelliteAPI.git
$ cd SatelliteAPI
$ python -m pip install grpcio-tools grpcio
```

## Usage

### Compiling .proto files for python services
From base directory run following commands:
```
python -m grpc_tools.protoc --proto_path=grpc --python_out=<service name> --pyi_out=<service name> --grpc_python_out=<service name>  grpc/proto/<extra path in proto for service>/<proto file>
```
