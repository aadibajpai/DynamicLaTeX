# DynamicLaTeX :crystal_ball:

Your LaTeX document always has the latest numbers when clicked. Originally created for updating LaTeX resumes.

Highly extensible.

## 📜 Usage

- Define this new command in your LaTeX document:
```LaTeX
\newcommand{\py}[1]{\textit{\%#1\%}}
```

- Wherever you want to format the dynamic variable, use the command as:
```LaTeX
\py{<variable_name>}
```
- Add your LaTeX code in `resume.tex`.

- In `main.py`, add the same variable names and updation function to `template_values`. That's it!

Serve your pdf by running `main.py`. I've used my name in the endpoints so do change that with your own :)

There are a few updation helper functions provided in `updater.py` already as well.

## :grey_question: Why?

I use it to get the latest downloads count for SwagLyrics and SwSpotify then write that so the resume is always up to 
date. 
Previously, I had to update the download count manually. Now, it's accurate to the day you download my resume.

Try it in action at https://aadibajpai.me

I've deployed mine to a heroku instance. Compilation takes place online.

It is extensible as you can add as many variables as you want in your resume eg. GitHub contributions count and so on.
You can also edit when you want it to update as well as automate that with a cron job.
