## 마침표 있는 경우: 1 fold(1), valid f1 score = 0.82216, public f1 score = 0.81782
## 마침표 없는 경우: 1 fold(1), valid f1 score = 0.81533, public f1 score = 0.81095


#---------------------------- functions ----------------------------#
## function6.py
  
  
#---------------------------- texts ----------------------------#    
## minor2major_dict3.py
train_texts = df['overview'].values
train_texts = minor2major(train_texts, minor2major_dict)
train_texts = clean_texts(train_texts)
train_texts = major2minor(train_texts, major2minor_dict)
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
NUM_EPOCHS = 30
MAX_LEN = 200  
BATCH_SIZE = 64
LEARNING_RATE = 5e-5
LABEL_SMOOTHING = 0.1  ## 잘못 라벨링된 데이터가 존재
SEED = 2022
drop_last = True  ## data loader

#---------------------------- transforms ----------------------------#  
None


## earlystop
patience = 7
monitor = 'f1_score'
mode = 'max'


## loss function
loss_fn = FocalLoss(alpha=0.25, gamma=2.5, label_smoothing=LABEL_SMOOTHING)


## optimizer, scheduler
optimizer = AdamW(model.parameters(), lr=LEARNING_RATE) 
t_total = len(train_dataloader) * NUM_EPOCHS  ## The total number of training steps
warmup_step = t_total // 10  ## The number of steps for the warmup phase
scheduler = get_cosine_schedule_with_warmup(optimizer, num_warmup_steps=warmup_step, num_training_steps=t_total)
