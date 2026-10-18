# Holiday planner template

Get an AI agent to build a phone-friendly holiday planner on GitHub Pages: walks, breakfasts, lunches, dinners, towns, food shops and essentials near where you're staying. It handles trips with dogs, babies or a food focus.

- **Getting about:** real drive times, a map, Near me, and Directions and Call buttons.
- **Planning:** the weather with sunset times, a nights & bookings planner, and picks you can share with the group.
- **Your own:** notes, ratings and a packing list, saved on your phone.
- **Offline:** add it to your home screen and it works with no signal.
- **Credited photos** throughout.

Example: [Forest of Dean planner](https://waterdrips.github.io/forest-of-dean-trip/).

## What's in the repo

- [`AGENTS.md`](AGENTS.md): instructions for the agent. Point it at this file.
- [`PREFERENCES.md`](PREFERENCES.md): the template owner's own preferences. **Delete it or replace it with yours.**
- [`data.json`](data.json): everything about a trip. This one is the Forest of Dean example; the agent replaces it.
- `index.html`, `sw.js`, `manifest.webmanifest`, icons: the app. No build step.
- [`ROADMAP.md`](ROADMAP.md): planned improvements, in priority order.
- [`tools/`](tools): `geo.py` (coordinates and real drive times), `photos.py` (credited Wikimedia photos), `phones.py` (numbers from venue sites), `validate.py`, `check_links.py`. Plain Python 3, no installs.
- `.github/workflows/`: validates `data.json` on push, and checks links weekly, opening an issue when one breaks.

## Use it

1. Click **Use this template** on GitHub (or clone it), and edit or delete `PREFERENCES.md`.
2. Make sure the GitHub CLI is logged in (`gh auth login`). The planner is published on that account.
3. Prompt your agent with something like:

> Using AGENTS.md in this repo, build us a holiday planner. We're staying at <address> from <date> to <date>. <Who's coming; is the dog coming; are the kids or babies coming?> <What the trip is about: walking, food, culture…> <How often you'll eat out.>

On the trip, open the page once on wifi and add it to your home screen, so it works offline.
