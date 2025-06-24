import json

from ....errors import ProofParseError
from ....embeddings.embedded_objects.circle import EmbeddedCircle
from ....embeddings.embedded_objects.line import EmbeddedLine
from ....embeddings.embedded_objects.point import EmbeddedPoint
from ....embeddings.embedded_objects.scalar import EmbeddedScalar
from ....embeddings.embedding import Embedding
from ....geometry_objects.geo_type import GeoType, Signature


class EmbeddingReader:
    """
    TODO: Document
    """

    signature: Signature

    def __init__(self, signature: Signature):
        self.signature = signature

    def read(self, data: list[str]) -> Embedding:
        """
        Parses the embedding section of the proof.
        """
        embedding = Embedding()
        for line in data:
            if not line.strip():
                continue
            name, data = line.split(':=')
            name = name.strip()
            data = json.loads(data)
            if name not in self.signature:
                raise ProofParseError(f'Embed given for unknown atom: {name}')
            embedded_object = None
            match self.signature[name]:
                case GeoType.POINT:
                    embedded_object = EmbeddedPoint.from_dict(data)
                case GeoType.LINE:
                    embedded_object = EmbeddedLine.from_dict(data)
                case GeoType.CIRCLE:
                    embedded_object = EmbeddedCircle.from_dict(data)
                case GeoType.ANGLE | GeoType.SCALAR:
                    embedded_object = EmbeddedScalar.from_dict(data)

            embedding[name] = embedded_object

        return embedding
