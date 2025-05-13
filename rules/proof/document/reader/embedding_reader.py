import json

from rules.rule_utils import ProofParseError

from ....embeddings.embedded_objects.circle import EmbeddedCircle
from ....embeddings.embedded_objects.line import EmbeddedLine
from ....embeddings.embedded_objects.point import EmbeddedPoint
from ....embeddings.embedded_objects.scalar import EmbeddedScalar
from ....embeddings.embedding import Embedding
from ....geometry_objects.geo_object import GeoObject
from .. import rule_utils


class EmbeddingReader:
    def read(self, data: list[str], obj_map: dict[str, GeoObject]) -> Embedding:
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
            if name not in obj_map:
                raise ProofParseError(f'Embed given for unknown object: {name}')
            embedded_object = None
            match obj_map[name].type:
                case rule_utils.POINT:
                    embedded_object = EmbeddedPoint.from_dict(data)
                case rule_utils.LINE:
                    embedded_object = EmbeddedLine.from_dict(data)
                case rule_utils.CIRCLE:
                    embedded_object = EmbeddedCircle.from_dict(data)
                case rule_utils.ANGLE | rule_utils.SCALAR:
                    embedded_object = EmbeddedScalar.from_dict(data)

            embedding[name] = embedded_object

        return embedding
