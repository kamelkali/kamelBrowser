from pypresence import Presence
import time


def discordRPC(self):
    self.client_id = "1263445543393431593"
    self.Rpc = Presence(self.client_id)
    self.Rpc.connect()


def discord_site_change(self):
    title = self.browser.page().title()
    if len(title) > 20:
        title = title[:20] + "..."
    print(title)
    if title:
        self.Rpc.update(
            large_image="ico",
            state=f"Napisane w PYQT5",
            large_text="Logo Kamel WebBrowser",
            party_id="ae488379-351d-4a4f-ad32-2b9b01c91657",
            details=f"Na stronie: {title}",
            start=int(time.time())
        )
        print("Zakturalizowano Status!")

    else:
        print(f"Nie wykryto żadnej strony !")
        self.Rpc.update(
            large_image="ico",
            state=f"Napisane w PYQT5",
            large_text="Logo Kamel WebBrowser",
            party_id="ae488379-351d-4a4f-ad32-2b9b01c91657",
            details=f"Na pustej stronie! ",
            start=int(time.time())
        )
        print("Zakturalizowano Status!")
