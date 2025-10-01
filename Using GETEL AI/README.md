# Using GRETEL AI API for synsthetic data generation:

## Choosing the technique:
The appropriate synthetic data generation technique depends on your use case, data type, and goals. For simple datasets with well-defined statistical distributions, random data generation or rule-based generation can be sufficient. 

If you're dealing with complex, interrelated data or need to preserve relational integrity (e.g., in healthcare or finance), a simulation-based approach or generative models like GANs and VAEs might be more appropriate. Transformer-based models can provide better results for text generation or tasks involving large-scale data. 

Consider the trade-offs between ease of implementation, data realism, and computational requirements when choosing a technique.

## python implementation with GRETEL AI api:

To implement api, you must sign up in GRETEL AI website and obtain a api key.
Then install python package by running following command in the terminal:
 
 !pip install -U gretel-trainer

To implement this use case, we will use RelationalData from the gretel_trainer.relational module. It allows users to automatically define and maintain relationships between multiple tables, ensuring that foreign key dependencies and data integrity are preserved in the synthetic output. 

This is particularly useful for generating high-quality synthetic data that mirrors the structure and dependencies of real-world databases, making it easier to use in applications like machine learning, research, or compliance with data privacy regulations. 

## sample code base:

For the sample codebase, please refer to the generator.py program.
This code uses the Gretel.AI API to generate synthetic data for a relational database. It first sets up a session using an API key and loads three CSV files (patients, lab_results, and treatments), specifying their primary keys and defining foreign key relationships. 

The RelationalData class is used to maintain these relationships. After configuring the data, a model is trained using the MultiTable class, which synthesizes the entire relational dataset. 

After the model is trained, the generate() method is used to generate synthetic data. The record_size_ratio parameter determines the ratio reference to size of the generated data. record_size_ratio=1 means the number of records in synthetic dataset = original dataset i.e. 5,000 records.

## evaluation:

Evaluating the quality of synthetic data is essential to ensure its utility and privacy. Start by comparing statistical distributions between the original and synthetic data—metrics like mean, variance, and correlation should closely match. 

Another method is to use synthetic data to train machine learning models and compare their performance (e.g., accuracy or F1 score) to models trained on real data. 
