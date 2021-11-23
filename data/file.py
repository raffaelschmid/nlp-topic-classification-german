import os

data_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(f"{data_dir}/..")
news_articles_raw_train = f"{root_dir}/data/raw/german_news_articles_raw_train.parq"
news_articles_raw_test = f"{root_dir}/data/raw/german_news_articles_raw_test.parq"

# raw: raw dataset (train and test joined)
news_articles_raw = f"{root_dir}/data/raw/german_news_articles_raw.parq"

# augmented: contains additional augmented rows
news_articles_augmented_only = f"{root_dir}/data/raw/german_news_articles_augmented_only.parq"
news_articles_augmented = f"{root_dir}/data/raw/german_news_articles_augmented.parq"

# cleaned: contains lemmatized, stemmed versions
news_articles_cleaned = f"{root_dir}/data/processed/german_news_articles_cleaned.parq"
news_articles_cleaned_train = f"{root_dir}/data/processed/german_news_articles_cleaned_train.parq"
news_articles_cleaned_test = f"{root_dir}/data/processed/german_news_articles_cleaned_test.parq"
news_articles_cleaned_val = f"{root_dir}/data/processed/german_news_articles_cleaned_val.parq"

# reporting data: contains a sampled expection, prediction and category mapping
reporting_data_report_tfidf = f"{root_dir}/data/processed/report_data_tfidf.json"
reporting_data_report_cnn = f"{root_dir}/data/processed/report_data_cnn.json"
reporting_data_report_rnn = f"{root_dir}/data/processed/report_data_rnn.json"
reporting_data_report_bert = f"{root_dir}/data/processed/report_data_bert.json"


# tokenized files for transformer input (hf=huggingface)
news_articles_hf_tokenized = f"{root_dir}/data/processed/german_news_articles_hf_tokenized.parq"
news_articles_hf_tokenized_train = f"{root_dir}/data/processed/german_news_articles_hf_tokenized_train.parq"
news_articles_hf_tokenized_test = f"{root_dir}/data/processed/german_news_articles_hf_tokenized_test.parq"
news_articles_hf_tokenized_val = f"{root_dir}/data/processed/german_news_articles_hf_tokenized_val.parq"