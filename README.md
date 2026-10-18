# Holiday planner template

Instructions and a starting page for getting an AI agent to build a phone-friendly holiday planner: walks, breakfasts, lunches, dinners, towns, food shops and essentials near where you're staying, with distances, Google Maps links, verified websites and credited photos, published on GitHub Pages. It handles trips with dogs, babies and food-focused trips.

- [`AGENTS.md`](AGENTS.md): the instructions. Point your agent at it.
- [`PREFERENCES.md`](PREFERENCES.md): the template owner's own preferences. **Delete it or replace it with yours.**
- [`reference/index.html`](reference/index.html): a finished example page, from a Forest of Dean trip ([live](https://waterdrips.github.io/forest-of-dean-trip/)).
- [`tools/photos.py`](tools/photos.py): fetches freely licensed Wikimedia Commons photos with credits.

## Use it

1. Click **Use this template** on GitHub (or clone the repo), and edit or delete `PREFERENCES.md`.
2. Make sure the GitHub CLI is logged in (`gh auth login`). The planner is published on that account.
3. Prompt your agent with something like:

> Using AGENTS.md in this repo, build us a holiday planner. We're staying at <address> from <date> to <date>. <Who's coming; is the dog coming; are the kids or babies coming?> <What the trip is about: walking, food, culture…> <How often you'll eat out.>
