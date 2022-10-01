## 1 fold(1), valid f1 score = 0.81748, public f1 score = 0.82085


#---------------------------- functions ----------------------------#
## function5.py
  
  
#---------------------------- texts ----------------------------#    
## minor2major_dict2.py
train_texts = df['overview'].values
train_texts = minor2major(train_texts, minor2major_dict)
train_texts = clean_texts(train_texts)
train_texts = cut_texts(train_texts, max_len=550)
train_texts = delete_duplicate_fullstops(train_texts)
train_texts = np.array(train_texts)


#---------------------------- parameters ----------------------------#  
MODEL_NAME = {'electra':'kykim/electra-kor-base', 'funnel':'kykim/funnel-kor-base'} 
MODEL_TYPE = 'electra'
MODEL_DEFAULT_WEIGHT_PATH = f'{MODEL_TYPE}_default_weight.pt' 
SAVE_PATH = './weight2'
NUM_CLASSES = len(np.unique(target))  ## 128개
NUM_FOLDS = 5
NUM_EPOCHS = 35
MAX_LEN = 150  
BATCH_SIZE = 64
LEARNING_RATE = 5e-5
LABEL_SMOOTHING = 0.1  ## 잘못 라벨링된 데이터가 존재
SEED = 2022


#---------------------------- transforms ----------------------------#  
## https://github.com/Jaesu26/text-augmentation
def get_transforms() -> A.Compose:
    transforms = A.Compose([
        RandomSwapSentences(p=0.5),
        RandomSwapWords(p=0.5),
        RandomDeletionSentences(min_sentences=3, deletion_prob=0.1, p=0.5),
        RandomDeletionWords(min_words_each_sentence=5, deletion_prob=0.1, p=0.5),
        DeletionFullstops()
    ])
    return transforms  ## 데이터 변환 방식을 반환

## earlystop
patience = 7
monitor = 'f1_score'
mode = 'max'

## loss function
loss_fn = FocalLoss(alpha=0.25, gamma=5.0, label_smoothing=LABEL_SMOOTHING)

## optimizer, scheduler
optimizer = AdamW(model.parameters(), lr=LEARNING_RATE) 
t_total = len(train_dataloader) * NUM_EPOCHS  ## The total number of training steps
warmup_step = int(t_total * 0.1)  ## The number of steps for the warmup phase
scheduler = get_cosine_with_hard_restarts_schedule_with_warmup(optimizer, num_warmup_steps=warmup_step, num_training_steps=t_total)
