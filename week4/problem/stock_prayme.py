import collections

def solution(prices):
    answer = [0] * len(prices)

    deq = collections.deque()

    for idx, cur in enumerate(prices):

        if cur > deq[-1]:


        deq.append(idx)

    return answer
solution([1,2,3,2,3])

# 출석부에서 학과/학번/학년/이름/성별/참가시간/나간시간/기간
path = os.path.join(base_dir, 'a')
for file in os.listdir(path):
    csv = pd.read_csv(os.path.join(path, file), encoding='utf-8-sig')
    A = pd.read_csv(os.path.join(base_dir, "b/글로벌기업 취업스쿨_신청자리스트_sheet1.csv"))

    df = pd.DataFrame()
    for idx, row in csv.iterrows():
        df = pd.concat(
            [df, pd.concat([row, A.loc[A['이름'] == row['Name']]], axis=1))]
        )
        df.to_csv(os.path.join(base_dir, "result" + file), encoding='utf-8-sig')