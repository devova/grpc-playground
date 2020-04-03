import purerpc
from purerpc_way import api_pb2
import google.protobuf.empty_pb2


class ChallengeServicer(purerpc.Servicer):
    async def create(self, input_message):
        raise NotImplementedError()

    async def bulk_create(self, input_messages):
        raise NotImplementedError()

    async def list(self, input_message):
        raise NotImplementedError()

    @property
    def service(self) -> purerpc.Service:
        service_obj = purerpc.Service(
            "challenges.Challenge"
        )
        service_obj.add_method(
            "create",
            self.create,
            purerpc.RPCSignature(
                purerpc.Cardinality.UNARY_UNARY,
                api_pb2.ChallengeRequest,
                api_pb2.ChallengeResponse,
            )
        )
        service_obj.add_method(
            "bulk_create",
            self.bulk_create,
            purerpc.RPCSignature(
                purerpc.Cardinality.STREAM_STREAM,
                api_pb2.ChallengeRequest,
                api_pb2.ChallengeResponse,
            )
        )
        service_obj.add_method(
            "list",
            self.list,
            purerpc.RPCSignature(
                purerpc.Cardinality.UNARY_STREAM,
                google.protobuf.empty_pb2.Empty,
                api_pb2.ChallengeResponse,
            )
        )
        return service_obj


class ChallengeStub:
    def __init__(self, channel):
        self._client = purerpc.Client(
            "challenges.Challenge",
            channel
        )
        self.create = self._client.get_method_stub(
            "create",
            purerpc.RPCSignature(
                purerpc.Cardinality.UNARY_UNARY,
                api_pb2.ChallengeRequest,
                api_pb2.ChallengeResponse,
            )
        )
        self.bulk_create = self._client.get_method_stub(
            "bulk_create",
            purerpc.RPCSignature(
                purerpc.Cardinality.STREAM_STREAM,
                api_pb2.ChallengeRequest,
                api_pb2.ChallengeResponse,
            )
        )
        self.list = self._client.get_method_stub(
            "list",
            purerpc.RPCSignature(
                purerpc.Cardinality.UNARY_STREAM,
                google.protobuf.empty_pb2.Empty,
                api_pb2.ChallengeResponse,
            )
        )


class Challenge2Servicer(purerpc.Servicer):
    async def create(self, input_message):
        raise NotImplementedError()

    @property
    def service(self) -> purerpc.Service:
        service_obj = purerpc.Service(
            "challenges.Challenge2"
        )
        service_obj.add_method(
            "create",
            self.create,
            purerpc.RPCSignature(
                purerpc.Cardinality.UNARY_UNARY,
                api_pb2.ChallengeRequest2,
                api_pb2.ChallengeResponse,
            )
        )
        return service_obj


class Challenge2Stub:
    def __init__(self, channel):
        self._client = purerpc.Client(
            "challenges.Challenge2",
            channel
        )
        self.create = self._client.get_method_stub(
            "create",
            purerpc.RPCSignature(
                purerpc.Cardinality.UNARY_UNARY,
                api_pb2.ChallengeRequest2,
                api_pb2.ChallengeResponse,
            )
        )