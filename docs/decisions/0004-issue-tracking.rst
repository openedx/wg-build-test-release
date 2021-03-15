===================================
Documenting and tracking BTR Issues
===================================

-------
Status
-------

Draft

-------
Context
-------

With the move to a Github Project to manage tasks, the BTR needs to 
define a clear process for documenting and managing issues.

This document aims to outline a set of guidelines to manage the work of
the BTR group on Github. These guidelines that are expected to evolve 
to meet any particular need that arises.

Last update: 2021-03-15

---------
Decisions
---------

#. A piece of work should be created as a github issue. Github projects support notes, 
   however these are too basic and don't support the additional information issues allows 
   (for example, an assignee).

#. To assess and discuss each issue, we need to know:

   #. The type of issue: is it a bug? is it a gap in documentation?
        - Tagged with <type:'issue-type'>
        - Issue types: bug, enhancement, question, btr-task, security.
   #. For bugs, the release that is affected. 
        - Tagged with <affects:'named-released'>
   #. The severity of the issue.
        - Tagged with <priority:'priority-evel'>
        - High: This issue stops the installation or core functionality of the
          platform and has no workaround.
        - Medium: This issue affect a non-core part of the installation or the 
          platform and/or has a workaround.
        - Low: This issue doesn't impact the usability of the platform.
        - If in doubt between two levels of priority, assign the highest level and it 
          can be reviewed by other members of the group.

#. Responsibilities
    #. It is the responsibility of the person creating issue to appropriately 
       describe and tag it (affect, type, priority). The tags can be reviewed and 
       modified by the group.
    #. It is the responsibility of the Bug triager to link the issues to the 
       appropriate Milestone.

------------
Consequences
------------

This process for tracking and managing the work of BTR group members will make 
for better asynchronous management of the workload.