# DynamicLaTeXResume :crystal_ball:

Updates LaTeX resume with the latest numbers on click if the data has changed.

## 📜 Usage

Add your LaTeX code and whatever variables you want to update in `updater.py`.

Then serve your pdf with `main.py`. 

Use the old `%s` python string formatting as LaTeX code has `{}` that you'll need to individuallly escape otherwise.

I've deployed mine to a heroku instance. Compilation takes place online.

The application updates the resume when the date since last updation has changed to avoid redundant updation.

## Why?

I use it to get the latest downloads count for SwagLyrics and write that so the resume is always up to date. Previously, I had to update the download count manually. Now, it's accurate to the day you download my resume.

It is extensible as you can add as many variables as you want in your resume eg. GitHub contributions count and so on.
