# 데이콘 2022 관광데이터 AI 경진대회

국문관광정보(POI)의 텍스트와 이미지데이터를 이용한 카테고리 자동분류 AI솔루션 개발

대회 링크: https://dacon.io/competitions/official/235978/overview/description

최종 순위: [48 / 290]

## 데이터 증강

`-` 클래스 불균형이 매우 심하여 균형있는 학습이 쉽지 않았다

`-` 클래스별 데이터의 개수를 맞춰주고자 EDA(Easy Data Augmentation) 기법 중에서 RS(Random Swap), RD(Random Deletion) 2가지 기법을 적용했다

`-` 클래스가 세부적으로 나뉜 관계로 유의어 대체는 모델에게 혼란을 줄 것 같아 수행하지 않았다 (자전거[자전거하이킹] $\rightleftarrows$ 오토바이[ATV])

`-` 마찬가지로, 무작위 단어 삽입 방법도 모델에게 혼달을 줄 것 같아 시도하지 않았음 (e.g. 클래스는 관광지인데 텍스트에서 관광지 근처에 산이 있다고 언급하는 경우) 

## 글의 일부분만 학습에 사용

`-` 클래스를 나타내는 단어는 글의 앞부분에 나타날 것이라 생각했고 데이터를 보니 실제로 그러한 경우가 대부분이었다

`-` 즉, 글을 끝까지 읽지 않아도 클래스를 구분할 수 있으므로 일정 글자수를 넘어가는 부분은 잘라내어 사용하지 않았다

`-` 이때, 단순히 임계치를 넘는다고 잘라내지 않고 임계치를 넘지 않는 마침표를 찾아 해당 마침표를 넘기는 지점부터 잘라냈다 (이로 인해 임계치로 의도한 글자수보다 더 많은 글자수를 설정해야 했다) 

`-` 장문의 경우 일부 문장만 사용해 학습 시간을 단축시킬 수 있었으며 모델의 정확도도 향상됐다

## 패인

`-` 라벨이 잘못 부여된 데이터가 많아 모델이 정확하게 학습하기 어려웠다 (잘못 부여된 라벨을 제대로 라벨링 했으면 성능이 향상됐을 것)

`-` 모델 입장에서 텍스트를 보고 클래스를 분류하기 어려운 경우가 꽤 있다 (e.g. 클래스는 호텔인데 텍스트에서 호텔 근처에 유명한 관광지가 있다고 언급하는 경우)  

`-` EDA 기법말고도 번역 후 재번역 등의 방법을 사용하여 텍스트를 증강할 수 있지만 증강하는데 시간이 오래걸려 사용하지 않았다 

