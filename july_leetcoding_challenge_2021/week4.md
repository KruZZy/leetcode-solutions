Originally posted on dev.to - https://dev.to/kruzzy/leetcode-explained-july-challenge-2021-week-4-partition-array-into-disjoint-sets-medium-54ic/edit

## Problem Description

In the July LeetCoding Challenge 2021, week 4, we're tasked with the following ([original problem here](https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3823/)):

Given an array **nums**, partition it into two (contiguous) subarrays **left** and **right** so that:

- every element in **left** is less than or equal to every element in **right**.
- **left** and **right** are non-empty.
- **left** has the smallest possible size.

We have to return the length of **left** after such a partitioning and the problem has the following notes: 

- 2 <= nums.length <= 30000
- 0 <= nums[i] <= 10^6
- it is guaranteed there is at least one way to partition nums as described.

Example 1:
- nums = [5,0,3,8,6] 
- output: 3 
- explanation: left = [5, 0, 3] / right = [8, 6]

Example 2:
- nums = [1,1,1,0,6,12]
- output: 4
- explanation: left = [1,1,1,0] /  right = [6,12]

## Finding a solution

As we are being tasked with finding subarrays, which are **contiguous**, it is only natural to search for an index in the array to make a "cut" - that is, the index after which array **left** ends.

We will make use of maximum values in subarrays of the array to devise a solution. 

It is a requirement that every element of **left** has to be smaller than or equal to every element of **right**, and **left** has to be as small as possible. Let's think about this a little. 

For the first requirement, it would be sufficient to just find the maximum in the whole array and make a "cut" behind it. That is, if the maximum was at index **i** (suppose we start from 0), then **left** will contain indexes from 0 through **i-1** of nums, and **right** will contain indexes from **i** through **n-1**, if **n** is the size of array **nums**.
That would, however, make **left as big as possible**, not as small as possible as it is required.

To keep the size of **left** as small as possible, we can think of a scenario where there is an index **i**, which is not necessarily the maximum of the array, but is the maximum of nums[0..i] and there is no other number in nums[i+1..n] that is bigger than what is left of index **i**.

The second example provided by the author presents this thing: while 6 is not the maximum value in the array as a whole, it is the maximum of the prefix from 0 through its index (which is 4 here), and has no number smaller than the maximum of nums[0..3] to its right.

The problem then resumes to finding such the number. We can do this in O(n) time complexity and O(1) space complexity.

We will traverse the array and keep two variables, let them be called **left_max**, which represents the maximum value that will be put in the **left** array, and **last_max**, which represents the last maximum values we encountered up until that point.

Initially, we will set both those values to the first element of the array. We will also keep a variable named **cut** representing the index after we split the array in **left** and **right**. So, the array will be cut after the first element.

While looping through the array, there are two types of numbers we can find at one index **i**:
- a number smaller than **left_max**: in such a case, we need to move the cut, because otherwise we will not obtain the arrays needed; we should keep in mind that before making a cut, nums[i] is to be placed in the array **right**; so, if we weren't to make a cut, we will not respect the requirements of the problem.
- a number bigger than or equal to **left_max**: in this case, we need to update the value of **last_max** if needed, so that when we make a cut we will know the maximum in the **left** array in O(1) time.

Let's see a short Python solution using this approach:

{% gist https://gist.github.com/KruZZy/c7b93b051095e65a8253cde5a2b4b82f %}

That would be all for this solution. I'll be back with other LeetCode solutions for my new **LeetCode Explained** series. In the meantime, feel free to comment your solutions in other programming languages here. Or, if you don't feel like it, you may like to read through my other series - [The Magic of Computing](https://dev.to/kruzzy/series/3724), discussing other algorithmic topics!




