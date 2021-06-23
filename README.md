# Digital Twin System Proposal for Renewable Energy

![img_keyvisual_post_kw46_DIGITAL_TWIN](https://user-images.githubusercontent.com/48045619/123182457-207b4880-d498-11eb-925b-3cbe43dc8431.jpg)


In renewable energy systems, the project is a system that provides an increase in the management of the energy produced and the efficiency obtained from the system, and makes use of the Intelligent Decision Support System and Digital Twin technologies in this process. Our project has been designed in such a way that organizations providing renewable energy production can benefit. The main objectives of our project can be summarized as follows:
The system designed within the scope of the project; It aims to increase the efficiency of the energy produced by the organizations that produce energy using renewable energy sources, and to prevent the sources from creating problems during the production phase.

# Data Visulation

With R Studio, made some charts to examine and visualize data set.

![Rplot](https://user-images.githubusercontent.com/48045619/123182371-f3c73100-d497-11eb-952d-c04e8344b538.png)

![Rplot01](https://user-images.githubusercontent.com/48045619/123182389-fcb80280-d497-11eb-9fb2-5e72abbcb049.png)



# System Structure

● Renewable Energy Sources: Devices installed to produce Renewable Energy.

● Digital Twin: A system that regularly examines the physical condition and functioning of energy-generating devices.

● Intelligent Decision Support System: A system that regularly examines production quantities and physical condition data and detects potential problems.

![Final Schema-ing](https://user-images.githubusercontent.com/48045619/123181577-3982fa00-d496-11eb-8e53-0f32795964e0.png)



# Steps of System Funcitons

1. Digital sensor integration into Renewable Energy sources.

2. Transferring physical states to the Decision Support System on a regular basis.

3. Examining the amount of produced energy, weather conditions, number of panels (capacity) conditions.

4. Regularly transferring the analyzed data to the Decision Support System.

5. Predicting and reporting possible problem situations by the system.

6. Intervention in case of verification of data examined by the control room.


# Smart Decision Support System

There are 2 different structures in SDDS;

1. Machine Learning Methods
  1.1 Random Forest Algorithm
  1.2 KNN Algorithm
  1.3 XGB Algorithm

2. Manuel Control System
  There are some conditions on spesific events. Manuelly written and it is written to check if ML Algorithms makes a mistake.
  
  
 
  
