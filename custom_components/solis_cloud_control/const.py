from logging import Logger, getLogger

import voluptuous as vol
from homeassistant.helpers import config_validation as cv

LOGGER: Logger = getLogger(__package__)

DOMAIN = "solis_cloud_control"

CONF_INVERTER_SN = "inverter_sn"

READ_SERVICE_NAME = "read"
READ_SERVICE_SCHEMA = vol.Schema(
    {
        vol.Required("client"): cv.string,
        vol.Required("cid"): cv.positive_int,
    }
)

CONTROL_SERVICE_NAME = "control"
CONTROL_SERVICE_SCHEMA = vol.Schema(
    {
        vol.Required("client"): cv.string,
        vol.Required("cid"): cv.positive_int,
        vol.Required("value"): cv.string,
    }
)

SET_STORAGE_MODE_SERVICE_NAME = "set_storage_mode"
SET_STORAGE_MODE_SERVICE_SCHEMA = vol.Schema(
    {
        vol.Required("client"): cv.string,
        vol.Required("storage_mode"): vol.In(["Self Use", "Feed In Priority"]),
        vol.Optional("battery_reserve", default="ON"): vol.In(["ON", "OFF"]),
        vol.Optional("allow_grid_charging", default="OFF"): vol.In(["ON", "OFF"]),
    }
)

SET_CHARGE_SLOT1_SERVICE_NAME = "set_charge_slot1"
SET_CHARGE_SLOT1_SERVICE_SCHEMA = vol.Schema(
    {
        vol.Required("client"): cv.string,
        vol.Required("from_time"): cv.time,
        vol.Required("to_time"): cv.time,
        vol.Optional("current"): vol.All(vol.Coerce(int), vol.Range(min=0, max=200)),
        vol.Optional("soc"): vol.All(vol.Coerce(int), vol.Range(min=0, max=100)),
    }
)

SET_DISCHARGE_SLOT1_SERVICE_NAME = "set_discharge_slot1"
SET_DISCHARGE_SLOT1_SERVICE_SCHEMA = vol.Schema(
    {
        vol.Required("client"): cv.string,
        vol.Required("from_time"): cv.time,
        vol.Required("to_time"): cv.time,
        vol.Optional("current"): vol.Coerce(int),
        vol.Optional("soc"): vol.Coerce(int),
    }
)

DISABLE_CHARGE_SLOT1_SERVICE_NAME = "disable_charge_slot1"
DISABLE_CHARGE_SLOT1_SERVICE_SCHEMA = vol.Schema(
    {
        vol.Required("client"): cv.string,
    }
)
DISABLE_DISCHARGE_SLOT1_SERVICE_NAME = "disable_discharge_slot1"
DISABLE_DISCHARGE_SLOT1_SERVICE_SCHEMA = vol.Schema(
    {
        vol.Required("client"): cv.string,
    }
)

API_BASE_URL = "https://www.soliscloud.com:13333"
READ_ENDPOINT = "/v2/api/atRead"
RESULT_ENDPOINT = "/v2/api/result"
CONTROL_ENDPOINT = "/v2/api/control"
API_TIMEOUT_SECONDS = 10
API_RETRY_COUNT = 3  # Initial attempt + 2 retries
API_RETRY_DELAY_SECONDS = 5  # Delay between retries
API_RESULT_ATTEMPTS = 10  # Number of attempts to fetch result data
API_RESULT_DELAY_SECONDS = 0.6  # Delay between result data fetch attempts

STORAGE_MODE_CID = 636
STORAGE_MODE_BIT_SELF_USE = 0
STORAGE_MODE_BIT_BACKUP_MODE = 4
STORAGE_MODE_BIT_GRID_CHARGING = 5
STORAGE_MODE_BIT_FEED_IN_PRIORITY = 6

CHARGE_SLOT1_TIME_CID = 5946
CHARGE_SLOT1_CURRENT_CID = 5948
CHARGE_SLOT1_SOC_CID = 5928

DISCHARGE_SLOT1_TIME_CID = 5964
DISCHARGE_SLOT1_CURRENT_CID = 5967
DISCHARGE_SLOT1_SOC_CID = 5965
