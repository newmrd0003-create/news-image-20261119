# THE WORLD — Thursday, 19 November 2026

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/news-image-20261119)

A one-image front page summing up 19 November 2026's world news in six
stories, drawn entirely with Python's PIL — no external images, no network.

## The six stories

1. **Trump, Xi and Putin meet in Shenzhen** — trilateral talks on Thursday
   19 November on the sidelines of APEC; Trump in China for the first time
   since his return to office.
2. **GTA VI rolls out worldwide** — after a 13-year wait, Grand Theft Auto VI
   begins its global rollout, returning players to Vice City.
3. **Jeffries nominated Speaker** — Democrats nominate Hakeem Jeffries for
   Speaker of the House, the first Black American to hold the post.
4. **Cyclone Akvan nears landfall** — a Severe Cyclonic Storm in the Bay of
   Bengal intensifies; landfall due 20 November, with winds 120–130 km/h
   gusting to 145 km/h.
5. **Voyager 1, one light-day out** — after almost 50 years in space, NASA's
   Voyager 1 probe reaches one light-day from Earth.
6. **EU plans €45bn Ukraine loan** — Brussels proposes a €45 billion loan for
   Kyiv, to be repaid after Russia pays war reparations.

## Run

```sh
python3 gen_image.py   # writes entry.png (1024x1024, deterministic)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
