## 1 fold(1), valid f1 score = 0.81186, public f1 score = 0.81010


#---------------------------- functions ----------------------------#
## function1.py
  
  
#---------------------------- texts ----------------------------#    
train_texts = df['overview'].values
train_texts = minor2major(train_texts)
# train_texts = remove_stopwords(train_texts, stopwords)
train_texts = clean_texts(train_texts)
train_texts = major2minor(train_texts)
train_texts = cut_texts(train_texts)
train_texts = remove_fullstops(train_texts)


#---------------------------- parameters ----------------------------#  
MODEL_NAME = {'electra':'kykim/electra-kor-base', 'funnel':'kykim/funnel-kor-base'} 
MODEL_TYPE = 'electra'
MODEL_DEFAULT_WEIGHT_PATH = f'{MODEL_TYPE}_default_weight.pt' 
SAVE_PATH = './weight'
NUM_CLASSES = len(np.unique(target))  
NUM_FOLDS = 5
NUM_EPOCHS = 30
MAX_LEN = 120  
BATCH_SIZE = 64
LEARNING_RATE = 5e-5
LABEL_SMOOTHING = 0.1
SEED = 2022

## earlystop
patience = 4
monitor = 'f1_score'
mode = 'max'
gamma = 5.0  ## focal loss

## optimizer, scheduler
optimizer = AdamW(model.parameters(), lr=LEARNING_RATE) 
t_total = len(train_dataloader) * NUM_EPOCHS  ## The total number of training steps
warmup_step = int(t_total * 0.1)  ## The number of steps for the warmup phase
scheduler = get_cosine_with_hard_restarts_schedule_with_warmup(optimizer, num_warmup_steps=warmup_step, num_training_steps=t_total)
