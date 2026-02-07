from puepy import Component, t


@t.component()
class FooterComponent(Component):
    props = []

    def populate(self):
        with t.footer():
            with t.div(classes=["container", "footer-grid"]):
                with t.div(classes=["footer-item"]):
                    t.a("Yong Hyun, Lee", classes=["footer-topic"], href="https://yhs.kr/")
                    t.span("Copyright(©) 2022-present gunyu1019 All right reserved.", classes=["footer-description"])
                    t.a("통합 이용약관", href="#term", classes=["footer-link"])
                    t.span("Made by gunyu1019, powered by PuePy", classes=["footer-description"])
                with t.div(classes=["footer-item"]):
                    t.span("Recommend Project", classes=["footer-topic"])
                    with t.a(href="#community", classes=["footer-link"]):
                        t.i(classes=["fab", "fa-discord", "footer-image"])
                        t("Developer Space (Discord Community)")
                    with t.a(href="https://pubg.yhs.kr", classes=["footer-link"]):
                        t.i(classes=["fab", "fa-discord", "footer-image"])
                        t("PUBG BOT")
                    with t.a(href="https://play.google.com/store/apps/details?id=kr.yhs.traffic", classes=["footer-link"]):
                        t.i(classes=["fab", "fa-android", "footer-image"])
                        t("MyBUS")
                    with t.a(href="https://github.com/gunyu1019/chzzkpy", classes=["footer-link"]):
                        t.i(classes=["fab", "fa-python", "footer-image"])
                        t("chzzkpy")
                    with t.a(href="https://github.com/gunyu1019/chzzkpy", classes=["footer-link"]):
                        t.i(classes=["fas", "fa-map", "footer-image"])
                        t("Kakao Map SDK with Flutter")
        return
