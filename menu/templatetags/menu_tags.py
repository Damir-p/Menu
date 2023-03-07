from django import template
from django.urls import reverse, resolve
from ..models import MenuItem, Menu

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu = Menu.objects.get(name=menu_name)
    request = context['request']
    current_path = request.path_info.lstrip('/')
    current_url_name = resolve(current_path).url_name
    
    def render_menu_item(menu_item):
        active = False
        if menu_item.url == current_path:
            active = True
        elif menu_item.url == reverse(current_url_name):
            active = True
        elif menu_item.url == reverse(current_url_name, args=()):
            active = True
        elif menu_item.url == reverse(current_url_name, kwargs=resolve(current_path).kwargs):
            active = True
        
        if active:
            css_class = 'active'
        else:
            css_class = ''
        
        if menu_item.children.count() > 0:
            return f'<li class="{css_class}">{menu_item.title}<ul>{"".join([render_menu_item(child) for child in menu_item.children.all()])}</ul></li>'
        else:
            return f'<li class="{css_class}"><a href="{menu_item.url}">{menu_item.title}</a></li>'
    
    return f'<ul>{"".join([render_menu_item(item) for item in menu.items.filter(parent=None)])}</ul>'

