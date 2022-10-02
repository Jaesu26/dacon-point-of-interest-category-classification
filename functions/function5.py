def clean_texts(texts: Sequence[str]) -> List[str]: 
    new_texts = [] 
    for text in texts: 
        text = text.lower()
        text = re.sub(r'\w*\d\w*', '', text)  ## 숫자 단어 제거
        text = re.sub(r'[^\uAC00-\uD7A3\s\.]', ' ', text)  ## 한글 음절, 띄어쓰기, 마침표 제외하고 모두 삭제
        text = re.sub(r'\s+', ' ', text)  ## extra space 제거
        text = text.strip()   
        new_texts.append(text) 
    return new_texts
  
def minor2major(texts: Sequence[str], minor2major_dict: Dict[str, str]) -> List[str]:
    new_texts = []
    for text in texts:
        for minor, major in minor2major_dict.items():
            text = text.replace(minor, major)
        new_texts.append(text)
    return new_texts
  
def cut_texts(texts: Sequence[str], max_len: int = 550) -> List[str]:
    new_texts = []
    for text in texts:
        end_idx = len(text)
        full_stop_idx = [idx for idx, char in enumerate(text) if char == '.']
        if full_stop_idx:
            full_stop_idx = np.array(full_stop_idx)
            end_idxes = full_stop_idx[full_stop_idx < max_len].tolist()
            if end_idxes:
                end_idx = end_idxes[-1]
            else:
                end_idx = full_stop_idx[0]

        new_texts.append(text[:end_idx].strip())
    return new_texts
  
def delete_duplicate_fullstops(texts: Sequence[str]) -> List[str]:
    new_texts = []
    for text in texts:
        text = re.sub(r'\.+', '.', text)  ## 중복 마침표 제거 (word1~...~word2 -> word1~.~word2)
        new_texts.append(text)
    return new_texts
