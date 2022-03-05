class ElevenstCV:
    INIT_URL = "https://www.11st.co.kr/AutoCompleteAjaxAction.tmall?method=getKeywordRankJson&type=hot&isSSL=Y&rankCnt=30&callback=fetchSearchRanking"
    HEADER_INFO = {
        "Content-Type": "application/x=www=form-urlencoded", 
        "Connection": "keep-alive", 
        "Accept-Encoding": "gzip, deflate, br", 
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
    }