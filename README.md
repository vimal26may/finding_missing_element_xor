# finding_missing_element_xor
Finding a missing element in two lists using xor

This code is a to search for a missing element from two given sets using xor

Assmuptions:
1) Set with a missing element would be a subset of main set
2) Only one element is missing from the set

Primary Logic behind using this code is to minimise the space complexity of the code keeping time complexity in control

Current time complexity of the code is O(N) where N is the number of elements in the main set

Another approach to solve the problem can be finding the difference of sum of all elements in both sets.
missing element = sum(main set numbers) - sum(missing element set numbers)
But if the numbers are too large in the sets, so will there sum be. In order to resolve this, the XOR operation approach comes in handy. XOR being a bitwise operation, will have the resulting number (residues of operations performed) of approx. same order.

Approach:
	Main Set = {A,B,C,D} where A,B,C,D are integers
	Missing Element Set = {A,B,C} (subset of Main Set)
	(A xor B xor C xor D) xor (A xor B xor C)
	= (A xor A) xor (B xor B) xor (C xor C) xor D
	= 0 xor 0 xor 0 xor D		(any number xor itself is 0)
	= D							(0 xor any number is number itself)

To understand this, following trial calculation was done.
1) To check in case the order of applying XOR on a given set of numbers will have any difference or not:

1 xor 3 xor 7 -> (001 xor 011)xor 111 -> 010 xor 111 -> 101												

7 xor 3 xor 1 -> (111 xor 011) xor 001 -> 100 xor 001 -> 101

1 xor 7 xor 3 -> (001 xor 111) xor 011 -> 110 xor 011 -> 101