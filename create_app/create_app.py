from aiohttp import web


def create_app():
    return web.Application(debug=True)
