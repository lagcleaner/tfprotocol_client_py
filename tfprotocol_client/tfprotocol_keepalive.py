from tfprotocol_client.connection.protocol_client import ProtocolClient
from tfprotocol_client.misc.status_server_code import StatusServerCode
from tfprotocol_client.models.message import TfProtocolMessage


class TfProtocolKeepAliveWrapper:
    """This is an in progress class it is not finished yet, and it is intended to be used for
    some inner operations so far
    """

    def __init__(self, proto_client: ProtocolClient,) -> None:
        self._proto_client = proto_client

    @property
    def client(self):
        return self._proto_client

    def sha256_command(self, path: str) -> str:
        """Makes a sha256 hash of a file indicated by 'path'. This command is intended to apply
        a hash to a file before downloading it in order to guarantee its integrity. Be aware
        that on very large files the time to resolve the digest function could be potentially long.

        Args:
            `path` (str): The path to the target file.

        Returns:
            str: Response message.
        """
        return self.client.translate('SHA256', path).message

    def prockey_command(self) -> str:
        """Retrieves a unique key generated by the server's instance that communicates with the
        client. This unique key could be used later to identify that instance. One of these
        uses, but not the only one, is to test whether the server or even the socket communication
        line is still opened, in other words: the keepalive mechanism from the client side
        perspective.

        Returns:
            str: Response message that contains a unique key generated server side.
        """
        return self.client.translate('PROCKEY').message

    def keepalive_command(
        self, is_on: bool, time_connection: int, interval: int, count: int,
    ) -> bool:
        """Sets the configuration parameters for the TCP keepalive feature. This is especially
        useful for clients behind NAT boxes. If there is some idle time in the established
        connection -no data transmission- the NAT box could close or unset the connection
        without the peers knowing it. In contexts where it is predictable that an established
        connection could be 'in silent' for long periods of time, and it is possible that
        clients are behind NAT boxes, it is necessary to set the TCP keepalive packets.

        Args:
            `is_on` (bool): The first parameter of the command could be 0 or 1, meaning on or off.
            `time_connection` (int): The second parameter is the time (in seconds) the connection
                needs to remain idle before TCP starts sending keepalive probes.
            `interval` (int): The third parameter is the time (in seconds) between individual
                keepalive probes.
            `count` (int): The fourth parameter is the maximum number of keepalive probes TCP
                should send before dropping the connection.

        Returns:
            bool: Response message StatusServerCode.OK.
        """
        return self.client.translate(
            TfProtocolMessage(
                'KEEPALIVE',
                '1' if is_on else '0',
                str(time_connection),
                '|',
                str(interval),
                '|',
                str(count),
            )
        ).status is StatusServerCode.OK

    def date_command(self)->int:
        """Returns the number of elapsed seconds since the epoch, and arbitrary point
        in the time continuum, which is the Gregorian calendar time Jan 1 1970 00:00 UTC.

        Returns:
            int: Number of elapsed seconds since the epoch.
        """
        return int(self.client.translate('DATE').message)
