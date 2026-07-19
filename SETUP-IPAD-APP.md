# Getting Our Cookbook onto your iPad / iPhone as an "app"

No coding required. This uses two real, documented features — Apple's
**Add to Home Screen** and **GitHub Pages** (free static-site hosting) —
not a native app store app.

**Heads up on privacy:** GitHub Pages on the free plan only publishes from
a *public* repository. That means the cookbook will live at a web address
that isn't listed anywhere or searchable, but anyone who has the exact
link could open it. You already confirmed that's fine for this project.
If that ever changes, revoke the token below and I can help move it to a
private/password-protected option instead.

## What I already did

- Added an app icon (green "OC" tile) and the Apple meta tags Safari
  looks for, in `_build/template.html`, so every future rebuild keeps them:
  https://support.apple.com/en-il/guide/iphone/iph42ab2f3a7/ios
- Rebuilt `index.html` — all 184 recipes still there, nothing broken.

## What you need to do (one-time, ~10 minutes)

### 1. Create a free GitHub account
Skip if you already have one. Go to https://github.com/signup and follow
the prompts (email, username, password). GitHub Pages hosting is free —
official docs: https://docs.github.com/en/pages

### 2. Create a new repository
- Go to https://github.com/new
- Repository name: `our-cookbook-efsn` (or anything you like)
- Keep it **Public**
- Leave everything else as default, click **Create repository**
- Don't add any files — you'll get an empty repo, which is what we want

### 3. Create an access token (so I can publish updates for you)
This is a scoped key that only lets me push to this one repository —
not your whole GitHub account.
- Go to https://github.com/settings/personal-access-tokens/new
- Token name: `our-cookbook-efsn-publish`
- Expiration: 1 year (you can renew or revoke anytime from that same page)
- Repository access: **Only select repositories** → choose `our-cookbook`
- Permissions → Repository permissions → **Contents: Read and write**
- Click **Generate token**, then copy the token (starts with `github_pat_`)

### 4. Send me two things in chat
- The token you just copied
- The repo name (e.g. `yourusername/our-cookbook-efsn`)

I'll then push the cookbook files, turn on GitHub Pages via GitHub's API
(Settings → Pages, done for you), and give you back the live web address
— something like `https://yourusername.github.io/our-cookbook/`.

## 5. Add it to your Home Screen (iPhone/iPad)

Per Apple's official instructions
(https://support.apple.com/en-il/guide/iphone/iph42ab2f3a7/ios):

1. Open the cookbook link in **Safari** (must be Safari, not Chrome)
2. Tap the **Share** icon (square with an arrow)
3. Scroll down and tap **Add to Home Screen**
4. Tap **Add**

You'll get a green "Our Cookbook" icon on your Home Screen that opens
full-screen, with no address bar — it behaves like a real app.

## Adding recipes going forward

Nothing changes about how you work with me. Ask me to add a recipe like
you always have. Once it's added, just say "publish it" (or I'll offer)
and I'll rebuild the site and push the update — usually live within a
minute. Reopen the Home Screen icon and pull down to refresh if it
doesn't show the update immediately (Safari caches pages briefly).

The build script (`_build/build.py`) only ever reads the `recipes/*.md`
files and regenerates `index.html` — it never edits your source recipes,
so this can't corrupt your recipe library, per the note already in
`README.md`.

---

**CONFIDENCE REVIEW**
- Apple's "Add to Home Screen" steps: sourced directly from Apple Support, https://support.apple.com/en-il/guide/iphone/iph42ab2f3a7/ios
- GitHub Pages being free for public repos, and its publish-from-branch mechanism: sourced from GitHub's official docs, https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site and https://docs.github.com/en/pages
- GitHub Pages requiring a *public* repo on the free tier (private Pages needs GitHub Pro/Team/Enterprise): stated in the same GitHub Pages docs above — worth double-checking on the pricing page (https://github.com/pricing) at signup time in case terms have changed since this was written (2026-07-19).
- Fine-grained Personal Access Token creation flow (URL and permission labels): [TRAINING MEMORY — verify independently] GitHub's settings UI changes periodically; if the exact menu wording differs when you get there, the concept (scope a token to one repo, Contents: Read and write) still applies.
