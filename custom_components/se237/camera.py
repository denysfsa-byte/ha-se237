from homeassistant.components.camera import Camera
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

DOMAIN = "se237"

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    async_add_entities([SE237Camera(entry)])


class SE237Camera(Camera):
    def __init__(self, entry):
        super().__init__()
        self._entry = entry
        self._attr_name = "SE237 Camera"
        self._attr_unique_id = entry.entry_id

    async def async_camera_image(self, width=None, height=None):
        return None
