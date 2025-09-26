# Method 2: Rule-based generator:

Rule-based methods use predefined rules or domain knowledge to create data with specific characteristics.

The Python code above generates a dataset of customer data with 1,000 records. For each customer, it randomly assigns an age between 18 and 80. Based on age, an income is calculated, where older individuals generally have higher incomes. The credit score is then determined, influenced by age and income, ensuring it falls between 300 and 850. A loan amount is also generated, dependent on the individual's income and credit score. 

The used approach ensures that the generated data adheres to known relationships and constraints, making it possible to incorporate domain-specific knowledge directly into the data generation process. However, it can become complex when dealing with systems with many interrelated rules, and defining and maintaining such rules can be time-consuming for large or intricate datasets.
