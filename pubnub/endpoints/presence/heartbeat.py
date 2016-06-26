from pubnub import utils
from pubnub.endpoints.endpoint import Endpoint
from pubnub.enums import HttpMethod, PNOperationType
from pubnub.errors import PNERR_CHANNEL_OR_GROUP_MISSING
from pubnub.exceptions import PubNubException


class Heartbeat(Endpoint):
    # /v2/presence/sub-key/<subscribe_key>/channel/<channel>/heartbeat?uuid=<uuid>
    HEARTBEAT_PATH = "/v2/presence/sub-key/%s/channel/%s/heartbeat"

    def __init__(self, pubnub):
        super(Heartbeat, self).__init__(pubnub)
        self._channels = []
        self._groups = []
        self._state = None

    def channels(self, channels):
        utils.extend_list(self._channels, channels)

        return self

    def channel_groups(self, channel_groups):
        utils.extend_list(self._groups, channel_groups)

        return self

    def state(self, state):
        self._state = state

        return self

    def http_method(self):
        return HttpMethod.GET

    def validate_params(self):
        self.validate_subscribe_key()

        if len(self._channels) == 0 and len(self._groups) == 0:
            raise PubNubException(pn_error=PNERR_CHANNEL_OR_GROUP_MISSING)

    def build_path(self):
        channels = utils.join_channels(self._channels)
        return Heartbeat.HEARTBEAT_PATH % (self.pubnub.config.subscribe_key, channels)

    def build_params(self):
        params = self.default_params()

        params['heartbeat'] = str(self.pubnub.config.presence_timeout)

        if len(self._groups) > 0:
            params['channel-group'] = utils.join_items(self._groups)

        if self._state is not None:
            params['state'] = utils.write_value_as_string(self._state)

        return params

    def create_response(self, envelope):
        return True

    def affected_channels(self):
        return None

    def affected_channels_groups(self):
        return None

    def operation_type(self):
        return PNOperationType.PNHeartbeatOperation

    def name(self):
        return "Heartbeat"