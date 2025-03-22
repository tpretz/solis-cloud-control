from logging import Logger, getLogger

import voluptuous as vol
from homeassistant.helpers import config_validation as cv

LOGGER: Logger = getLogger(__package__)

DOMAIN = "solis_cloud_control"

CONF_INVERTER_SN = "inverter_sn"

READ_SERVICE_NAME = "read"
READ_SERVICE_SCHEMA = vol.Schema(
    {
        vol.Required("cid"): cv.positive_int,
    }
)

CONTROL_SERVICE_NAME = "control"
CONTROL_SERVICE_SCHEMA = vol.Schema(
    {
        vol.Required("cid"): cv.positive_int,
        vol.Required("value"): cv.string,
    }
)

API_BASE_URL = "https://www.soliscloud.com:13333"
READ_ENDPOINT = "/v2/api/atRead"
CONTROL_ENDPOINT = "/v2/api/control"
API_TIMEOUT_SECONDS = 10
API_RETRY_COUNT = 3  # Initial attempt + 2 retries
API_RETRY_DELAY_SECONDS = 5  # Delay between retries

