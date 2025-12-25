from puepy import Application, Page, t
from puepy.runtime import is_server_side
from puepy.util import jsobj

# noinspection PyUnresolvedReferences
import introduction
# noinspection PyUnresolvedReferences
import virtual_business_card
# noinspection PyUnresolvedReferences
import project

if not is_server_side:
    import js

application = Application()


@application.page()
class MainPage(Page):
    def populate(self):
        with t.div(classes=["swiper", "swiper-container"]):
            with t.div(classes=["swiper-wrapper"]):
                t.introduction(data_anchor="introduction", classes=["swiper-slide"])
                t.project(data_anchor="project", classes=["swiper-slide"])
                t.virtual_business_card(data_anchor="virtual_business_card", classes=["swiper-slide"])
            t.div(classes=["swiper-pagination"])
        return

    def on_ready(self):
        if is_server_side:
            return

        fullpage = js.Swiper.new(".swiper-container", jsobj(
            direction="vertical",
            simulateTouch=False,
            loop=False,
            slidesPerView=1,
            spaceBetween=0,
            mousewheel=True,
            pagination=jsobj(
                el=".swiper-pagination",
                clickable=True,
            )
        ))


application.mount("#app")
