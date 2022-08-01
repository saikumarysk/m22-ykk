---
layout: page
title: Admin
nav_exclude: true
description: A feed containing all admin-related pages.
---

# Admin-related info

Starting with the course checklist and the TA responsibilities, the relevant admin-side info is below.

These pages are stored in the `_admin` directory and rendered according to the layout file, `_layouts/admin.html`. 

{% assign pages = site.admin %}
{% for apage in pages %}
<a href="{{ apage.url }}">apage.title</a>
{% endfor %}

---


# CSW8 course prep checklist
{:.no_toc}

Hello!

Congratulations on being assigned as an instructor for CSW 8. :-) You are going to have a blast!

This document is an attempt to document and formalize/operationalize the process of booting up a new instance of this course.

YK’s workflow is as follows: first, create the resources, documents, etc. and then, when all mentors have signed their contract, add them to the respective resources.
The checklist is structured to reflect this: first, you set up and collect the materials that do not require the team, then you save their info to a CSV by collecting it from the DocuSign emails, and proceed with the rest of the set up.

Previous versions of this checklist: 
- S21, 
- F21, 
- W22, 
- [S22](https://docs.google.com/document/d/1t6fS7oD3RkFryGOg1ls7THoLG3QOygCUOBgT3Mx1lHU/edit#)

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Course Preparation Checklist
### Adopt the zyBook (online textbook)
- [ ] Request to adopt the most appropriate version of zyBooks (the most recent is best or most relevant summer version)
- [ ] Update the “From your instructor” section (if necessary)
- [ ] Get the subscription instructions from the right sidebar of the zyBook and post them on Gauchospace 

### Create a shared folder
- [ ] Create a Google Drive folder (e.g., \_CSW8-QQ) to keep track of your notes, slides/videos/handouts, and files for your own reference.
- [ ] Bookmark it in your browser
- [ ] Copy this checklist to this folder (if in a doc)

### Create a Shared Google Drive folder for Team Resources.
- [ ] Create \_CSW8-QQ-PUBLIC with the materials for the class
- [ ] Add a shared folder for lab presentations / resources
    - [ ] Add this link to the Slack’s quick access links
- [ ] Add a template for that quarter’s slides (at a minimum, change the quarter on the title slide)
- [ ] Add a link/shortcut to previous lab materials 
    - [ ] Add this link to the Slack’s quick access links
- [ ] Create \_CSW8-QQ-Team for the materials for the TAs/ULAs 
    - [ ] Add the ASE form for TAs and ULAs (See below for things to check)
    - [ ] Update the ASE form according to the new quarter 


### Create/set up the course website.
- [ ] See the  [github README](https://github.com/ucsb-csw8/m22-ykk)  for links
- [ ] Fork / Copy the previous quarter’s website

Follow the “Getting Started” notes in the README; e.g., use the “Local development environment” notes to preview the site on your computer, before pushing it to github – use the `./jekyll.sh` “script”/shortcut to run the bundle command
- [ ] Update the website pages (depending on how many changes you are making to the previous structure, it can take around 2-4ish hours to go through all the pages and verify that the info is consistent with the course policies and that you know what question to send the students to)

_If using the website, add the files below as markdown files; otherwise, add them as documents in the shared folders._
- [ ] Update the Syllabus  ([F21 doc](#), W22, S22)
    - [ ] use the [instructional Checklist](https://docs.google.com/document/d/16sj-tbPSpnNRaoB673qjhWxel1E4YB88DxVi4AjtH_8/edit) to see if all’s there
- [ ] Create/update the Course schedule
    - [ ] Get a list of [university holidays](https://registrar.sa.ucsb.edu/calendars/calendars-deadlines/academic-calendars)
    - [ ] Add the holidays to [the script](https://github.com/ucsb-csw8/s22/blob/main/_modules/generate_weekly_calendar.py)
    - [ ] Add [drop dates](https://registrar.sa.ucsb.edu/calendars/calendars-deadlines/registration-pass-dates)
    - [ ] Create the weekly structure by running the relevant scripts in the `_modules` folder
    - [ ] Cement the exam/project dates → manually update week 1 and 11 / finals week

The Google forms were added (to avoid email)
as part of the website's `_config.yml` for ease of updating (currently the forms are used in the `about.md` and the `faq.md`)
- [ ] [“a fully-anonymous form” that goes directly to the prof](https://ucsb-csw8.github.io/s22/faq/#getting-help)
- [ ] [Request for an extension](https://ucsb-csw8.github.io/s22/about/#request-for-accommodations)
- [ ] [Regret form](https://ucsb-csw8.github.io/s22/about/#regret-clause-and-academic-integrity)


### Set up the course on Gauchospace.
- [ ] Open up the Gauchospace site and bookmark it.
- [ ] [Restore the previous course setup](https://help.lsit.ucsb.edu/hc/en-us/articles/202535454#copy2015-2021)
- [ ] Use the “Turn Editing On” yellow button and update the weekly tabs 
- [ ] hide all weeks/tabs, other than Week 0/1
    
If using the website, **update the schedule there first**, for easy copy-paste of the weekly pattern to Gauchospace.
**IMPORTANT**: make sure to keep the website updated with the changes made directly on Gauchospace. Best to update the website and then copy the change to Gauchospace.

- [ ] Update the quick access links and zyBooks subscription info

#### Create groups on Gauchospace
If running quizzes on Gauchospace, set up the extended-timing groups for DSP students. 
Add the students as their DSP letters come in to your inbox (accessible via https://dsp.sa.ucsb.edu)

- [ ] Create groups **extra-x1.5** and **extra-x2** for DSP students 

Once you get the team and their contact info, add them to their own group for quick access.
You can use a bulk upload from the course-level “Administration” sidebar option to “Add …”.

- [ ] Create a group “Mentors” 
    - [ ] Add the TAs and ULAs to the group “Mentors”     
    - [ ] Set up the Editing/Non-editing TA roles, based on the roles
    
The last task can be accomplished via the “People” tab, click on the “Filters” link, filter by the group “Mentors” and apply Editing/Non-editing TA roles, based on their roles.

#### Update the reflection forms

In the first week, the weekly reflection form is just the ["Welcome survey"]().

- [ ] Link the Welcome survey on Gauchospace 
- [ ] Copy the reflection forms for other weeks to get them ready for possible updates


#### Update the welcome message on Gauchospace

- [ ] Provide the information that will be emailed to students as soon as the Gauchospace goes live
- [ ] Set up the dates on Gauchospace and make the site visible when ready

---

### Add the team resources
- [ ] Add/update the Team Guidelines ([W22](https://ucsb-csw8.github.io/w22-staff/guidelines/), [current]({{ site.url }}/{{ site.baseurl }}/admin-guidelines))
- [ ] Add the breakdown of roles and responsibilities ([F21 doc](https://docs.google.com/document/d/1qfYCtHcNDwBbDXv_hBVhmLECUx1-jH0NEsMOLnz7NKM/edit?usp=sharing), [W22](https://ucsb-csw8.github.io/w22-staff/), [M22](https://docs.google.com/spreadsheets/d/1_dSrnLc0QSc3OM8zoQmE7XRgHSaTwcGr77LTHi2peiw/edit#gid=1097265728))
- [ ] Share [the spreadsheet](https://docs.google.com/spreadsheets/d/1_dSrnLc0QSc3OM8zoQmE7XRgHSaTwcGr77LTHi2peiw/edit?usp=sharing) where they can select their role preferences.
- [ ] Create/update the weekly pattern of work / schedule for the mentors based on the course deadlines

Once you have the team and their emails, create a list with their names and @ucsb.edu addresses as well as @umail.ucsb.edu (e.g., needed for Zoom) - see below how to get the initial list from Google contacts.

- [ ] Get the staff / mentors info:
- [ ] Collect the names and email addresses of the TAs and tutors (Both: paid and 190J) from their DocuSign confirmation emails
- [ ] Add the emails to a new group, e.g., cs8-s22-staff: https://contacts.google.com (Makes it easier to email them and/or create shared Google folders/docs).
- [ ] Gmail contacts allows you to Create a CSV that lists their names / UMail email addresses (for Zoom, Gradescope, forum (Piazza or Campuswire)) -


### Add the team to the resources

Each TA/mentor is added to the following:
- [ ] Gauchospace https://gauchospace.ucsb.edu (grades, quizzes, schedule, links, reflections)

- [ ] Gradescope https://www.gradescope.com (quizzes and/or assignments/grades)

- [ ] Forum: Piazza https://piazza.com/

- [ ] Co-host on Zoom https://ucsb.zoom.us/meeting#/  (use your @umail.ucsb address and please change your name on Zoom to include the word _MENTOR before your name and add your pronouns (https://support.zoom.us/hc/en-us/articles/4402698027533))

- [ ] Calendar invitation for the weekly meeting

- [ ] Zybooks https://learn.zybooks.com/library

- [ ] Shared Google Drive folder (helpful internal resources and docs)

- [ ] internal/hidden github repo for assignment/autograder development/management

- [ ] Slack (self-sign-up)

### Create/set up the communication channels.
#### Set up course forum
Set up Piazza/Campuswire to communicate with the class.
- [ ] Turn off global anonymous posting
- [ ] Add custom folders (e.g., grading, troubleshooting, project1-2)
- [ ] Add the TAs
- [ ] Add the students (get the CSV roster from egrades)

#### Set up Slack
Set up Slack to communicate with the course mentors (TAs/tutors).

- [ ] Add the channels for each week, meeting-notes, references

- [ ] Create a #_quick-access channel 
- [ ] Create an #action-items channel for meeting notes and next steps
- [ ] Create an #lab-notes channel for notes regarding lab preparation / setup
- [ ] Create a #week-XX channel for easy sorting of the messages by the related week
- [ ] Add the intro message (see below)
- [ ] Add reference links (see Bookmarks)

#### Slack intro message

```
:wave: Hi everyone! @channel

I highly recommend that you download the Slack app, since the experience is much better than using the website.

Here are a few guidelines and suggestions to streamline our communication.

* Try to keep _**related**_ conversations in threads (use the "Reply in thread" speech bubble :speech_balloon:  icon that shows up on the right when you hover over the message)
* :star2::exclamation: **Make sure to tag me** (using @K) in any messages that you need me to see :eyes:, respond to :speaking_head_in_silhouette: or take action on :arrow_right:. (I might not see your message otherwise. :see_no_evil: )
* Any message that you are tagged in or that contains an :arrow_right: action item, please mark it with a +1 :+1: or a checkmark :heavy_check_mark: emoji to let me know that you've seen/done it :white_check_mark:.    
:arrow_right: Practice doing so on this note. :wink: 

I encourage you to customize your sidebar on slack to allow you to quickly access messages and catch up on what you missed.
:arrow_right: Go to "Preferences" (on the desktop client, click on the top-right icon and select "Preferences" from the dropdown.
Select the following items to be added to your "Sidebar":
*  All unreads
*  All DMs
*  Mentions & reactions
*  Saved items

Sometimes, you see a message at a time when you can't address it right away. It's easy to skim something on Slack and then forget to follow up on a message, so to remember to come back to it, set a reminder about a specific message on Slack. :alarm_clock:
On a desktop client:
hover over the message and click on the tri-dot `"More actions"` on the right hand side, 
:arrow_right: select `"Remind me about this"`, 
and then select when you want the Slackbot to ping you about the message on Slack. :hourglass_flowing_sand:

If you have any other helpful Slack tips, please share them by responding to this note.
```

– 

Other notes for the team:

Whenever you are responding to a message on Piazza, please be very cognizant as to whether it was posted anonymously.
It might be best to never use students' names in your reply than for you to address by name a student who posted something anonymously to classmates.

Also, please make sure that you are on time for your office hours. Remember to `*add the chime*, so that you know whether someone joined or is in the waiting room.
when you have OH make sure you turn on “play join and leave sound” from the Participants tab on Zoom

FYI : If any of you ever need to adjust your office hour times on the course website, you can do so by submitting a Pull Request (PR) after updating this file:
https://github.com/ucsb-csw8/s22/blob/main/_schedules/weekly.md
(same process as what you went through to add your bio: update the file in your forked repo, then submit a PR)



### Bookmarks

Add this to your "Saved items" by hovering over the message and clicking on the bookmark icon 

Suggested Browser Bookmarks:
* Top-level Google Drive folder
* Shared Team Drive folder
* Gauchospace course link
* Gradescope course link
* Piazza course link
* zyBooks
* syllabus https://ucsb-csw8.github.io/s22/about/
* Office hours & who's available when 
* Zoom link
* Previous lab recordings

M22 Browser Bookmarks:
* Top-level Google Drive folder https://drive.google.com/drive/u/0/folders/15fi4dWR0UAJFFUI_zfOR8wn7-qIj-UP9
* Shared Team Drive folder https://drive.google.com/drive/u/0/folders/1tNJBGbuxx6plvkAtmLQNBF1qPULftFGU
* Gauchospace course link https://gauchospace.ucsb.edu/courses/course/view.php?id=24892
* Gradescope course link https://www.gradescope.com/courses/412207
* Piazza course link https://piazza.com/class/l6am3wbct272u9
* zyBooks https://learn.zybooks.com/zybook/UCSBCMPSCW8KharitonovaSesssionBSummer2022
* syllabus https://ucsb-csw8.github.io/m22-ykk/about/
* Office hours & who's available when https://docs.google.com/spreadsheets/d/1_dSrnLc0QSc3OM8zoQmE7XRgHSaTwcGr77LTHi2peiw/edit?usp=sharing
* Zoom link
* Previous lab recordings


* S22 Lab recordings: <https://drive.google.com/drive/u/0/folders/1xdXxzGf62b7BJ4b3dW0LILRA2Jx_tlz7>
* (Old) W22 lab recordings: <https://drive.google.com/drive/folders/1A82X62Wazhi4CwDsconmHiH4N7i6Eb2Q?usp=sharing>

---

# Links to other admin pages
* [Guidelines]({{ site.url }}/{{ site.baseurl }}/admin-guidelines)
* [How-to]({{ site.url }}/{{ site.baseurl }}/admin-howto)

