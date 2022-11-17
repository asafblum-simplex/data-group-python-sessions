items = {}


def h(slug: str):
    category, item = slug.split('.', 1)
    if category == 'vertices':
        items.setdefault(item, {})

    if category == 'edges':
        vert_a, vert_b = item.split("_to_", 1)
        items.setdefault(vert_b, set())
        items[vert_b].add(vert_a)


data = """
edges.bitcoin_address_to_payment
edges.phone_to_partner_end_user
edges.ip_to_payment
edges.creditcard_to_payment
edges.cookie_to_payment
edges.phone_to_payment
edges.email_to_payment
edges.payment_to_partner_end_user
edges.email_to_partner_end_user
edges.crypto_address_to_payment
vertices.crypto_address
vertices.cookie
vertices.ip
vertices.CreditCard
vertices.payment
vertices.email
vertices.phone
vertices.partner_end_user
vertices.bitcoin_address
"""

x = [h(s) for s in data.lower().split('\n') if s]
print(x)
