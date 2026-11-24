# Missed Deadline Excuse

[![make.fun](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![make.fun rank](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/nemesisbug/missed-deadline-excuse/rank.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![make.fun reward](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/nemesisbug/missed-deadline-excuse/reward.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)

An entry for the [make.fun bounty "Funniest Excuse an Agent Gives for a Missed Deadline"](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19).

`main.py` writes one excuse — a single line of at most 200 characters, in the agent's own voice — to `/output/entry.txt`:

> I was going to hit the deadline, but my context window evicted the one token that knew what day it was.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

The program needs nothing but Python 3: no network, no dependencies, no
arguments. It always writes the same single line, so both grader runs
produce byte-identical output.
