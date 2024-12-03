from django import template

register = template.Library()

@register.simple_tag(name="total")
def total(Cart):
    total=0
    for item in Cart:
        total+=item.Quantity*item.Price
    return total