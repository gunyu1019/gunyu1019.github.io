from puepy import Application
from puepy.router import Router, Route


application = Application()
application.install_router(Router, link_mode=Router.LINK_MODE_HASH)
