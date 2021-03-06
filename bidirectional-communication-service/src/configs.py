from os import getenv

SERVICE_RUNTIME = getenv('SERVICE_RUNTIME', 'locally')
SERVICE_PORT = int(getenv('SERVICE_PORT', 3001))
SERVICE_HOST = getenv('SERVICE_HOST', '0.0.0.0')

USER_MANAGEMENT_SERVICE_HOST = getenv('USER_MANAGEMENT_SERVICE_HOST', '0.0.0.0')
USER_MANAGEMENT_SERVICE_PORT = int(getenv('USER_MANAGEMENT_SERVICE_PORT', 3000))

CHECK_USER_CREDENTIALS_ROUTE = \
    f"http://{USER_MANAGEMENT_SERVICE_HOST}:{USER_MANAGEMENT_SERVICE_PORT}/users/check_credentials"
