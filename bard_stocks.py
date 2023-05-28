import bardapi
import os
from dotenv import load_dotenv

load_dotenv()

def bardStocks(stocks, type):

    os.environ['_BARD_API_KEY'] = os.getenv('BARD_API_KEY')
    result = [stocks, type]

    input_text = stocks + "최근 시세 및 거래량, 전날 대비 등락율 등 전반적인 현재 상황은?"
    response = bardapi.core.Bard().get_answer(input_text)

    for i, choice in enumerate(response['choices']):
        if i == 0:
            result.append(choice['content'][0])



    # 질문작성
    input_text = "현재 주식 시장에서 " + type + "해서 본 " + stocks + "의 앞으로의 주식 전망은?"

    # 바드 대답
    response = bardapi.core.Bard().get_answer(input_text)

    for i, choice in enumerate(response['choices']):
        if i == 0:
            result.append(choice['content'][0])


    print(result)
    return result


if __name__ == '__main__':
    bardStocks('삼성 전자', "외국인 투자자와 기관 투자자 동향을 분석")