from puepy import Application, Page, t
from puepy.runtime import is_server_side
from puepy.util import jsobj

# noinspection PyUnresolvedReferences
import introduction
# noinspection PyUnresolvedReferences
import virtual_business_card
# noinspection PyUnresolvedReferences
import project

import json

if not is_server_side:
    import js

application = Application()


@application.page()
class MainPage(Page):
    def initial(self):
        f = open("project.json", mode="r", encoding='utf-8')
        project_info = json.load(f)
        f.close()
        return {
            "data": project_info
        }

    def populate(self):
        with t.div(classes=["swiper", "swiper-container"]):
            with t.div(classes=["swiper-wrapper"]):
                t.introduction(data_anchor="introduction", classes=["swiper-slide"])
                t.project(data_anchor="project", classes=["swiper-slide"])
                t.virtual_business_card(data_anchor="virtual_business_card", classes=["swiper-slide"])
            t.div(classes=["swiper-pagination"])

        # Modal for long project description
        with t.div(classes=["modal-group"]):
            for project_data in self.state["data"]:
                project_unique_id = project_data["title"].replace(" ", "-") + "-modal"
                with t.div(classes=["modal fade"], tabindex="-1", id=project_unique_id,
                           aria_labelledby=f"{project_unique_id}_label", aria_hidden="true"):
                    with t.div(classes=["modal-dialog modal-dialog-centered modal-lg"]):
                        with t.div(classes=["modal-content"]):
                            with t.div(classes=["modal-header"]):
                                t.h5(project_data["title"], classes=["modal-title"], id=f"{project_unique_id}_label")
                                t.button(classes=["btn-close"], data_bs_dismiss="modal", aria_label="Close")
                            with t.div(classes=["modal-body"]):
                                t.p("\n".join(project_data["description"]))
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
