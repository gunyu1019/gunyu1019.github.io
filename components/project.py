import json
import random

from puepy import Component, t
from puepy.runtime import is_server_side
from puepy.util import jsobj

if not is_server_side:
    import js


@t.component()
class Project(Component):
    props = []

    def initial(self):
        f = open("project.json", mode="r", encoding='utf-8')
        project_info = json.load(f)
        f.close()

        shuffled_project_info = []
        while len(project_info) > 0:
            selected_project = random.randint(0, len(project_info) - 1)
            shuffled_project_info.append(project_info.pop(selected_project))
        return {
            "data": shuffled_project_info
        }

    def populate(self):
        with t.div(classes=["project"]):
            t.span("진행했던 여러 개인 프로젝트를 소개합니다!", classes=["container", "section-title"])

            with t.div(classes=["swiper", "swiper-project-container"]):
                with t.div(classes=["swiper-wrapper"]):
                    for project_data in self.state["data"]:
                        with t.div(classes=["swiper-slide"]):
                            with t.div(classes=["project-wrapper", "container"]):
                                if "image" in project_data.keys() and project_data["image"] is not None:
                                    t.img(src='assets/image/project/' + project_data["image"], classes=["project-image"])
                                with t.div(classes=["project-wrapper-content"]):
                                    with t.div(classes=["project-wrapper-title"]):
                                        t.span(project_data["title"], classes=["project-name"])
                                    t.span(project_data["date"], classes=["project-date"])
                                    t.span("\n".join(project_data["description"]), classes=["project-description"])
                                    with t.div(classes=["project-button-group"]):
                                        for raw_button_data in project_data["button"]:
                                            t.a(raw_button_data["title"], href=raw_button_data["url"], classes=["project-button"])
                t.div(classes=["swiper-scrollbar"])
                # t.div(classes=["swiper-button-prev"])
                # t.div(classes=["swiper-button-next"])

    def on_ready(self):
        if is_server_side:
            return

        project_swiper = js.Swiper.new(".swiper-project-container", jsobj(
            autoplay=jsobj(
                delay=10000
            ),
            direction="horizontal",
            simulateTouch=False,
            loop=True,
            slidesPerView=1,
            spaceBetween=0,
            scrollbar=jsobj(
                el=".swiper-scrollbar",
                draggable=True,
            ),
            keyboard=True
        ))