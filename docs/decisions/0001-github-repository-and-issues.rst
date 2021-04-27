============================
GitHub Repository and Issues
============================

-------
Status
-------

Provisional

-------
Context
-------

The `Build-Test-Release Jira board
<https://openedx.atlassian.net/jira/software/projects/BTR/boards/641>`_ suffers
from a debilitating limitation: it does not allow tagging of members on issues.
This hinders communication severely, so a different solution is required.
Plus, usage requires an Atlassian account, which not everyone has and is,
therefore, a significant hindrance for general community acceptance.

Given that both the Community and Core Commiter working groups are moving to
`GitHub Projects <https://github.com/features/project-management/>`_ to solve
similar issues, it makes sense for the Build-Test-Release working group to do
the same.

Using GitHub Projects requires a repository to "back" it, and creating a
dedicated one for this group would be a good idea even if it weren't necessary.
For one, it will be a good place to store ADRs such as this one.

---------
Decisions
---------

1. A repository will be created for the Build-Test-Release working group in the
   ``openedx`` organization and named ``build-test-release-wg``.

2. Upon acceptance of this ADR, all new issues will be created against the
   `Everything <https://github.com/openedx/build-test-release-wg/projects/1>`_
   GitHub project.

3. All old issues that are still relevant will be copied over from the `Jira
   board <https://openedx.atlassian.net/jira/software/projects/BTR/boards/641>`_.

------------
Consequences
------------

It is hoped that doing this will make it easier for the group to create and
manage tickets, and for the community in general to use it.
