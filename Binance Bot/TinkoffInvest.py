from config import token_tinkoff_full_rights
from openapi_client import openapi

client = openapi.api_client(token_tinkoff_full_rights)

pf = client.portfolio.portfolio_get()
print('value:', pf.payload.positions[0].average_position_price.value)
print('currency:', pf.payload.positions[0].average_position_price.currency)
print('balance:', pf.payload.positions[0].balance)
print('figi:', pf.payload.positions[0].figi)
print('ticker:', pf.payload.positions[0].ticker)
print('name:', pf.payload.positions[0].name)
