https://github.com/jayshah19949596/CodingInterviews/tree/master/TwoSigma%20Software%20Engineer%20Investments%202019
http://www.goodtecher.com/tag/two-sigma-interview-question/
https://www.hackerrank.com/company-page-two-sigma-a2bd324b0babbd81703c990f4cb6e42b/
https://blog.csdn.net/u012290414/article/details/47051861
https://www.ctolib.com/jayshah19949596-CodingInterviews.html
https://github.com/jayshah19949596/CodingInterviews
https://medium.com/@jayshah_84248/how-to-do-well-in-a-coding-interview-2bcd67e93cb5

friend circle
https://blog.csdn.net/u012290414/article/details/47051861

https://www.open-open.com/github/view/github2015-03-20.html
https://www.cnblogs.com/EdwardLiu/category/615066.html


每日一贴: http://www.mitbbs.com/article_t/JobHunting/33072385.html

http://www.mitbbs.com/article_t/JobHunting/33072385.html
每日一贴: http://www.mitbbs.com/article_t/JobHunting/33072385.html
面了google/facebook/linkedin/two sigma/aqr/uber, 被uber/aqr据了。基本所有面
hedge fund 1:
1.    Write a function that takes as input integers P and Q and returns P to
the power of Q.  Note any assumptions you make and the complexity of the
algorithm.  We expect you to do better than O(Q).
2.  Write a function that takes as input an array of 1 million integers,
such that 1 ≤ x ≤ 10 for every element x in the array, and returns the
sorted array.  The sort does not need to occur in-place.  Obviously you can
just call a standard sorting function like quicksort, but can you do better?
3. You are given an alphanumeric string.  Write an algorithm that will
segment the string into substrings of consecutive integers or numbers and
then sort the substrings.  For example, the string "AZQF013452BAB" will
result in "AFQZ012345ABB".
4.    Write a function to determine the largest palindromic subsequence of a
string.  A palindromic string is a string which is the same when read in
either the forward or reverse direction.  For example, "ABBA" is a
palindromic string and the largest palindromic substring of "TABBA" is "
ABBA".
I did with a double loop solution.

tech company 1:
phone screen:
word ladder (check the leetcode for this question)
onsite:
1. graph deepcopy
2. use normal lock to implement readwrite lock
3. design question, how to scale web application
4. given a list of iterators which iterates over sorted lists, write a
MergeIterator class which iterates over the merged list, e.g.

class MergeIterator<T extends comparable<T>>
{
    MergeIterator(List<Iterator<T>> iterators)
    {
    }

    boolean hasNext()

    T next();
}

hedge fund 2:
1. friend circles - give a matrix, Y in cell means i and j is friend, N
otherwise, find how many friend circles in the matrix, e.g. 1 is friend of 2
, and 2 is friend of 3, then 1,2,3 is in same friend circle.
2. StringChain, give a dictionary, the string chain is by remove a char in
the string, and if the new string is in the dictionary, then continue, e.g.
dict = { a, b, ab, abc, add} then the longest chain is (a, ab, abc) or (b,
ab, abc). The char can be removed from any place in the string.

online coding:
huffman decoding. give a huffman encoding dictionary, decode a string back.

Onsite:
1. multiply 2 numbers, the digits of the numbers are given as int array, e.g
. int[] product(int[] num1, int[] num2);
2. given a list of intervals, each interval is defined as 2 integer (start/
end), find min set of points, for those points, each interval at least cover
1 point. e.g. given intervals as [1, 4], [2, 3], [5, 6], we just need 2
points, (2, 5), and each interval will either cover piont 2, or point 5.
need O(nlogn) solution.
3. given binary search tree, each tree node contains piont of (left, right,
parent, leftChildTreeSize), write a function to find the number of nodes
which has value less than the given node, e.g.
int findNumberofLess(Node current, Node root);
4. process 2 stream of data and output result, basic merge sort
implementation.

tech company 2:
1. have N offices globally. each office have a local calender with holidays.
you are allowed to move every weekend to different office, how to get max
numbers of holidays. follow up, if for each office, there are only certain
set of offices are reacheable, e.g. if you are in NYC this weekend, you can
move to SF, or London. If you are in SF, you can move to NYC and Beijing,
etc. how to max the holidays.
2. Binary tree find the longest consecutive path.
3. how to check 2 rectangles overlap. Give a very large set of segments (
each segment is defined by start point and end point), given a function
which given 2 segments, returns the intesection of the 2 segment if they
intersect, or null if not. How to find all the intersections, cannot do the
double loop in memory since the dataset is too big to fit in memory.
4. give a string array, find the 2 string which don't share any char, and
have the max product of the lengths. e.g. given string abc, aagh, def, the
max product is len(abc) * len(def) = 3 * 3 = 9
5. design question, how to generate unique sequence number using distributed
system. e.g. you have a set of machines which is running this sequence
number generator, client can connect to any machine, and get the next
sequence number which is guranteed to increment for same client.

tech company 3:
online coding:
1. find kth minimal number in tournament tree. sample of tournament tree (2
beat 4, 3 beat 5, 2 beat 3 and become champion)
2
2  3
4 2, 3, 5
2. word distance, e.g. given an array of words, and give 2 words, find the
min distance of index those 2 words

Onsite:
1. deepIterator, e.g. given list {1, 2, {{3, 5}, 4}, 6}, write an iterator
class which will iterate through the deep list.
2. check whether 2 tree is identical, can you do it iteratively?
3. roman string to int, and int to roman string
4. adding a list of intervals, each interval is defined by start point and
end point, find the total coverage of the intervals, e.g. intervals: { 1, 4}
, {2, 5}, {7, 10}, total coverage is 1 to 5 and 7 to 10, which is 7.
5. design question, design a system which can rank the url sharings, e.g.
users will share urls, we want to rank the most shared urls for the last 10
minutes, for last hour, for last day, etc. there are total 100 millions url
sharing happen every day.

现在two sigma/google 二选一，工资基本一样，组都不错，不知道有没有在那里上班
的可以给点建议。