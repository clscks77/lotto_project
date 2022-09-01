from datetime import datetime
import requests
import numpy as np

def get_recent_round():
    """현재 시각을 기준으로 했을 때 가장 최신의 로또 회차 계산. 단, 로또 api 업데이트 기준을 20:50으로 함.
    Returns:
        가장 최신의 로또 회차
    """
    now = datetime.now()
    timestamp = now.timestamp()
    recent_round = (int)(timestamp - 1661633400)//604800 + 1030
    # 604800 = 일주일에 대한 timestamp 차이
    # 1661633400 = 2022-08-27 20:50:00에 대한 timestamp
    # 1030 = 그때 나온 최신 로또 회차
    # 20:50을 기준으로 하는 이유 = 추첨 후 5분쯤 지나면 api가 업데이트 돼있을 것 같아서
    return recent_round

def get_lotto_nums(round, bonus):
    """동행복권 API로 로또 번호 조회하기.
    Args:
        조회할 로또 회차, 보너스 포함 유무(on, None)
    Returns:
        해당 회차의 로또 번호 6개 리스트
    """
    drwtNos = []
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=' + str(round)
    res = requests.get(url)
    lottos = res.json()

    drwtNos.append(lottos['drwtNo1'])
    drwtNos.append(lottos['drwtNo2'])
    drwtNos.append(lottos['drwtNo3'])
    drwtNos.append(lottos['drwtNo4'])
    drwtNos.append(lottos['drwtNo5'])
    drwtNos.append(lottos['drwtNo6'])
    if bonus == 'on':
        drwtNos.append(lottos['bnusNo'])
    drwtNos.sort(reverse=True)
    return drwtNos

def get_checks_per_round(round, bonus):
    """회차별 당첨 번호 표시하기. 당청 -> ●
    Args:
        get_lotto_nums() -> 특정 회차의 당첨 번호
        보너스 포함 유무(on, None)
    Returns:
        특정 회차의 당첨 번호의 인덱스가 ●로 체크된 리스트
    """
    checks = []
    lotto_nums = get_lotto_nums(round, bonus)
    lotto_num = lotto_nums.pop()
    for num in range(46):
        if num == lotto_num:
            checks.append("●")
            if len(lotto_nums) != 0:
                lotto_num = lotto_nums.pop()
        else:
            checks.append("")
    return checks

def count_win_nums(nums_per_round):
    """번호 별 당첨 회수 리스트
    Args:
        회차별 당첨 번호가 ●로 체크된 이차원 리스트
    Returns:
        번호별 당첨 횟수에 대한 리스트. 인덱스 == 번호
    """
    count_per_num = [0] * 46
    for checks in nums_per_round:
        for index, check in enumerate(checks):
            if check == "●":
                count_per_num[index] = count_per_num[index] + 1
    return count_per_num

def index_for_desc(_list):
    """내림차순 정렬하는데, 값 대신 원래 인덱스 번호로 표시하기. 즉, 가장 많이 나온 번호부터 정렬됨.
    Args:
        정수 리스트
    Returns:
        내림차순에 대한 인덱스 리스트
    """
    result_list = []
    np_list = np.array(_list)
    np_list[0] = -1
    for i in range(45):
        max_idx = np.argmax(np_list)
        result_list.append(int(max_idx))
        np_list[max_idx] = -1
    return result_list