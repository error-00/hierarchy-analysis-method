# hierarchy-analysis-method
The software product implements the method of analysis of hierarchies (HAI), which is a tool for decision-making in conditions of multicriteria and ambiguity. The main functions of the software product include:
1. Entering the number of criteria and alternatives on the main page (Figure 2.1): The user can enter the number of criteria and alternatives that will be used to make a decision. This can be entered on the main page of the application.

![image](https://user-images.githubusercontent.com/90632114/234251049-c1570430-332a-4709-a7f8-1fad03681183.png)
Entering the number of criteria and alternatives


2. Entering the names of criteria and alternatives on the "Names" page (Figure 2.2): The user can enter the names of criteria and alternatives on a separate "Names" page, where they can be specified for further use in calculations.

![image](https://user-images.githubusercontent.com/90632114/234251181-35c378b7-2bfa-428f-8ff1-3d08f9df5998.png)
Entering the names of criteria and alternatives


3. Entering the criteria weight matrix on the Criteria Matrix page (Figure 2.3): The user can enter the criteria weight matrix (only the upper triangular part, the rest will be filled in automatically), which reflects the importance of one criterion relative to others. This matrix is used to calculate the weights of the criteria in the subsequent steps of the MAI.

![image](https://user-images.githubusercontent.com/90632114/234251298-3288073a-ef21-4fdd-b619-dd9679b52dc4.png)
Completing the matrix of pairwise comparisons for criteria


4. Entering alternative weighting matrices (Figure 2.4): The user enters relative evaluations of alternatives for each criterion on the required page. For each alternative, the user indicates which of the criteria is preferable to this alternative. The software automatically calculates the values in the matrix of pairwise comparisons based on the entered scores, using the established rules of analysis of hierarchies.

![image](https://user-images.githubusercontent.com/90632114/234251419-fdc5c4e1-008e-4ddc-9812-ecd23c4f939b.png)
Completing pairwise comparison matrices for alternatives


5. Calculation of the components of the eigenvector, the normalized estimates of the priority vector, the sum by columns, the product of the applications by columns and the normalized estimate of the priority vector, as well as the ranking on the "Result" page: The software automatically calculates the components of the eigenvector, the normalized estimates of the priority vector, the sum of columns and a normalized priority vector score for each alternative and outputs all this information on the result page. And at the end, the main ranking result will be displayed.


6. Visualization of results on the "Result" page: The software product can visualize the results of the analysis of hierarchies in a convenient graphical form on the "Result" page. It is a representation of the ranking of the alternatives according to their scores, criteria weights and other visual information that helps the user to understand the obtained results.

![image](https://user-images.githubusercontent.com/90632114/234251584-fc616f7c-bc43-4569-9a91-3a1773ed5829.png)
![image](https://user-images.githubusercontent.com/90632114/234251604-c0075f73-357e-4d90-b840-8ec57ea2197d.png)
![image](https://user-images.githubusercontent.com/90632114/234251628-6f3fe210-daef-4d26-84fb-16608e9d322c.png)
![image](https://user-images.githubusercontent.com/90632114/234251646-8d6aee58-f710-463e-8ed3-11d8a6d7bdb9.png)
Result


7. Interaction with the user in the Ukrainian language: The software product has an interface and functionality that fully supports the Ukrainian language, which allows users to comfortably work with the product in their native language.

Error handling is also provided in the software product. The user will not be able to go to another page without filling in all the fields on the current page. The fields must be filled in according to the rules. For example, in a matrix of paired comparisons, if the user enters 0.2, he will not be able to go to the next page, because the software will see the error and indicate it to the user.

If the consistency ratio will be more than 15%, then on the result page the software product will indicate in which table it is.

A web application that uses the mymodules.mai module I created to use calculations related to matrices and eigenvalues. The program has multiple routes for different pages such as Home, Names, Alternatives Matrix, etc. Routes receive data from web forms submitted by users, perform calculations on the data, and store the results in a Flask session for use by subsequent routes.

The program uses the Flask templating engine to render HTML pages and display the results of calculations to users. It also uses a request module to access data submitted by users through web forms, and a session module to store and retrieve data through various routes.

Computations performed in routes include creating matrices from user input, computing eigenvalues and eigenvectors, normalizing vectors, computing sums and products of matrix columns, and performing consistency checks on computed results.
