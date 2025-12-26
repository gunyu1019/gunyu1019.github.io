from puepy import Component, t


@t.component()
class VirtualBusinessCard(Component):
    props = []

    def populate(self):
        with t.div(classes=["virtual-business-card"]):
            t.span("궁금한 것이 있으면 언제든지 연락주세요!", classes=["container", "section-title"])

            with t.div(classes=["business-card"], ref="business-card"):
                with t.div(classes=["business-card-header"]):
                    t.span("이용현", classes=["business-card-header-title"])
                    t.span("Lee Yong Hyun", classes=["business-card-header-subtitle"])
                    t.img(src="assets/image/qr.png", classes=["business-card-qrcode"])
                with t.div(classes=["business-card-footer"]):
                    t.span("Software Engineer", classes=["business-card-footer-title"])
                    t.div(classes=["divider"])
                    with t.div(classes=["business-card-item"]):
                        t.i(classes=["fab fa-linkedin"])
                        t.a("in/gunyu1019", href="https://www.linkedin.com/in/gunyu1019")
                    with t.div(classes=["business-card-item"]):
                        t.i(classes=["fab fa-discord"])
                        t.a("@gunyu1019")
                    with t.div(classes=["business-card-item"]):
                        t.i(classes=["fab fa-github"])
                        t.a("gunyu1019", href="https://github.com/gunyu1019")
                    with t.div(classes=["business-card-item"]):
                        t.i(classes=["fas fa-envelope"])
                        t.a("gunyu1019@yhs.kr", href="mailto://gunyu1019@yhs.kr")

    def on_ready(self):
        self.refs["business-card"].add_event_listener(self.refs["business-card"].element, "mousemove", self.on_move_mouse)

    def on_move_mouse(self, offset):
        offset.preventDefault()
        rotate_x = (offset["layerX"] - 583.2 / 2) / (583.2 / 2)
        rotate_y = (offset["layerY"] - 928.8 / 2) / (928.8 / 2)
        self.refs["business-card"].element.style = (
            f"transform: rotate3D({rotate_y}, {rotate_x}, 0, -20deg);"
            f"box-shadow: {-rotate_x * 5}px {-rotate_y * 5}px #50505080;"
        )