## ref: https://dacon.io/competitions/official/235884/codeshare/4754?page=1&dtype=recent
def clean_texts(texts: Sequence[str]) -> NDArray: 
    new_texts = [] 
    for text in texts: 
        text = re.sub(r'\w*\d\w*', '', text)         ## 숫자 단어 제거
        text = re.sub(r'<[^>]+>', '', text)          ## Html tags 제거
        text = re.sub(u'[\u4E00-\u9FA5]', '', text)  ## 한자 제거
        text = re.sub(r'[@%\\*=()/~#&\+á?\xc3\xa1\-\|\:\;\!\-\,\_\~\$\'\"\n\]\[\>\<]', ' ', text)   ## @%*=()/+ 와 같은 문장부호 제거(마침표 제외)
        text = re.sub(r'[^\uAC00-\uD7A30-9\s\.]', ' ', text)  ## 숫자, 한글 음절, 띄어쓰기, 마침표 제외하고 모두 삭제
        text = re.sub(r'\s+', ' ', text)      ## extra space 제거
        text = re.sub(r'^\s+', '', text)      ## space from start 제거
        text = re.sub(r'\s+$', '', text)      ## space from the end 제거
        new_texts.append(text) 
    new_texts = np.array(new_texts)
    return new_texts
  
def minor2major(texts: Sequence[str]) -> NDArray:
    new_texts = []
    for text in texts:
        text = text.replace('cafe', '카페')
        text = text.replace('까페', '카페')
        text = text.replace('5일장', '오일장')
        text = text.replace('ATV', '오토바이')
        text = text.replace('MTB', '산악자전거')
        new_texts.append(text)
    new_texts = np.array(new_texts)
    return new_texts  
  
def major2minor(texts: Sequence[str]) -> NDArray:
    new_texts = []
    for text in texts:
        text = text.replace('오일장', '5일장')
        text = text.replace('산악자전거', 'MTB')
        new_texts.append(text)
    new_texts = np.array(new_texts)
    return new_texts  
  
def cut_texts(texts: Sequence[str], max_len: int = 500) -> NDArray:
    new_texts = []
    for text in texts:
        full_stop_idx = [idx for idx, char in enumerate(text) if char == '.']
        if full_stop_idx:
            full_stop_idx = np.array(full_stop_idx)
            end_idx = full_stop_idx[full_stop_idx < max_len][-1]
        else:
            end_idx = len(text)
        new_texts.append(text[:end_idx])
    new_texts = np.array(new_texts)
    return new_texts 
   
def remove_fullstops(texts: Sequence[str]) ->  NDArray:
    new_texts = []
    for text in texts:
        text = re.sub(r'\.', '', text)       ## 마침표 제거 (word1~.~word2 -> word1~~word2)
        text = re.sub(r'\s+', ' ', text)     ## extra space 제거 (word1~~word2 -> word1~word2)
        new_texts.append(text)
    new_texts = np.array(new_texts)
    return new_texts
