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
                        project_unique_id = project_data["title"].replace(" ", "-") + "-modal"
                        with t.div(classes=["swiper-slide"]):
                            with t.div(classes=["project-wrapper", "container"]):
                                if "image" in project_data.keys() and project_data["image"] is not None:
                                    t.img(src='assets/image/project/' + project_data["image"], classes=["project-image"])
                                with t.div(classes=["project-wrapper-content"]):
                                    with t.div(classes=["project-wrapper-title"]):
                                        t.span(project_data["title"], classes=["project-name"])
                                    t.span(project_data["date"], classes=["project-date"])
                                    t.span("\n".join(project_data["description"]), classes=["project-description"])

                                    with t.a(classes=["project-description-more-button"], data_bs_toggle="modal", data_bs_target=f"#{project_unique_id}"):
                                        t("더보기 ")
                                        t.i(classes=["fas fa-angle-right"])

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
            # autoplay=jsobj(
            #     delay=10000
            # ),
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

        js.window.addEventListener("resize", self.on_resize)
        self.on_resize(None)

    def on_resize(self, _):
        if js.window.innerHeight / js.window.innerWidth > 1:  # 모바일 환경
            # document.querySelector('span.project-description').style.webkitLineClamp = 3 to PyScript
            wrapper_elements = js.document.querySelectorAll("div.project-wrapper")

            for index, element in enumerate(wrapper_elements):
                wrapper_content_element = element.querySelector(".project-wrapper-content")
                title_element = element.querySelector("span.project-name")
                date_element = element.querySelector("span.project-date")
                description_element = element.querySelector("span.project-description")
                description_more_button_element = element.querySelector("a.project-description-more-button")
                button_group_element = element.querySelector("div.project-button-group")

                is_image = element.querySelector("img.project-image") is not None

                actual_description_line_height = js.parseInt(js.window.getComputedStyle(description_element).lineHeight.replace("px", ""))
                actual_date_margin_bottom = js.parseInt(js.window.getComputedStyle(date_element).marginBottom.replace("px", ""))
                available_height = (
                    wrapper_content_element.offsetHeight
                    - title_element.offsetHeight
                    - date_element.offsetHeight
                    - actual_date_margin_bottom
                    - description_more_button_element.offsetHeight
                    - button_group_element.offsetHeight
                )
                if is_image:
                    available_height -= js.window.innerHeight * 0.3  # 이미지 크기 고려
                description_element.style.webkitLineClamp = available_height // actual_description_line_height
            # js.document.querySelector("span.project-description").style.webkitLineClamp = 3
            return
        return