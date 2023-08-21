

class BrowserHistory:
    def __init__(self, homepage: str):
        self.urls = []
        self.urls.append(homepage)
        self.cur_url = homepage
        self.cur_url_numb = 0

    def visit(self, url: str) -> None:
        if url not in self.urls:
            self.urls.append(url)
            self.cur_url, self.cur_url_numb = url, len(self.urls) - 1
        else:
            for i in range(len(self.urls)):
                if self.urls[i] == url:
                    self.cur_url_numb = i
                    self.cur_url = self.urls[self.cur_url_numb]

    def back(self, steps: int) -> str:
        if steps > self.cur_url_numb:
            self.cur_url_numb = 0
        else:
            self.cur_url_numb -= steps
        self.cur_url = self.urls[self.cur_url_numb]
        return self.cur_url

    def forward(self, steps: int) -> str:
        if self.cur_url_numb + steps > len(self.urls) - 1:
            self.cur_url_numb = len(self.urls) - 1
        else:
            self.cur_url_numb += steps
        self.cur_url = self.urls[self.cur_url_numb]
        return self.urls[self.cur_url_numb]
