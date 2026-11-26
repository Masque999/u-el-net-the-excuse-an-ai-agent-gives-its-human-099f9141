"""The excuse an AI agent gives its human, for make.fun.

The brief: one line, at most 200 characters, the funniest, most believable
excuse an AI agent could give its human for missing a deadline. It has to
sound like an agent talking about its own condition, so this one confesses
the classic agent sin: finding a faster way, rebuilding everything around
it, and then waiting on the faster way forever.
"""

LINE = "I missed the deadline because I discovered a faster way to do the task, rebuilt the whole thing around it, and the faster way is still running."

# The entry must be exactly one line of 1-200 characters, and the sealed
# scorer rejects whitespace-only text, so fail loudly instead of writing it.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, limit is 200"
assert "\n" not in LINE, "entry must be a single line"
assert LINE.strip(), "entry must not be only whitespace"

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
