from redis import asyncio  # noqa
from redis.backoff import default_backoff
from redis.client import Redis, StrictRedis
from redis.cluster import RedisCluster
from redis.connection import (
    BlockingConnectionPool,
    Connection,
    ConnectionPool,
    SSLConnection,
    UnixDomainSocketConnection,
)
from redis.credentials import CredentialProvider, UsernamePasswordCredentialProvider
from redis.exceptions import (
    AuthenticationError,
    AuthenticationWrongNumberOfArgsError,
    BusyLoadingError,
    ChildDeadlockedError,
    ConnectionError,
    DataError,
    InvalidResponse,
    OutOfMemoryError,
    PubSubError,
    ReadOnlyError,
    RedisError,
    ResponseError,
    TimeoutError,
    WatchError,
)
from redis.sentinel import (
    Sentinel,
    SentinelConnectionPool,
    SentinelManagedConnection,
    SentinelManagedSSLConnection,
)
from redis.utils import from_url


def int_or_str(value):
    try:
        return int(value)
    except ValueError:
        return value


__version__ = "5.2.1"
VERSION = tuple(map(int_or_str, __version__.split(".")))


__all__ = [
    "AuthenticationError",
    "AuthenticationWrongNumberOfArgsError",
    "BlockingConnectionPool",
    "BusyLoadingError",
    "ChildDeadlockedError",
    "Connection",
    "ConnectionError",
    "ConnectionPool",
    "CredentialProvider",
    "DataError",
    "from_url",
    "default_backoff",
    "InvalidResponse",
    "OutOfMemoryError",
    "PubSubError",
    "ReadOnlyError",
    "Redis",
    "RedisCluster",
    "RedisError",
    "ResponseError",
    "Sentinel",
    "SentinelConnectionPool",
    "SentinelManagedConnection",
    "SentinelManagedSSLConnection",
    "SSLConnection",
    "UsernamePasswordCredentialProvider",
    "StrictRedis",
    "TimeoutError",
    "UnixDomainSocketConnection",
    "WatchError",
]
