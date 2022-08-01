---
layout: page
title: Admin
nav_exclude: true
description: A feed containing all admin-related pages.
---

# Quick access links

Some of this information has been transferred from <https://ucsb-csw8.github.io/w22-staff/howto/>.

## Gauchospace

### Grades
* ["How to upload grades to Gauchospace"](https://help.lsit.ucsb.edu/hc/en-us/articles/202561544-How-do-I-upload-a-spreadsheet-of-grades-into-the-GauchoSpace-gradebook-)
* [Manually Override Points for a Specific Question in Quiz](https://help.lsit.ucsb.edu/hc/en-us/articles/360042449951-Manually-Override-Points-for-a-Specific-Question-in-Quiz) (as much as possible refrain from using this: instead, add the other correct options to the list of correct answers)

### Quizzes
Here are the official Gauchospace reference pages for quizzes:
* [Quiz Reference Guide for Gauchospace](https://help.lsit.ucsb.edu/hc/en-us/articles/204491504-Quiz-Reference-Guide-for-Gauchospace)
* [Revealing Quiz Scores and Feedback Only After a Quiz Closes](https://help.lsit.ucsb.edu/hc/en-us/articles/360052427312-Revealing-Quiz-Scores-and-Feedback-Only-After-a-Quiz-Closes) (uncheck all options for "After the quiz is closed" until all responses have been checked and options have been adjusted, and then set the review option for "After the quiz is closed" retroactively.)
* [Understanding Quiz Statistics](https://help.lsit.ucsb.edu/hc/en-us/articles/360056425031-Understanding-Quiz-Statistics)
* [Quiz Tips: How to create multiple choice quiz questions in Gauchospace using Word](https://help.lsit.ucsb.edu/hc/en-us/articles/214732228-Quiz-Tips-How-to-create-multiple-choice-quiz-questions-in-Gauchospace-using-Word)
* see above how to [Manually Override Points for a Specific Question in Quiz](#) (as much as possible refrain from using this: instead, add the other correct options to the list of correct answers)

## Gradescope

<https://help.gradescope.com/>

## zyBooks

See the relevant guidelines under [the Guidelines section]({{ site.url }}{{ site.baseurl }}/guidelines#zybook)
* [How to create a new zyLab](https://zybooks.zendesk.com/hc/en-us/articles/360012355613-How-to-create-a-new-zyLab)
* [How to copy a new zyLab](https://zybooks.zendesk.com/hc/en-us/articles/360015181913-How-to-copy-a-zyLab)
* [Configure zyBook](https://zybooks.zendesk.com/hc/en-us/articles/360007903633-How-to-configure-your-zyBook)
* [Create a test using zyBooks test banks](https://zybooks.zendesk.com/hc/en-us/articles/360018781373)

---

# Course-specific Components, Setup and Considerations

## Zoom
Please change your name on Zoom to include the word `_MENTOR` _before_ your name and add your pronouns: 
<https://support.zoom.us/hc/en-us/articles/4402698027533>
 
Remember that anything that you say online can be recorded, so be mindful of what you share.
 
When working with students, if you ask them to share their screen, ensure that no other student can see the shared solution. 
* You can take a look at their work directly inside of zyBooks.
* Alternatively, the student can share their screen when they are in their own breakout room with you.

## Forum

When answering questions on the forum, point students to the appropriate concepts, slides, lecture notes, or book chapters, since sometimes they ask questions that are almost directly from the assignments.
* If something is difficult to find, let the instructor know, so that we can add it to the quick links, highlight it during the review, etc.

Direct them to the post with the initial **“Posting guidelines”** post if they are missing relevant information in their post.

Also, when answering questions on the forum _please double-check if the student posted anonymously_ to their classmates before using their name! If they posted anonymously, please **do not** address the student by their name.

Mark duplicate posts/questions as such, instead of responding to them again.


## zyBook

See the relevant links under [the "How to" section]({{ site.url }}{{ site.baseurl }}/howto#zybooks).

### Releasing the labs
Note that the new labs will always be hidden, _until **at least one test** is added to them_.

### Make a lab optional

1. From the main textbook page (the one that lists all chapters), click on the ["Configure zyBook" link at the top right](https://zybooks.zendesk.com/hc/en-us/articles/360007903633-How-to-configure-your-zyBook). 
1. Select the lab on the left (by placing a checkmark next to it) and click on the link on the right that reads “Set selected sections as optional”. _Note: do not mark as optional the book sections without first notifying/consulting with the instructor._
 
### Reorder labs
From the main textbook page, click on "Configure zyBook", then drag the labs by the tri-line icon on the left to reorder them. _Note: do not reorder the book sections without first notifying/consulting with the instructor._


### Lab guidelines

Read over the labs to ensure that they follow the format that was outlined in [the sample lab on the course website](https://ucsb-csw8.github.io/w22/ref/labtocode/#sample-lab-instructions):
* learning objectives that help students review the relevant zyBooks sections (Read more about learning objectives [here](https://ucsb-teaching-cs.github.io/s21/hw/teaching_demo/#select-your-topicconcept-and-determine-the-learning-goals).)
    - **DO NOT USE** "learn" and "understand" in the learning objectives
    - use action verbs that explain what students should be able **to DO** / _practice_ in this lab or know _how to use_ before doing the lab
* introduction that explains the motivation for the lab and provides the necessary information/data/clarifications
* clearly states whether to define a function or write a program
    * Checklist for a function: 
        - description of what needs to happen that can go into a doctring
        - name
        - number of parameters and their types
        - print / return / both?
    * Checklist for a program (written in the `if __name__ == "__main__"` block):
        - what input is needed
        - how/where to call the function
        - what output is needed and in what format
        - one or two example input and the corresponding output

* Include a **"Test your code"** section that provides two or more example scenarios for students to check their code with.
* Add a few Hints for the tricky concepts: e.g., a reminder of how to use a built-in function/method that they can use or what it does.
* A "Troubleshooting" section, if appropriate - best to add it to the class website's Troubleshooting section

Make sure that the code template provided for students is very clear and uses proper documentation.

Lab skeleton:

```
# Learning objectives
In this lab, you will practice
* 

# Instructions
motivation for the lab and the necessary information/data/clarifications

# Test your code
If the input is:
XXX

the output is:
YYY

# Hints / Troubleshooting

TBA

---
Code template -- this section is for the lab creators -- **remove the comments before publishing the lab**!

Make sure that the code template provided for students is very clear and uses proper documentation.

def func():
    """
    The function 
    Returns
    """
    pass
# Get from the lab instructions:
# description of what needs to happen that can go into a doctring
# function name
# number of parameters and their types
# print / return / both?

if __name__ == "__main__":
    pass
# Get from the lab instructions:
# what input is needed
# how/where to call the function
# what output is needed and in what format
# one or two example input and the corresponding output


```

## Gauchospace / Gradescope

The setup for these platforms is more involved and our specific setup and considerations for this quarter are [documented here]({{ site.url }}{{ site.baseurl }}/howto).
* [(S21) Quiz creation and considerations](https://docs.google.com/document/d/1B8s-7H_cU8DOyHuqZrZo1wP-HQ63qlFI7jp2zJmsRQc/edit#heading=h.smt0w1ynkxrc)
* [F21 Quiz creation and considerations](https://docs.google.com/document/d/1pMx6lfBUvLBz_HtiWwgjwM8ebrzWt1ojr4aFZlzCoA4/edit#heading=h.smt0w1ynkxrc)
* [F21 team drive with How-to videos](https://drive.google.com/drive/u/0/folders/1GzMXjrUsQ8LUz8FvX3HwEl-8iV8X3vrE)
