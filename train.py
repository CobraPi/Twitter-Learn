from TwitterBot import TwitterBot
from datetime import datetime


def train_new_cambrasine_model():
    current_time = datetime.now()
    bot = TwitterBot(embedding=True, model_layers=2)
    bot.read_corpus_file("data/cambrasine_tweets.txt")
    bot.set_outpufile("generated_text/generated_cambrasine_tweets(" + str(current_time) + ").txt")
    bot.build_embedding_model()
    bot.train()
    bot.save_model("models/Cambrasine_double_layer_embedding.h5")


def train_existing_cambrasine_model(filepath):
    current_time = datetime.now()
    bot = TwitterBot(embedding=True, model_layers=2)
    bot.read_corpus_file("data/cambrasine_tweets.txt")
    bot.set_outpufile("generated_text/generated_cambrasine_tweets(" + str(current_time) + ").txt")
    bot.load_saved_model(filepath)
    print("Training model:", filepath)
    bot.train()
    bot.save_model("models/Cambrasine_double_layer_embedding.h5")

if __name__ == "__main__":
    #train_new_cambrasine_model()
    train_existing_cambrasine_model("models/LSTM_MODEL_EMBEDDING_2_LAYERS-epoch009-words62992-sequence30-minfreq20-loss7.4443-acc0.1109-val_loss7.7539-val_acc0.1068")
