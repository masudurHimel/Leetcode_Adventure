<h2><a href="https://leetcode.com/problems/print-in-order/">1114. Print in Order</a></h2><h3>Easy</h3><hr><div><p>Suppose we have a class:</p>

<pre style="">public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
</pre>

<p>The same instance of <code style="">Foo</code> will be passed to three different threads. Thread A will call <code style="">first()</code>, thread B will call <code style="">second()</code>, and thread C will call <code style="">third()</code>. Design a mechanism and modify the program to ensure that <code style="">second()</code> is executed after <code style="">first()</code>, and <code style="">third()</code> is executed after <code style="">second()</code>.</p>

<p><strong>Note:</strong></p>

<p>We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre style=""><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> "firstsecondthird"
<strong>Explanation:</strong> There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
</pre>

<p><strong>Example 2:</strong></p>

<pre style=""><strong>Input:</strong> nums = [1,3,2]
<strong>Output:</strong> "firstsecondthird"
<strong>Explanation:</strong> The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code style="">nums</code> is a permutation of <code style="">[1, 2, 3]</code>.</li>
</ul>
</div>