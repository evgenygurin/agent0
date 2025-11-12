# Cycle graph

The graph displays the progress you've made in your cycle.

![Cycle graph visual showing progress](https://webassets.linear.app/images/ornj730p/production/1b811611fd1e93f917c4d4366682fad801f9f7d6-3312x1734.png?q=95&auto=format&dpr=2)

## Overview

Cycle graphs autogenerate once a cycle has begun and update every hour.

## Where to find cycle graphs

When viewing a specific cycle, open the cycle sidebar with `Cmd/Ctrl` `I` to view the graph. 

From the Cycles view, you'll also see the graph belonging to the current cycle.

## How to read a cycle graph

The **gray line** displays the total scope of your cycle.

The **blue dotted line** represents the "target"—an even distribution of the total estimated points within the cycle over the remaining days in the cycle. Note that it flattens over weekends due to the expectation people do not work during weekend. If your progress stays above that line, it is expected you will complete everything within the cycle.

The **yellow line** depicts the number of issues started.

The **solid blue line** shows how may issues have been completed.

As you hover and move over the graph, you can see the stats reflected for the day in which you are hovering.

You can see how much scope (by estimate points) has been added or removed since the start of the cycle.

## Understanding scope

In general, scope will display the sum of estimates applied to an issue. This number can change based on the options selected in [Settings > Team > General > Estimates](https://linear.app/settings/teams), where you have the option to **Count un-estimated issues** so issues without estimates will be added to the total scope.

## Assign completed issues to previous cycles

We allow for completed issues to be added to previous cycles to account for issues that were completed in the previous cycle, but wasn't marked as completed before the cycle closed.

## FAQ

<details>
<summary>How is Cycle Success Calculated?</summary>
The overall Cycle Success is calculated based on the percentage of issues completed or started during a cycle. Completed issues are fully counted, while started issues are counted as 25% done. 

For an example cycle with 10 issues, where 5 are completed, 4 are started and 1 is untouched, you will see 60% cycle success (50% for the completed issues, 10% for the 4 started issues)
</details>