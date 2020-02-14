from flask import Flask
from gql import Client
from gql.transport.requests import RequestsHTTPTransport

from config import DB_ENDPOINT

transport = RequestsHTTPTransport(
    url=DB_ENDPOINT,
    use_json=True,
)

client = Client(
    transport=transport,
    fetch_schema_from_transport=True,
)

app = Flask(__name__)

import routes