Intro to Hadoop and MapReduce project
In this project you will work with some discussion forum (also sometimes called discussion board) data. It is a type of user generated content that you can find all around the web. Most popular websites have some kind of a forum, and the things you will do in this project can transfer to other similar projects. This page will be followed by various questions about the data set. Feel free to share your responses to these questions on the discussion forums to get feedback from your peers.

The Data Set
This particular dataset was taken from the Udacity forums the first months after the launch of this course. Udacity forums were run on a free, opensource software called OSQA, which was designed to be similar to the popular StackOverflow forums. The basic structure is - the forum has nodes. All nodes have a body and author_id. Top level nodes are called questions, and will also have a title and tags. Questions can have answers. Both questions and answers can have comments.

You will have to run the code mostly on your VMs, or on your real Hadoop cluster, if you have set up one. You can download the additional dataset here. To unarchive it, download it to your VM, put in the data directory and run:

tar zxvf forum_data.tar.gz
There are 2 files in the dataset. The first is "forum_nodes.tsv", and that contains all forum questions and answers in one table. It was exported from the RDBMS by using tab as a separator, and enclosing all fields in doublequotes. If you finished Lesson 4, you already know how to deal with such files. You can find the field names in the first line of the file "forum_node.tsv". The ones that are the most relevant to the task are:

"id": id of the node
"title": title of the node. in case "node_type" is "answer" or "comment", this field will be empty
"tagnames": space separated list of tags
"author_id": id of the author
"body": content of the post
"node_type": type of the node, either "question", "answer" or "comment"
"parent_id": node under which the post is located, will be empty for "questions"
"abs_parent_id": top node where the post is located
"added_at": date added
The second table is "forum_users.tsv". It contains fields for "user_ptr_id" - the id of the user. "reputation" - the reputation, or karma of the user, earned when other users upvote their posts, and the number of "gold", "silver" and "bronze" badges earned. The actual database has more fields in this table, like user name nickname, bio (if set) etc, but we have removed this information here.



Students and Posting Time on Forums
We have a lot of passionate students that bring a lot of value to forums. Forums also sometimes need a watchful eye on them, to make sure that posts are tagged in a way that helps to find them, that the tone on forums stays positive, and in general - they need people who can perform some management tasks - forum moderators. These are usually chosen from students who already have shown that they are active and helpful forum participants.

Our students come from all around the world, so we need to know both at what times of day the activity is the highest, and to know which of the students are active at that time.

In this exercise your task is to find for each student what is the hour during which the student has posted the most posts. Output from reducers should be:

author_id    hour
For example:

13431511\t13
54525254141\t21
If there is a tie: there are multiple hours during which a student has posted a maximum number of posts, please print the student-hour pairs on separate lines. The order in which these lines appear in your output does not matter.

You can ignore the time-zone offset for all times - for example in the following line: "2012-02-25 08:11:01.623548+00" - you can ignore the +00 offset.

In order to find the hour posted, please use the date_added field and NOT the last_activity_at field.

To make sure your code is running properly, we have put together a smaller data set and set of expected outputs for you to use to check your work. Please click here to access the instructions to use it.




Post and Answer Length
We are interested to see if there is a correlation between the length of a post and the length of answers.

Write a mapreduce program that would process the forum_node data and output the length of the post and the average answer (just answer, not comment) length for each post. You will have to decide how to write both the mapper and the reducer to get the required result.

To make sure your code is running properly, we have put together a smaller data set and set of expected outputs for you to use to check your work. Please click here to access the instructions to use it.
Hints for writing reducer code

Code should not use a data structure (e.g. a dictionary) in the reducer that stores a large number of keys. Remember that Hadoop already sorts the mapper output based on key, such that key-value pairs with the same key will appear consecutively as input to the reducer. Make sure you take advantage of this ordering when you write your reducer code.

This is part of a more general principle connected with the Volume characteristic of Big Data. Mappers and reducers read through very large amounts of data and we should be mindful, as we write mapper and reducer code, of how much data we store in main memory.



Top Tags
We are interested seeing what are the top tags used in posts.

Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in.

For an extra challenge you can think about how to get a top 10 list of tags, where they are ordered by some weighted score of your choice. If you decide to do this, then please submit your solution to the regular problem and then also submit this extra challenge problem in separate files as described on the instruction page.

To make sure your code is running properly, we have put together a smaller data set and set of expected outputs for you to use to check your work. Please click here to access the instructions to use it.

Please note that you should only look at tags appearing in questions themselves (i.e. nodes with node_type "question"), not on answers or comments.
Hints for writing reducer code

Code should not use a data structure (e.g. a dictionary) in the reducer that stores a large number of keys. Remember that Hadoop already sorts the mapper output based on key, such that key-value pairs with the same key will appear consecutively as input to the reducer. Make sure you take advantage of this ordering when you write your reducer code.

Please feel free to use dictionaries to process data for the current key, but you shouldn't keep old data around from previous keys (eg. in a dictionary) if you don't need to.

This is part of a more general principle connected with the Volume characteristic of Big Data. Mappers and reducers read through very large amounts of data and we should be mindful, as we write mapper and reducer code, of how much data we store in main memory.



Study Groups
We might want to help students form study groups. But first we want to see if there are already students on forums that communicate a lot between themselves.

As the first step for this analysis we have been tasked with writing a mapreduce program that for each forum thread (that is a question node with all it's answers and comments) would give us a list of students that have posted there - either asked the question, answered a question or added a comment. If a student posted to that thread several times, they should be added to that list several times as well, to indicate intensity of communication.

To make sure your code is running properly, we have put together a smaller data set and set of expected outputs for you to use to check your work. Please click here to access the instructions to use it.
Hints for writing reducer code

Code should not use a data structure (e.g. a dictionary) in the reducer that stores a large number of keys. Remember that Hadoop already sorts the mapper output based on key, such that key-value pairs with the same key will appear consecutively as input to the reducer. Make sure you take advantage of this ordering when you write your reducer code.

This is part of a more general principle connected with the Volume characteristic of Big Data. Mappers and reducers read through very large amounts of data and we should be mindful, as we write mapper and reducer code, of how much data we store in main memory.
