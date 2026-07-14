from homeassistant import config_entries
import voluptuous as vol

DOMAIN = "se237"

class Se237ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(
                title="SE237",
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("device_id"): str,
                vol.Required("local_key"): str,
                vol.Required("ip"): str,
            }),
        )
