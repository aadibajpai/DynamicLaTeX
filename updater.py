"""
Made by Aadi Bajpai <me AT aadibajpai DOT me>, originally for personal use.
Don't use my résumé lol, but feel free to use the LaTeX template
You'll probably need to modify the variables for your own use
"""

import requests
import subprocess
import os
from bs4 import BeautifulSoup


def update_resume():
  r = requests.get('https://pepy.tech/project/swaglyrics')
  soup = BeautifulSoup(r.text, "html.parser")

  dl = soup.td.string

  tex = r'''
  \documentclass[letterpaper,11pt]{article}

  \usepackage{latexsym}
  \usepackage[empty]{fullpage}
  \usepackage{titlesec}
  \usepackage{marvosym}
  \usepackage[usenames,dvipsnames]{color}
  \usepackage{verbatim}
  \usepackage{enumitem}
  \usepackage[pdftex]{hyperref}
  \usepackage{fancyhdr}


  \pagestyle{fancy}
  \fancyhf{}
  \fancyfoot{}
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\footrulewidth}{0pt}


  \addtolength{\oddsidemargin}{-0.375in}
  \addtolength{\evensidemargin}{-0.375in}
  \addtolength{\textwidth}{1in}
  \addtolength{\topmargin}{-.5in}
  \addtolength{\textheight}{1.0in}

  \urlstyle{same}

  \raggedbottom
  \raggedright
  \setlength{\tabcolsep}{0in}


  \titleformat{\section}{
    \vspace{-4pt}\scshape\raggedright\large
  }{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]


  \newcommand{\resumeItem}[2]{
    \item\small{
      \textbf{#1}{: #2 \vspace{-2pt}}
    }
  }

  \newcommand{\resumeSubheading}[4]{
    \vspace{-1pt}\item
      \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
        \textbf{#1} & #2 \\
        \textit{\small#3} & \textit{\small #4} \\
      \end{tabular*}\vspace{-5pt}
  }

  \newcommand{\resumeSubItem}[2]{\resumeItem{#1}{#2}\vspace{-4pt}}

  \renewcommand{\labelitemii}{$\circ$}

  \newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=*]}
  \newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
  \newcommand{\resumeItemListStart}{\begin{itemize}}
  \newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}


  \definecolor{lightGray}{gray}{0.6}
  \definecolor{darkGray}{gray}{0.3}



  \begin{document}

  \begin{tabular*}{\textwidth}{l@{\extracolsep{\fill}}r}
    \textbf{}{\Large Aadi Bajpai} & website // \href{https://aadibajpai.me}{aadibajpai.me}\\
    Senior Year & email // \href{mailto:me@aadibajpai.me}{me@aadibajpai.me} \\
      \today & number // +91-93-3661-6656 \\
  \end{tabular*}

  \section{Education}
    \resumeSubHeadingListStart
      \resumeSubheading
        {Delhi Public School Kalyanpur}
        {\color{lightGray}Kanpur, India}
        {All India Senior School Certificate Examination, CBSE}
        {\color{lightGray}May 2019 (Exp.)}
      \resumeSubheading
        {Delhi Public School Kalyanpur}
        {\color{lightGray}Kanpur, India}
        {All India Secondary School Examination, CBSE;  CGPA: 10/10}
        {\color{lightGray}May 2017}
        \vspace{-3.5mm}
    \resumeSubHeadingListEnd


  \section{Awards \& Honours}
    \resumeSubHeadingListStart
      \resumeSubheading
        {Grand Prize Winner, Google Code-in 2017}
        {\color{lightGray}Google}
        {\color{darkGray}\href{https://ccextractor.org}{CCExtractor Development}}
        {\color{lightGray}November 2017 - January 2018}
        \resumeItemListStart
          \item { Among fifty winners from over 3500 contestants for \textbf{two months of exceptional contribution} to open source software.}
      \vspace{-1mm}
          \item {Worked on a real-time Continuous Integration/Continuous Deployment platform written in Python and Flask making \textbf{over 30 commits}.} 
          \item {Completed \textbf{all [Harddesign] tasks} and designed the \href{https://dribbble.com/shots/4422512-For-CCExtractor-Development-My-GCI-Org-3}{\textbf{new organization logo}.}}
       \resumeItemListEnd
       
       \resumeSubheading
       {Finalist, Topcoder Humblefool Charity Hackathon}
       {\color{lightGray}{Topcoder}}
       {\color{darkGray}{\'Evariste}}
       {\color{lightGray}December 2017 - February 2018}
       \resumeItemListStart
       \item \textbf{Competed among college teams} to develop an application that furthers and provides ease-of-access to programming education and resources in India.
       \item Developed \textbf{``HumbleHelper''} using Ruby on Rails and Material Design hosted on IBM Bluemix and were \textbf{ranked 5th nationwide}.
       \resumeItemListEnd
       
  \resumeSubHeadingListEnd

  \section{Achievements}
    \resumeSubHeadingListStart
      \item{Awarded \textbf{10 years' Scholar Badge} by DPS Kalyanpur for consistent \textbf{\\ excellent academic performance}}
      \hfill\textit{\color{lightGray}2007 - 2018}
      \vspace{-3mm}
      \item {Qualified for the \textbf{Indian National Olympiad in Informatics 2019}}
      \hfill\textit{\color{lightGray}2018}
      \vspace{-3mm}
      \item {One out of the only two people in the city to successfully clear Indian \textbf{\\ Zonal Computing Olympiad 2019}}
      \hfill\textit{\color{lightGray}2018}
      \vspace{-3mm}
      \item {Successfully completed the \textbf{Microsoft Hacktoberfest Challenge}}
      \hfill\textit{\color{lightGray}2018}
   
      \vspace{-1.5mm}
      \item {Awarded the \textbf{General Proficiency} Award by DPS Kalyanpur for academic excellence.}
      \hfill\textit{\color{lightGray}2015}
      \vspace{-3mm}
      \item {Won several \textbf{National Level} Model UN Conferences}
      \hfill\textit{\color{lightGray}2015 - 2018}
      \vspace{-3mm}
      \item {Won multiple \textbf{National Level} Inter-School Quiz Competitions}
      \hfill\textit{\color{lightGray}2014 - 2018}
      \vspace{-1.5mm}
  \resumeSubHeadingListEnd


  \section{Work Experience}
    \resumeSubHeadingListStart
      \resumeSubheading
        {Volunteer Developer}
        {\color{lightGray}CCExtractor Development}
        {\color{darkGray}Under Carlos Fernandez Sanz, Org Admin and Founder}
        {\color{lightGray}November 2017 - Ongoing}
        \resumeItemListStart
          \item {Mentored participants as a part of Google Code-in 2018.}
      \vspace{-1mm}
          \item {Created various tasks and reviewed over 250 instances of tasks throughout the contest.}
      \vspace{-1mm}
          \item {Contributed to multiple projects, added features and fixed issues.}
      \vspace{-1.5mm}
       \resumeItemListEnd
       
      \resumeSubheading
        {Software Development}
        {\color{lightGray}Personal Projects}
        {\color{darkGray}Application development and open-source contributions}
        {\color{lightGray}February 2017 - Ongoing}
        \resumeItemListStart
          \item {Notably, developed Python Package \textbf{``SwagLyrics For Spotify"} which has \textbf{%(dl)s users} as of \today.}
      \vspace{-1mm}
          \item {Made \textbf{1,000 GitHub contributions} in 2018, also contributed to open-source repositories such as Reddit, Microsoft and Node Package Manager.}
      \vspace{-1mm}
          \item {GitHub Developer Program Member.}
      \vspace{-1.5mm}
       \resumeItemListEnd
       
      \resumeSubheading
        {Member, Open Source Initiative}
        {\color{lightGray}Open Source Initiative}
        {\color{darkGray}Open Source Advocate}
        {\color{lightGray}December 2018 - Ongoing}
        \resumeItemListStart
          \item {The Open Source Initiative (OSI) is a non-profit corporation with global scope formed to educate about and advocate for the benefits of open source and to build bridges among different constituencies in the open source community.}
      \vspace{-1mm}
          \item {We're the stewards of the Open Source Definition (OSD) and the community-recognized body for reviewing and approving licenses as OSD-conformant.}
      \vspace{-1mm}
          \item {Major organizations such as \textbf{Mozilla, the Wikimedia Foundation and Linux} are affiliated to the OSI.}
      \vspace{-1.5mm}
       \resumeItemListEnd    
  \resumeSubHeadingListEnd


  \section{Programming Skills}
   \resumeSubHeadingListStart
      \item{\textbf{Languages}
      {: C++ {\color{lightGray}//} Python {\color{lightGray}//} HTML {\color{lightGray} // }CSS + SASS {\color{lightGray} // }Javascript {\color{lightGray} // }A Programming Language (APL)}}
          \vspace{-3mm}
      \item{\textbf{Software and Utilities}
      {: \LaTeX{} {\color{lightGray} // }Flask {\color{lightGray} // }Jinja2 {\color{lightGray} // }HAML {\color{lightGray} // }Git {\color{lightGray} // }Material Design {\color{lightGray} // }Adobe Illustrator}}
          \vspace{-1.5mm}
   \resumeSubHeadingListEnd

  \section{Positions of Responsibility}
  \resumeSubHeadingListStart
        \item \textbf{Head Boy} {\color{darkGray}Student Council, DPS Kalyanpur}
        \hfill\textit{\color{lightGray}April 2018 - Present}\\
      
      \vspace{-1mm}
      
      \item \textbf{Editor-in-Chief} {\color{darkGray}Muse, DPS Kalyanpur}
          \hfill\textit{\color{lightGray}April 2018 - Present}\\
          
      \vspace{-1mm}
      
      \item \textbf{President} {\color{darkGray}Model UN Club, DPS Kalyanpur}
          \hfill\textit{\color{lightGray}April 2017 - March 2018}\\
          
      \vspace{-1mm}

      \item \textbf{Secretary-General }
          {\color{darkGray}Delhi Public School Kalyanpur Model UN}
          \hfill\textit{\color{lightGray}August 2017 - September 2017}\\
          
      \vspace{-1mm}

      \item \textbf{President} {\color{darkGray}UN Security Council, Delhi Public School Kalyanpur Model UN}
          \hfill\textit{\color{lightGray}October 2018}\\
          
      \vspace{-1mm}

      \item \textbf{Core Team Member} {\color{darkGray}Panorama, DPS Kalyanpur}
          \hfill\textit{\color{lightGray}August 2017 - October 2018}\\
          
      \vspace{-1mm}

      \item \textbf{Head of Design} {\color{darkGray}Delhi Public School Kalyanpur Model UN}
          \hfill\textit{\color{lightGray}September 2016}\\
          
      \vspace{-1mm}
      
      \item \textbf{House Prefect} {\color{darkGray}Shamrock House, DPS Kalyanpur}
          \hfill\textit{\color{lightGray}April 2016 - March 2017}\\
          
      \vspace{-1mm}
  \resumeSubHeadingListEnd

  \section{Relevant Links}
      \vspace{1mm}
      \resumeSubHeadingListStart
          \item \href{https://dribbble.com/aadibajpai}{\textbf{\underline{I Design.}}}\\
          \vspace{1mm}
          \item \href{https://github.com/aadibajpai}{\textbf {\underline{I Code.}}}\\
          \vspace{1mm}
          \item \href{https://medium.com/@aadibajpai}{\textbf {\underline{I Write.}}}\\
          \vspace{1mm}
      \resumeSubHeadingListEnd

  \end{document}
  ''' % {"dl":dl}

  # print(tex)
  with open('aadi_resume.tex', 'w') as f:
  	f.write(tex)

  cmd = ['pdflatex', '-interaction', 'nonstopmode', 'aadi_resume.tex']
  proc = subprocess.Popen(cmd)
  proc.communicate()

  retcode = proc.returncode
  if not retcode == 0:
      os.unlink('aadi_resume.pdf')
      raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 

  for ext in ['tex', 'aux', 'out', 'log']:
  	os.unlink(f'aadi_resume.{ext}')


if __name__ == '__main__':
  updater()