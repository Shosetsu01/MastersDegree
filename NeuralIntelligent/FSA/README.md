# Fish-School-Search 🐟
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)<br>
### The fish swarm algorithm (FSA) is a population-based/swarm intelligent evolutionary computation technique that was inspired by the natural schooling behavior of fish. FSA presents a strong ability to avoid local minimums in order to achieve global optimization.

<div align="center" id="top"> 
  <img src="./images/fish-19.gif" alt="Gh_fish" />
</div>

## About algorithm
A school of fish is an aggregation of fish that move with approximately the same speed and orientation, maintaining a constant distance between them.In the FSS algorithm (J.B.M. Philo and F. Neto, 2008), fish swim in an aquarium, which is the domain of acceptable solutions in the search for food (the solution to the optimization problem), with the position of fish in it reflecting the current solution vector. Each n-dimensional fish location represents a possible solution to the optimization problem.
### The main stages
1. Population initialization<br>
* Random selection of the agent's position within the aquarium. <br>
* The algorithm limits the maximum allowed weight of agents. <br>
* All agents are assigned a value equal to half of the maximum weight.<br>
2. Migration of agents to the food source<br>
The number of iterations (iter) is used as the stopping criterion.
At each iteration of the cycle all agents overcome several stages:
* Individual stage of floating agents <br> 
* Instinctive-collective stage <br>
* Collective-volitional stage of swimming <br> 
### Test function
In addition, there is a test function EggHolder function (function(x)) and a function for sorting individuals by values of the function sort(x, f).
<img src="https://github.com/Kirnata/Fish-School-Search/raw/main/images/formula.png" width="700">

<img src="https://github.com/Kirnata/Fish-School-Search/raw/main/images/Eggholder.png" width="700">

## How to use?

**The input of FSS and FSS_mod is 7 parameters:**<br> 
**X_min** - vector of lower bounds of the search;<br> 
**X_max** - vector of upper bounds of search;<br> 
**N_agent** - number of fish in a school;<br> 
**iter** - number of iterations;<br> 
**Wmax** - maximum weight of fish;<br> 
**StepMax** - maximum (initial) step size;<br> 
**StepMin** - minimum (final) step size.<br> 

You can change the parameters of the function call at the end of the code file, e.g.:<br> 
`x = FSS_MOD([-512, -512, -512, -512], [512, 512, 512, 512], 1000, 1000, 50, 50, 10)`<br> 
Then:<br> 
`run ffs.py` 
or
`run ffs_mod.py`<br> 
To obtain a more accurate maximum value, we should enter parameters where the population size and the number of iterations should be relatively large, the initial and final search radii should not differ by a very small number, and the maximum weight of the agent should be about 50. It is also worth noting that the parameters N_agent and iter have the greatest influence on the algorithm, and special attention should be paid to their selection.
## Modifications
The main drawback of the algorithm is the approximation of the data. On the plus side, it is fast. Sometimes this factor is the main factor in the work, and even the minimum error is not so important.
It is not always possible to immediately find the desired result, which depends directly on the values entered by the user. <br>
To modify the algorithm, a modification of the usual operators was proposed, aimed at improving the reliability of the weight parameters. In the basic version of the algorithm, there are cases where the weight of an individual does not affect how much it affects during the search. To solve this problem, it was decided to include normalization in the feeding operator to ensure that the heaviest individual is the one that presented the best result during the search.
In the implementation, the modification differs from the basic algorithm in the instinctive swimming, post-weigh counting, and collective-instinctive swimming stages. Another list containing test function values for all agents, updated at each iteration, is added to the algorithm, which is necessary for further normalization of the feeding operator. <br>
In order to analyze the effect of changes on the efficiency of the algorithm, several calculations were performed with the same initial parameters with the basic and modified FSS and FSS_MOD algorithms, respectively.<br>
(Iter = 1000, N_agent = 1000, Wmax = 50, StepMin = 50, StepMax = 100)<br>

<img src="https://github.com/Kirnata/Fish-School-Search/raw/main/images/table.png" width="300">

Based on the results, we can conclude that the changes made have improved the accuracy of the algorithm, but to an insignificant extent.<br>
