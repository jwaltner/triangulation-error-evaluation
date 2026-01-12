## Introduction

This triangulation project provides code which shows examples of how triangulation could be performed.  Of note, these are not necessarilly the best algorithms, but they do present several methods of performing triangulation.

## Algorithms

### Geometric / Numerical Method

The geometric / numerical solution relies on geometry and numerical methods follows.  Note that this uses geometry and logic to determine the triangulation point and in practice requires adherence to reasonable tolerances given numerical uncertainties.  This algorithm is not a closed form solution to determine the triangulation point location.

* Given three points 1, 2, and 3, with known locations, observe the angular separation angle12, angle23, and angle31 between them.  These angles and point locations are the required inputs to the algorithm.
* Find all circles which satisfy the constraints of the angular separations angle12, angle23, angle31.  Any valid triangulation point must lie on these circles.
  * This is done for each point pair by using the inscribed angle theorem by defining the line segment between the two points as a chord on a circle and noting that the inscribed angle of any point on that circle to the two points at the end of the chord will be constant.  As such, any valid triangulation point with a prescribed inscribed angle between two points will be constrained to the set of points which make up the circles which have the chord between the two points defined along with the provided inscribed angle. 
* Find all intersections of these circles.  These intersections are the candidate triangulation points as any valid triangulation point must lie on an intersection point between two of the circles as the circles are constrained to the valid angular separation between observed points.
* Filter out any intersections which lie on one of the points with known locations.  Note that if an observer is very close to a landmark, then that landmark will likely cause larger numerical error if it is used in this algorithm. 
* Remove duplicates from the candidate point list.
* Calculate the 6 different orders of inscribed angles between landmarks and the candidate point to determine if any ordering of points results in angular separations to that which was provided.
* Return the list of points which meet the angular separation provided as an input.  Note that there may be multiple points returned; however, if the target's orientaiton is known (as is the case for April Tags since April Tags can only be observed from one side), the knowledge of which solution to pick for the final answer will be able to be determined. **TODO: CONFIRM THIS**

**TODO: add pictures for each step and expand description / logic.**

### 