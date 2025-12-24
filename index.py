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
        with t.div(id="container"):
            t.introduction(data_anchor="introduction")
            t.project(data_anchor="project")
            t.virtual_business_card(data_anchor="virtual_business_card")
        return

    def on_ready(self):
        if is_server_side:
            return
        pageable = js.Pageable.new("#container")
        pageable.on("scroll.start", self.on_scroll_start)
        pageable.on("scroll.end", self.on_scroll_end)

    def on_scroll_start(self, data):
        image_element = self.document.querySelector("div.introduction > img")
        if data["index"] == 0:
            image_element.style.display = "block"
            image_element.style.transform = "translateY(calc(100vh - 100%))"

    def on_scroll_end(self, data):
        image_element = self.document.querySelector("div.introduction > img")
        if data["index"] > 0:
            image_element.style.display = "none"
            image_element.style.transform = "translateY(-100vh)"


application.mount("#app")
