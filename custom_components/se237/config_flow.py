import voluptuous as vol

from homeassistant import config_entries

DOMAIN = "se237"


class SE237ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(
                title="SE237",
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required("client_id"): str,
                    vol.Required("client_secret"): str,
                    vol.Required("device_id"): str,
                    vol.Required("region", default="us"): str,
                }
            ),
        )