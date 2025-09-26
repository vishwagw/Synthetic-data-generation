# Method 3: simulation-base generator:
Simulation-based data generation models real-world processes to create synthetic datasets. It involves simulating events or behaviors based on predefined rules and variables, allowing us to study how different factors interact in dynamic systems. 

This method is often used to test scenarios and analyze potential outcomes, providing valuable insights into complex systems like customer service processes, supply chains, and healthcare operations. 

The code simulates a bank using the SimPy library. Customers arrive at random intervals, wait for service from one of the three available tellers, and then leave after being served. 

The Bank class defines the service time (averaging 10 minutes), while the customer() function tracks each customer’s arrival, waiting time, and service duration. Customers are processed in the run_simulation() function, which generates new arrivals on average every 5 minutes.