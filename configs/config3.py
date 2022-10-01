## 1 fold(1), valid f1 score = 0.82222, public f1 score = 0.81563
## 1 fold(2), valid f1 score = 0.83339, public f1 score = 0.81651
## 2 fold(1, 2), valid f1 score = (0.82222, 0.83339), public f1 score = 0.82102
## 5 fold, valid f1 score = (0.82222, 0.83339, 0.82561, 0.81729, 0.81679), public f1 score = 0.82649


#---------------------------- functions ----------------------------#
## function2.py
  
  
#---------------------------- texts ----------------------------#    
## minor2major_dict1.py
train_texts = df['overview'].values
train_texts = minor2major(train_texts, minor2major_dict)
train_texts = clean_texts(train_texts)
train_texts = cut_texts(train_texts, max_len=550)
train_texts = remove_fullstops(train_texts)


#---------------------------- parameters ----------------------------#  
MODEL_NAME = {'electra':'kykim/electra-kor-base', 'funnel':'kykim/funnel-kor-base'} 
MODEL_TYPE = 'electra'
MODEL_DEFAULT_WEIGHT_PATH = f'{MODEL_TYPE}_default_weight.pt' 
SAVE_PATH = './weight'
NUM_CLASSES = len(np.unique(target))  ## 128개
NUM_FOLDS = 5
NUM_EPOCHS = 30
MAX_LEN = 200  
BATCH_SIZE = 64
LEARNING_RATE = 5e-5
LABEL_SMOOTHING = 0.1  ## 잘못 라벨링된 데이터가 존재
SEED = 2022

## earlystop
patience = 4
monitor = 'f1_score'
mode = 'max'

## loss function
loss_fn = FocalLoss(alpha=0.25, gamma=5.0, label_smoothing=LABEL_SMOOTHING)

## optimizer, scheduler
optimizer = AdamW(model.parameters(), lr=LEARNING_RATE) 
t_total = len(train_dataloader) * NUM_EPOCHS  ## The total number of training steps
warmup_step = int(t_total * 0.1)  ## The number of steps for the warmup phase
scheduler = get_cosine_with_hard_restarts_schedule_with_warmup(optimizer, num_warmup_steps=warmup_step, num_training_steps=t_total)
