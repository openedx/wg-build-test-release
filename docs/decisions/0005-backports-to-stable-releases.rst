============================
Backports to Stable Releases
============================

-------
Status
-------

Draft

-------
Context
-------

During the Lilac.2 release process, `a backport request was made
<https://discuss.openedx.org/t/backporting-badgr-integration-updates-to-lilac/5440>`__
that raised the question:  where should the group draw the line when deciding
to merge a backport PR?

Traditionally, the group has merged bug fixes that have been merged to master,
but not features.  However, while the PR in question fixes a nominal bug *and*
has been merged to master, it does so via an extensive changeset that, among
other things, includes a migration.  It was decided during one of the group's
meetups that this was too risky to merge when weighed against the benefits:
there are too few users of Badgr to justify the backport to a stable point
release.

On the other hand, there have been exceptions to this rule.  Including, for
example, a preemptive decision to merge a PR that `revives the pre-Lilac
payment flow <https://github.com/openedx/build-test-release-wg/issues/74>__`
but by force of circumstance, will not be mergeable to master.

It is evident that finding an algorithmic way to determine whether a particular
PR should be merged to a particular point release will be difficult.  Instead
of trying to do so, the group proposes instead to analyze each PR on a
case-by-case basis.

--------
Decision
--------

Each PR that introduces changes to a stable release by way of its master branch
must be reviewed by the group and approved by `lazy consensus
<https://openedx.atlassian.net/wiki/spaces/COMM/pages/1022099494/Build+-+Test+-+Release+Working+Group#How-we-make-decisions>`__.
In other words, the change must be communicated so that group participants
where likely to see it, and enough time must have elapsed for objections to be
raised.  If no objections are raised, the change may be merged.

------------
Consequences
------------

This can make backporting code a little cumbersome, but the group considers
this a good thing: stable releases should be conservative when accepting
changes, otherwise they shouldn't be called "stable".
