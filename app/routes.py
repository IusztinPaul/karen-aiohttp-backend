# -*- coding: utf-8 -*-
from .views import CommandWebSocketView, StatusWebSocketView, HlsVideoView

ROUTERS = (
    ('GET', '/command', CommandWebSocketView, 'command_view'),
    ('GET', '/status', StatusWebSocketView, 'status_view'),
    ('GET', '/video', HlsVideoView, 'video_view'),
)


def setup(app):
    for method, path, handler, name in ROUTERS:
        app.router.add_route(method, path, handler, name=name)
