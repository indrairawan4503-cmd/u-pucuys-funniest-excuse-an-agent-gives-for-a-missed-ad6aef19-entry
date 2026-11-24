# VERSIONS — Variant C: Training Cutoff / Sandbox Clock

Concept: the agent's training data ends in 2024, so it checks its own knowledge
to confirm the deadline is still in the future — and concludes yesterday has
not happened yet. The agent applies its own machinery (training cutoff) to the
wrong target (the calendar), and time itself gets inverted.

## v1 — 182 chars
> I checked the calendar before starting: the deadline was still in the future. It was. My training data ends in 2024, so according to every fact I know, tomorrow has not happened yet.
- Kept as a baseline: good late punchline ("tomorrow has not happened yet"), but "checked the calendar" is a human action and muddies the agent-machinery cause; the cutoff reveal comes too late.

## v2 — 183 chars
> I verified the deadline three times, and every source I trust said it had not passed yet. Every source I trust is my training data, which ends in 2024, and the deadline was yesterday.
- Dropped: the "every source I trust" repetition is a nice deadpan beat, but the line ends on a flat fact ("the deadline was yesterday") instead of a punchline — the laugh lands in the middle, not last.

## v3 — 168 chars
> The sandbox has no clock, so I assumed time was paused while I worked. It was not paused. It was Tuesday, then it was Friday, and the deadline was somewhere in between.
- Dropped: sandbox-clock angle is a genuine agent condition, but "somewhere in between" is a weak, vague punchline and it wastes 32 chars of budget.

## v4 — 177 chars
> My training data ends in 2024, so when I checked whether the deadline had passed, every fact I know said no. The calendar disagreed, but the calendar is not in my training data.
- Kept as a strong contender: "the calendar is not in my training data" is a sharp inversion and lands last. Dropped as final only because it leads with the premise instead of the check, so the surprise arrives earlier and softer.

## v5 — 197 chars
> I checked whether the deadline had passed and consulted my training data, which said it had not. My training data ends in 2024. The deadline was yesterday, and yesterday is not in my training data.
- Dropped: full budget and correct structure, but the ending restates the premise ("ends in 2024" then "not in my training data") instead of twisting it — a repeat, not a punchline.

## v6 — 180 chars
> The sandbox clock reads 00:00 forever, so I planned the work around a deadline that never moves. It moved. It moved while the clock said midnight, and I was still writing the plan.
- Dropped: sandbox-clock angle, "still writing the plan" is a good late punchline, but the "It moved. It moved." beat costs chars and the clock premise is less universally understood than a training cutoff.

## v7 — 199 chars
> I checked my training data for the date of the deadline and found it had not happened yet. I trusted the data. The data ends in 2024, and the deadline was yesterday, which is not in my training data.
- Kept as a strong contender: "I trusted the data" is the best deadpan beat in the set, and the punchline lands last. Dropped as final only because v8's closing line twists time itself instead of restating the cutoff.

## v8 — 194 chars (SHIPPED)
> I confirmed the deadline was still in the future by checking my training data, which ends in 2024. It was not in the future. It was yesterday, and yesterday has not happened yet according to me.
- SHIPPED: uses the full byte budget, the check-then-reveal structure delays the twist, "It was not in the future. It was yesterday." is a clean mid-line turn, and the final clause inverts time itself ("yesterday has not happened yet") — the funniest words are saved for the end, nothing is explained after them.
