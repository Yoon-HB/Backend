import pandas as pd

labels_tree = ['나무전체', '기둥', '수관', '가지', '뿌리', '열매', '다람쥐', '나뭇잎', '꽃', '그네']
labels_person = ["사람전체", "머리", "얼굴", "눈", "코", "입", "귀", "머리카락", "목", "상체", "팔", "손", "다리", "발", "단추", "주머니", "운동화", "여자구두"]

def res_tree(df):
    global labels_tree

    res = ""
    index = list(df.index)
    col = list(df.columns)

    tree_size = 0

    for i, label in enumerate(labels_tree):
        num = index.count(i)
        if label == "나무전체":
            if num > 1:
                res += "외로움을 느끼는 경향이 있으며 이중자아를 나타낼 수 있는 특성이 나타납니다."
                
            if df.loc[i, "x"] <= 0.5:
                res += "내향적인 성향을 가지고 있으며 자존감이 낮고 부끄러움을 많이 느끼며 과거에 집착하는 경향이 있습니다. 또한 창의적이고 감수성이 풍부합니다."
            else:
                res += "미래를 중시하며 남성적인 특징을 가지고 있습니다. 또한 동질적 사고와 이질적 사고에 경계가 없으며, 타인에 대한 적대감이나 적대적 태도보다는 지적인 만족을 중시하는 경향이 있습니다."
            
            if df.loc[i, "y"] <= 0.5:
                res += "불안정하고 적절하지 않은 느낌을 자주 경험하며 우울하고 패배감을 갖는 경향이 있습니다."
            
            tree_size = df.loc[i, "w"] * df.loc[i, "h"]

        elif label == "기둥":
            if num == 0:
                res += "자아강도가 극도로 악되었거나 와해되어 정신증적 상태에 있다. 때로는 지나치게 부적절하다고 느끼며 자기를 억제하거나 피하는 경향이 강할 수 있습니다."

        elif label == "수관":
            if df.loc[i, "w"] * df.loc[i, "h"] <= tree_size // 2:
                res += "정서적으로 빈곤함을 느끼고 있는 모습이 보일 수 있습니다."
            else:
                res += "공상적인 면을 가지고 있지만 현실적인 전망이 부족하며, 환경에 대해 적극적으로 대응하고 때로는 공격적인 태도를 보일 수 있습니다."

        elif label == "가지":
            if num == 0:
                res += "세상과의 상호작용에 있어서 매우 억제되어 있는 것으로 보입니다."
            elif num > 5:
                res += "많은 일을 하고 싶어하며 대인 관계가 활발하지만 과도한 의욕을 보이는 경향이 있습니다."
            else:
                res += "세상과의 상호작용에 억제적인 경향이 있으며, 때때로 우울하거나 우울감을 느끼는 것으로 보입니다."

        elif label == "뿌리":
            continue

        elif label == "열매":
            res += "애정의 결핍의 모습이 나타나며 사랑과 관심에 대한 강한 욕구가 있는 것으로 보입니다."

        elif label == "그네":
            res += "우울함을 많이 느끼고 자주 외로움을 경험하는 경향이 있습니다."

    return res

def res_person(df):
    global labels_person

    res = ""
    index = list(df.index)
    col = list(df.columns)

    tree_size = 0

    # 클래스에 따른 해석 추가
    for i, label in enumerate(labels_person):
        num = index.count(i)

        if label =="사람전체":
            res += '클래스 0에 대한 해석'
        elif label == "머리":
            res += '클래스 1에 대한 해석'
        elif label == "얼굴":
            res += '클래스 2에 대한 해석'
        elif label == "눈":
            res += '클래스 3에 대한 해석'
        elif label == "코":
            res += '클래스 4에 대한 해석'
        elif label == "입":
            res += '클래스 5에 대한 해석'
        elif label == "귀":
            res += '클래스 6에 대한 해석'
        elif label == "머리카락":
            res += '클래스 7에 대한 해석'
        elif label == "목":
            res += '클래스 8에 대한 해석'
        elif label == "상체":
            res += '클래스 9에 대한 해석'
        elif label == "팔":
            res += '클래스 10에 대한 해석'
        elif label == "손":
            res += '클래스 11에 대한 해석'
        elif label == "다리":
            res += '클래스 12에 대한 해석'
        elif label == "발":
            res += '클래스 13에 대한 해석'
        elif label == "단추":
            res += '클래스 14에 대한 해석'
        elif label == "주머니":
            res += '클래스 15에 대한 해석'
        elif label == "운동화":
            res += '클래스 16에 대한 해석'
        elif label == "여자구두":
            res += '클래스 17에 대한 해석'


    return res