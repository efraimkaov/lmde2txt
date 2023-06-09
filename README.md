# lmde2txt

### This application converts lmde to txt (removes lmde syntax from text files)

![lmde2txt](https://github.com/efraimkaov/lmde2pdf/assets/63643635/dd10ad0b-925e-474b-b1b5-70a5640d7889)

### What are lmde files

* **lmde** stands for **Like Mark Down Extended**

* **lmde** is a plain text file with **.lmde** extension and markdown inspired syntax

## lmde syntax

```
# Heading1
## Heading2
### Heading3
$ Paragraph1
$^ Paragraph1 with drop caps
$$ Paragraph2

[png](link.png)

**Bold text**
__Italicized text__
``Red text``

[^][(Footnote)]

[lh](Left header text)
[rh](Right header text)
```

### Dependencies

* Python3 >= 3.9.2

## Installation (in progress)

```sh
git clone https://github.com/efraimkaov/lmde2txt.git
cd lmde2pdf/
pip3 install -r requirements.txt
```

### lmde2txt-cli.py examples

```sh
python3 lmde2txt-cli.py -d /home/user/Documents/mybook
```

#### If you find a bug please open a new issue and send a Bug report.

##### If someone test this application in macOS or Windows please let me know if works or not (only tested in Linux)!
