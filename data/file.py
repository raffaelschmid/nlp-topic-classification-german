import os

data_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(f"{data_dir}/..")
news_articles_raw_train = f"{root_dir}/data/raw/german_news_articles_raw_train.parq"
news_articles_raw_test = f"{root_dir}/data/raw/german_news_articles_raw_test.parq"

news_articles_cleaned = f"{root_dir}/data/processed/german_news_articles_cleaned.parq"
news_articles_cleaned_train = f"{root_dir}/data/processed/german_news_articles_cleaned_train.parq"
news_articles_cleaned_test = f"{root_dir}/data/processed/german_news_articles_cleaned_test.parq"
news_articles_cleaned_val = f"{root_dir}/data/processed/german_news_articles_cleaned_val.parq"

news_articles_hf_tokenized = f"{root_dir}/data/processed/german_news_articles_hf_tokenized.parq"
news_articles_hf_tokenized_train = f"{root_dir}/data/processed/german_news_articles_hf_tokenized_train.parq"
news_articles_hf_tokenized_test = f"{root_dir}/data/processed/german_news_articles_hf_tokenized_test.parq"
news_articles_hf_tokenized_val = f"{root_dir}/data/processed/german_news_articles_hf_tokenized_val.parq"