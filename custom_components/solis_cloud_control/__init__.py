from homeassistant.const import CONF_API_KEY, CONF_TOKEN
from homeassistant.core import HomeAssistant, ServiceCall, ServiceResponse, SupportsResponse
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import aiohttp_client

from .api import SolisCloudControlApiClient, SolisCloudControlApiError
from .const import (
    CONF_INVERTER_SN,
    CONTROL_SERVICE_NAME,
    CONTROL_SERVICE_SCHEMA,
    DOMAIN,
    LOGGER,
    READ_SERVICE_NAME,
    READ_SERVICE_SCHEMA,
)


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    conf = config.get(DOMAIN, {})

    api_key = conf.get(CONF_API_KEY)
    api_token = conf.get(CONF_TOKEN)
    inverter_sn = conf.get(CONF_INVERTER_SN)

    if not api_key:
        LOGGER.error("Missing required configuration entry: %s", CONF_API_KEY)
        return False
    if not api_token:
        LOGGER.error("Missing required configuration entry: %s", CONF_TOKEN)
        return False
    if not inverter_sn:
        LOGGER.error("Missing required configuration entry: %s", CONF_INVERTER_SN)
        return False

    session = aiohttp_client.async_get_clientsession(hass)

    client = SolisCloudControlApiClient(api_key, api_token, inverter_sn, session)

    async def async_service_read(call: ServiceCall) -> ServiceResponse:
        cid = call.data.get("cid")
        try:
            result = await client.read(cid)
            LOGGER.info("Read state for '%s': '%s'", cid, result)
            return {"value": result}
        except SolisCloudControlApiError as err:
            raise HomeAssistantError(str(err)) from err

    async def async_service_control(call: ServiceCall) -> None:
        cid = call.data.get("cid")
        value = call.data.get("value")
        try:
            LOGGER.info("Control '%s' state with value: '%s'", cid, value)
            await client.control(cid, value)
        except SolisCloudControlApiError as err:
            raise HomeAssistantError(str(err)) from err

    hass.services.async_register(
        DOMAIN,
        READ_SERVICE_NAME,
        async_service_read,
        supports_response=SupportsResponse.ONLY,
        schema=READ_SERVICE_SCHEMA,
    )
    hass.services.async_register(
        DOMAIN,
        CONTROL_SERVICE_NAME,
        async_service_control,
        supports_response=SupportsResponse.NONE,
        schema=CONTROL_SERVICE_SCHEMA,
    )

    return True
