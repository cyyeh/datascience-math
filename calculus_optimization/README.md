# Calculus and Optimization for Machine Learning

## Overview

Course starts with basic introduction to concepts concerning functional mappings. Later students are assumed to study limits (in case of sequences, single- and multivariate functions), differentiability (once again starting from single variable up to multiple cases), integration, thus sequentially building up a base for the basic optimisation. To provide an understanding of the practical skills set being taught, the course introduces the final programming project considering the usage of optimisation routine in machine learning.

## Key Concepts by Week

Week 1, Introduction: Numerical Sets, Functions, Limits
> Here we introduce basic concept the calculus course could not be imagine without: function. In order to properly do it, one should say that the function is a mapping from one set to another. Thus, we start with the ideas of numerical sets and mapping, then proceeding with functions itself. Since we are particularly interested in functions' graph, we spend a lot of time discussing simplest ways to produce a complex function graph from elementary case. In the second part of the week we start our calculus journey with a discrete limit, the limit of sequences, and master skills needed to calculate them.

- Understand basic ideas of sets, numerical sets and mappings
- Understand and interpret the definition of sequence's limit
- Apply basic graph transformations to existing plot to produce a more sophisticated one
- Distinguish between various functions related concepts: domain, codomain, support, etc.
- Calculate various limits of sequences by several different techniques

---

Week 2, Limits and Multivariate Functions
> Now it is time to move from discrete limits to continuous ones: in other words, in the current module we are going to discuss limits of functions. We start with the basic question: does this case sufficiently differ from the sequences? Turns out, yes, it does thanks to significant structural differences between natural and real numbers. One of those differences - the continuousness - allows us to define and calculate limits at finite moments. We spend some time specifically on the famous important limits, then we proceed with the idea of asymptotic comparison of functions, Big- and little-o notations. To top our module with, we introduce functions of several variables and spend some time getting used to conveniently plot and interpret them, finishing up with discussion of its limits.

- Illustrate the multivariate functions with surface or level plots
- Understand the concept and distinguish between the indeterminate forms
- Calculate limits of functions
- Understand the structural difference in taking limits of sequences and functions
- Understand and interpret the formal and informal function's limit definition
- Understand the srtuctural difference of limits of single- and multivariate functions

--- 

Week 3, Derivatives and Linear Approximations: Singlevariate Functions
> Since we now know limits, let us use them in order to define some instantaneous characteristics of functions starting with its slope. Thus we define function's derivative and discuss all the machinery to calculate it. Since it is a purely technical issue, you are expected to be able to do it: in order to make sure that you can find a derivative we provide a drill. This skills could be used for finding approximate values via linear approximation or during the search for extremal values. To provide an understanding of the sufficient condition of the extremum, we introduce the concept of convexity.

- Understand the motivation of the definition of derivatives
- Provide a full extrema analysis for the function by its derivative
- Use linear approximations to produce close estimation of the true value of the function
- Understand the idea of differential and derivatives of higher order
- Calculate the derivative of any single-variate function
- Understand the concept of convexity and its relation to derivatives
- Distinguish between differetiable and non-differentiable cases

--- 

Week 4, Derivatives and Linear Approximations: Multivariate Functions
> Whilst we have discussed all linear related concepts for single variate functions, it is essential to try and generalise it for the multivariate case. Since the derivative concept is hard to stretch directly, we start with the idea of linear approximation and tangent plane; thus we introduce partial derivatives and the differentiability. We separately spend sometime discussing neural network inspired composite multivariate functions and all-mighty chain rule. Our generalisation attempt finalised with the idea of convexity in terms of the second partial derivatives.

- Understand and be able to establish the convexity of the multivariate function
- Find approximate values by tangent planes and linear approximations
- Explain the generalization idea of differentiability
- Calculate partial derivatives and gradient for any function
- Calculate the derivative of composite function by chain rule

--- 

Week 5, Integrals: Anti-derivative, Area under Curve
> As we introduced the operation of differentiation, it is essential to think about the inverse procedure - the integration. We start the module with basic definition of the integration and, as usual, all techniques required to calculate wide range of the indefinite integrals, stressing out that the result is not guaranteed now. Then we proceed with the idea and formal definition of area under curve and its relation to the indefinite case - the fundamental theorem of calculus. We finish our week with the discussion of the areas of infinite figures (improper integrals) and numerical methods to assess the value of the definite integral.

- Distinguish between convergent and non-convergent improper integrals
- Understand the concept of the indefinite integral
Calculate areas under curve
- Understand the idea of various numerical methods of integration
- Understand the concept of definite integral and its relation to the indefinite case
- Calculate a vast range of indefeinite integrals

---

Week 6, Optimization: Directional derivative, Extrema and Gradient Descent
> As we built up impressive base by introducing various estimations of change and overall function's behaviour, it is essential to speak about general idea of the optimisation procedure. Since we already tackled it in a single variate case, we try to generalise our principles of necessary and sufficient conditions to the case of multivariate functions. Whilst it provides theoretical understanding, one should seek for faster iterative way to find an extremal point. In order to do it, we start our week with the concept of the directional derivative in order to provide and understanding of the desired direction of iterative search. Thus we produce the idea and motivation of the gradient descent, the last and final concept in our course you are asked to master.

- Distinguish between necessary and sufficient conditions of the multivariate extrema
- Understand the concept of the directional derivative and its relation to the gradient
- Explain the way to establish the direction of maximal growth
- Complete full extrema analysis of the multivariate function
- Calculate directional derivatives by definition and by scalar product rule
- Understand the motivation and mechanics of the gradient descent