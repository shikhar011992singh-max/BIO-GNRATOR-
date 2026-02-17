#CHALLNG: STYLISH BIO GNRATOR FOR INSTAGRAM/TWITTER

import textwrap

name = input("enter your name: ").strip()
proffession = input("enter your proffession: ").strip()
passion = input("enter your passion in one line: ").strip()
emoji   = input("enter your favourite emoji: ").strip()
website = input("enter your website: ").strip()

print("\n choose your style: ")
print("1. Simple lines ")
print("2. Vertical flair ")
print("3. Emoji sandwich ")

style = input("enter 1, 2 or 3: ").strip()

def generate_bio(style):
      if style == "1":
            return f"{emoji} {name} | {proffession} \n {passion} \n {website}"

      elif style == "2":
            return f"{emoji} {name} \n {proffession}🔥\n {passion} \n {website}🔥"

      elif style == "3":
            return f"{emoji*3}\n {name} - {proffession}\n {passion} \n {website} \n {emoji*3}"

bio = generate_bio(style)

print("\n your stylish bio:\n")
print("*" * 60)
print(textwrap.dedent(bio))
print("*" * 60)

save = input("want to save this into text file? (y/n): ").lower()
if save == "y":
      filename = f"{name.lower().replace(' ', '_')}_bio.txt"
      with open(filename,"w", encoding ="utf-8")as f:
            f.write(bio)
      print("file saved")
   
      