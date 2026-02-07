from puepy import Page, t
from puepy.runtime import is_server_side

from common import application

if not is_server_side:
    import js


@application.page("/community")
class CommunityPage(Page):
    DISCORD_URL = "https://discord.com/invite/Sc9XnqZj5a"

    def on_ready(self):
        js.window.location.href = self.DISCORD_URL
        return

    def populate(self):
        with t.div(classes=["redirect-container", "community-cover"]) as container:
            with t.div(class_="redirect-card"):
                t.div(class_="spinner")  # 로딩 애니메이션
                t.p("디스코드 커뮤니티로 이동하고 있습니다.")

                with t.p():
                    t.span("로딩이 안되면 ")
                    t.a("이 링크", href=self.DISCORD_URL, class_="manual-link")
                    t.span("를 클릭해주세요.")
