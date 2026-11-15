class ConfigurationError(Exception):
    pass


config = {}
try:
    url = config["database_url"]
except KeyError as original_err:
    raise ConfigurationError("Db URL cannot find") from original_err
