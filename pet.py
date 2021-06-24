#%%

# 1. 판다스와 넘파이를 임포트하기
import pandas as pd
import numpy as np
from icecream import ic

if __name__ == '__main__':
    menu = input('1. 라이브러리 임포트\n'
                 '2. 판다스 버전 출력\n'
                 '3. 판다스 라이브러리 정보 모두 출력\n'
                 '4. 주어진 값으로 DataFrame 객체 생성\n'
                 '5. 객체 내부 정보 출력\n'
                 '6. 객체 상위 3열 출력\n'
                 '7. animal과 age 컬럼만 출력\n'
                 '8. 객체의 3,4, 8번의 animal과 age 값 출력\n'
                 '9. visits 컬럼에서 3 초과하는 값 출력\n'
                 '10. age에서 NaN 값 출력\n'
                 '11. age가 3 미만인 고양이만 출력\n'
                 '12. age가 2살 이상 4살 미만인 값 출력\n'
                 '13. f행의 나이를 1.5살로 변경\n'
                 '14. 객체에서 visit의 합 출력\n'
                 '15. 동물별로 나이의 평균 출력\n'
                 '16. k행을 추가하여 dog, 5.5세, 방문 횟수 2회, 우선권없음(no) 열 추가\n'
                 '16-1 방금 추가한 열 삭제\n'
                 '17. 객체에 있는 동물의 종류의 수 출력\n'
                 '18. age는 내림차순, visits는 오름차순으로 정렬\n'
                 '19. priority의 yes를 True, no를 Flase로 매핑 후 출력\n'
                 '20. snake를 python으로 값을 변경\n'
                 '21. 각각의 동물 유형과 방문 횟수에 대해, 평균나이를 찾으시오.'
                 )


    def quiz_2():
        # 2. 판다스 버전 체크하기
        ic(pd.__version__)


    # %%
    def quiz_3():
        # 3. 판다스 라이브러리 버전 정보 모두 출력하기
        pd.show_versions()


    # %%
    def quiz_4()
        # 4. DataFrame 만들기
        data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
                'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
                'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
        labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        df = pd.DataFrame(data, index=labels)


    # %%
    def quiz_5():
        # 5. 객체 내부 정보를 출력하시오
        df.info()
        # df.describe()


    # %%
    def quiz_6():
        # 6. 객체 상위 3열까지 출력하시오
        df.iloc[:, :3]


    # %%
    def quiz_7()
        # 7. animal과 age컬럼만 출력하시오
        df.loc[:, ['animal', 'age']]


    # %%
    def quiz_8():
        # 8. 객체의 3, 4, 8번 행에 해당하는 animal값과 age 값만 출력
        df.iloc[[3, 4, 8], [0, 1]]
        # df.loc[df.index[[3,4,8]], ['animal','age']]


    # %%
    def quiz_9():
        # 9. visit 컬럼에서 3 초과하는 값 출력
        df.loc[df['visits'] > 3]
        # df[df['visits']>3]


    # %%
    def quiz_10():
        # 10. age에서 NaN값 출력
        df.loc[:][df['age'].isna() == True]
        # df[df['age'] == NaN]


    # %%
    def quiz_11():
        # 11. age가 3살 미만 고양이값 출력
        df.loc[:][(df['age'] < 3) & (df['animal'] == 'cat')]
        # df[(df['age'] <3) & (df['animal'] =='cat')]


    # %%
    def quiz_12():
        # 12. age가 2살 이상 4살 미만인 값 출력
        df.loc[:][(df['age'] >= 2) & (df['age'] < 4)]
        # df[df['age'].between(2,4)]


    # %%
    def quiz_13():
        # 13. f 행의 나이를 1.5살로 변경
        # df.loc['f']['age'] = 1.5
        df.loc['f', 'age'] = 1.5
        df


    # type(df.loc['f']['age'])

    # %%
    def quiz_14():
        # 14. 객체에서 visit의 합 출력
        df['visits'].sum()


    # %%
    def quiz_15():
        # 15. 동물별로 나이 평균 출력
        df.groupby('animal')['age'].mean()


    # %%
    def quiz_16():
        # 16. k행을 추가하여 dog , 5.5세, 우선권없음(no), 방문회수 2회 열을 추가
        df.loc['k'] = ['dog', 5.5, 2, 'no']
        df


    # %%
    def quiz_16_1():
        # 16. 방금 추가한 열 삭제
        df.drop('k', inplace=True)
        df


    # %%
    def quiz_17():
        # 17. 객체에 있는 동물의 종류의 수 출력
        # len(df.groupby('animal').count())
        df['animal'].value_counts()


    # %%
    def quiz_18():
        # 18. age 는 내림차순, visits 는 오름차순으로 정렬
        df.sort_values(['age', 'visits'], ascending=[False, True])


    # %%
    def quiz_19():
        # 19. priority 의 yes를 True, no 를 False  로 맵핑 후 출력
        # df['priority'] =
        df['priority'].map({'yes': True, 'no': False})
        df


    # %%
    def quiz_20():
        # 20. snake 를 python 으로 값을 변경
        df['animal'].replace('snake', 'python')
        df


    # %%
    def quiz_21():
        # 21. 각각의 동물 유형과 방문 횟수에 대해, 평균나이를 찾으시오.
        # 즉,각 행은 animal 이고, 각 열은 visit 이며, 값은 평균연령
        # (힌트, 피벗 테이블을 활용해야 함)

        df.pivot_table(index='animal', columns='visits', values='age', aggfunc='mean')


    # %%

    while 1:
        select = input(select)
        if select == '0':
            break

        elif select == 2:
            quiz_2()

        elif select == 3:
            quiz_3()

        elif select == 4:
            quiz_4()

        elif select == 5:
            quiz_5()

        elif select == 6:
            quiz_6()

        elif select == 7:
            quiz_7()

        elif select == 8:
            quiz_8()

        elif select == 9:
            quiz_9()

        elif select == 10:
            quiz_10()

        elif select == 11:
            quiz_11()

        elif select == 12:
            quiz_12()

        elif select == 13:
            quiz_13()

        elif select == 14:
            quiz_14()

        elif select == 15:
            quiz_15()

        elif select == 16:
            quiz_16()

        elif select == 16_1:
            quiz_16_1()
            
        elif select == 17:
            quiz_17()

        elif select == 18:
            quiz_18()

        elif select == 19:
            quiz_19()

        elif select == 20:
            quiz_20()

        elif select == 21:
            quiz_21()


