import aiohttp


class TuyaAPI:

    def __init__(
        self,
        access_id,
        access_secret,
        device_id,
        region="us",
    ):
        self.access_id = access_id
        self.access_secret = access_secret
        self.device_id = device_id
        self.region = region

        self.token = None

    async def get_token(self):
        pass

    async def get_events(self):
        pass

    async def get_snapshot(self):
        pass