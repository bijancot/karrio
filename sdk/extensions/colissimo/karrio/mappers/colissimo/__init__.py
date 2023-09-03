
from karrio.core.metadata import Metadata

from karrio.mappers.colissimo.mapper import Mapper
from karrio.mappers.colissimo.proxy import Proxy
from karrio.mappers.colissimo.settings import Settings
import karrio.providers.colissimo.units as units


METADATA = Metadata(
    id="colissimo",
    label="Colissimo",
    # Integrations
    Mapper=Mapper,
    Proxy=Proxy,
    Settings=Settings,
    # Data Units
    is_hub=False
)
