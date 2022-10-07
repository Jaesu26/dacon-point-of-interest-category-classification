def clean_texts(texts: Sequence[str]) -> List[str]: 
    new_texts = [] 
    for text in texts: 
        text = text.lower()
        text = re.sub(r'[^\s.]*\d+\.\d+[^\s.]*', '', text)  ## 소수점을 포함한 숫자단어 제거
        text = re.sub(r'[^\s.]*\d[^\s.]*', '', text)  ## 숫자를 포함한 단어 제거
        text = re.sub(r'[^\uAC00-\uD7A3\s.]', ' ', text)  ## 한글 음절, 공백, 마침표 제외하고 모두 삭제
        text = re.sub(r'\s+', ' ', text)  ## 다중 공백 제거
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
  
  
def major2minor(texts: Sequence[str], major2minor_dict: Dict[str, str]) -> List[str]:
    new_texts = []
    for text in texts:
        for major, minor in major2minor_dict.items():
            text = text.replace(major, minor)
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
        text = re.sub(r'\.+', '.', text) 
        new_texts.append(text)
    return new_texts
  
  
def delete_last_fullstop(texts: Sequence[str]) -> List[str]:
    new_texts = []
    for text in texts:
        if text.endswith('.'):
            text = text[:-1]
        new_texts.append(text)
    return new_texts
  
  
def delete_fullstops(texts: Sequence[str]) -> List[str]:
    new_texts = []
    for text in texts:
        text = re.sub(r'\.', ' ', text)   
        text = re.sub(r'\s+', ' ', text) 
        text = text.strip()     
        new_texts.append(text)
    return new_texts
  
  
def add_last_fullstop(texts: Sequence[str]) -> List[str]:
    new_texts = []
    for text in texts:
        if not text.endswith('.'):
            text = text + '.'
        new_texts.append(text)
    return new_texts
