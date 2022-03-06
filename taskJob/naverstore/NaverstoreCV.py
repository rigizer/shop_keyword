class NaverstoreCV:
    INIT_URL = "https://search.shopping.naver.com/best/api/graphql"
    HEADER_INFO = {
        "Content-Type": "application/json", 
        "Connection": "keep-alive", 
        "Accept-Encoding": "gzip, deflate, br", 
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5", 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }