

class BrowserHistory:
    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.cur_url, self.cur_url_numb = homepage, 0

    def visit(self, url: str) -> None:
        self.urls = self.urls[:self.cur_url_numb + 1]
        self.urls.append(url)
        self.cur_url, self.cur_url_numb = url, len(self.urls) - 1

    def back(self, steps: int) -> str:
        self.cur_url_numb = max(self.cur_url_numb-steps, 0)
        self.cur_url = self.urls[self.cur_url_numb]
        return self.cur_url

    def forward(self, steps: int) -> str:
        self.cur_url_numb = min(len(self.urls)-1, self.cur_url_numb+steps)
        self.cur_url = self.urls[self.cur_url_numb]
        return self.urls[self.cur_url_numb]




