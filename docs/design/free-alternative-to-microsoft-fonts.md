# Alternatives to Microsoft Proprietary Fonts

This tutorial explains how to install free fonts on Linux that can serve as alternatives to Microsoft's proprietary fonts. Some of them are available in Linux repositories, others on Google Fonts, and others from additional sources.

The following table lists common document uses for free font alternatives to Microsoft's proprietary fonts:

|     **Windows Font**     |                                                  **Free Alternatives**                                                   |                  **Common Use in Documents**                  |                                             **Notes**                                             |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Arial**                | **Free Sans** / **Liberation Sans** / **Nimbus Sans** / **IBM Plex Sans** / **Ubuntu Sans**                              | Body text, titles, subtitles                                  | Standard and versatile sans-serif font.                                                           |
| **Times New Roman**      | **Free Serif / Liberation Serif / Nimbus Roman / IBM Plex Serif**                                                        | Body text, formal reports, books                              | Classic serif font for professional documents.                                                    |
| **Courier New**          | **FreeMono / Liberation Mono**                                                                                           | Code, technical documents, monospaced text                    | Monospaced font used in programming and tabular text.                                             |
| **Calibri**              | **Carlito** / **Lato**                                                                                                   | Body text, presentations                                      | Modern and readable font.                                                                         |
| **Cambria**              | **Caladea / Cambo**                                                                                                      | Body text, formal reports                                     | Similar to Times New Roman, with better on-screen readability.                                    |
| **Comic Sans MS**        | **Comic Neue**                                                                                                           | Informal text, educational material, children's presentations | Comic Neue is a more refined alternative.                                                         |
| **Verdana**              | **DejaVu Sans**                                                                                                          | Body text, web pages, graphical interfaces                    | Excellent screen readability.                                                                     |
| **Georgia**              | **Gelasio**                                                                                                              | Body text, document titles                                    | Serif font with good on-screen readability.                                                       |
| **Trebuchet MS**         | **Fira Sans**                                                                                                            | Titles, subtitles, presentations                              | Alternative with a clean and modern design.                                                       |
| **Impact**               | **Anton** / **Oswald**                                                                                                   | Attention-grabbing titles                                     | Anton is an alternative with strong visual impact.                                                |
| **Tahoma**               | **Signika**                                                                                                              | Body text in graphical interfaces and business documents      | Similar spacing and clarity.                                                                      |
| **Palatino Linotype**    | **Source Serif 4**                                                                                                       | Books, essays, academic texts                                 | Based on the Palatino design.                                                                     |
| **Book Antiqua**         | **P052 / C059**                                                                                                          | Body text in elegant or classic documents                     | Classic alternatives with a refined style.                                                        |
| **Franklin Gothic Book** | **Libre Franklin**                                                                                                       | Titles, posters, headings                                     | Strong sans-serif font with a bold style.                                                         |
| **Century Gothic**       | **URW Gothic**                                                                                                           | Modern titles, graphic design                                 | Clean, futuristic design.                                                                         |
| **Rockwell**             | **Arvo**                                                                                                                 | Titles with visual impact                                     | Slab-serif style alternatives.                                                                    |
| **Baskerville**          | **Goudy Bookletter 1911**                                                                                                | Body text in classic and elegant documents                    | Font with excellent print readability.                                                            |
| **Consolas**             | **JetBrains Mono** / **DejaVu Sans Mono** / **Fira Code** / **Hack** / **Iosevka** / **Victor Mono** / **Fragment Mono** | Programming code, terminals, technical documents              | Consolas is monospaced; these alternatives support code ligatures or developer-friendly features. |

## Installing Free Fonts from Linux Repositories (Debian/MX Linux/Ubuntu, etc.)

Install free fonts directly from the repositories with this command:

```bash
sudo apt install fonts-liberation fonts-freefont-ttf fonts-crosextra-carlito \
    fonts-crosextra-caladea fonts-dejavu fonts-cantarell fonts-firacode \
    fonts-jetbrains-mono fonts-ebgaramond fonts-ebgaramond-extra \
    fonts-hack fonts-inconsolata fonts-uralic \
    fonts-urw-base35 fonts-bpg-georgian fonts-comic-neue \
    fonts-goudybookletter fonts-ibm-plex
```

**Note:** To install the `fonts-ibm-plex` package, the `contrib` repository must be enabled. If you use Debian, you need to [enable it](https://facilitarelsoftwarelibre.blogspot.com/search/label/Descargar%20Debian).

Among the installed packages, some provide multiple fonts with different styles and names:

**fonts-liberation =** Liberation Sans, Liberation Serif  
**fonts-freefont-ttf =** FreeMono  
**fonts-crosextra-carlito =** Carlito  
**fonts-crosextra-caladea =** Caladea  
**fonts-dejavu =** DejaVu Sans, DejaVu Sans Mono  
**fonts-cantarell =** Cantarell  
**fonts-ebgaramond =** EB Garamond (08, 12)  
**fonts-ebgaramond-extra =** EB Garamond SC (08, 12), EB Garamond 12 All SC  
**fonts-ibm-plex =** IBM Plex Sans, IBM Plex Serif, IBM Plex Mono  
**fonts-hack =** Hack  
**fonts-inconsolata =** Inconsolata  
**fonts-urw-base35 =** Nimbus Roman, Nimbus Sans, URW Gothic, URW Bookman, C059, P052  
**fonts-comic-neue =** Comic Neue  
**fonts-goudybookletter =** Goudy Bookletter 1911

* * *

## Alternative Fonts from Google Fonts

Some fonts are not available in Linux repositories. Some are included in this repository, but you can also download them manually from [Google Fonts](https://fonts.google.com/):

Search for the font and download it as a `.zip` file containing `.ttf` or `.otf` files.

**Note:** I keep a backup at: [https://github.com/wachin/Alternativa-a-fuentes-de-Windows](https://github.com/wachin/Alternativa-a-fuentes-de-Windows)

**Slabo 27px -> Alternative to Rockwell**  
[https://fonts.google.com/specimen/Slabo+27px](https://fonts.google.com/specimen/Slabo+27px)

**EB Garamond -> Alternative to Garamond**  
https://fonts.google.com/specimen/EB+Garamond

**Libre Franklin -> Alternative to Franklin Gothic**  
[https://fonts.google.com/specimen/Libre+Franklin](https://fonts.google.com/specimen/Libre+Franklin)

**Oswald -> Alternative to Impact**  
[https://fonts.google.com/specimen/Oswald](https://fonts.google.com/specimen/Oswald)

**Anton -> Alternative to Impact**  
[https://fonts.google.com/specimen/Anton](https://fonts.google.com/specimen/Anton)

**Arvo -> Alternative to Rockwell**  
[https://fonts.google.com/specimen/Arvo](https://fonts.google.com/specimen/Arvo)

**Source Serif 4 -> Alternative to Georgia**  
[https://fonts.google.com/specimen/Source+Serif+4](https://fonts.google.com/specimen/Source+Serif+4)

**Lato -> Alternative to Calibri**  
[https://fonts.google.com/specimen/Lato](https://fonts.google.com/specimen/Lato)

**Cambo**  
[https://fonts.google.com/specimen/Cambo](https://fonts.google.com/specimen/Cambo)

**Fira Sans**  
[https://fonts.google.com/specimen/Fira+Sans](https://fonts.google.com/specimen/Fira+Sans)

**Victor Mono -> Alternative to Consolas**  
[https://fonts.google.com/specimen/Victor+Mono](https://fonts.google.com/specimen/Victor+Mono)

**Fragment Mono -> Alternative to Consolas**  
[https://fonts.google.com/specimen/Fragment+Mono](https://fonts.google.com/specimen/Fragment+Mono)

**Gelasio -> Alternative to Georgia**  
[https://fonts.google.com/specimen/Gelasio](https://fonts.google.com/specimen/Gelasio)

**Signika**  
[https://fonts.google.com/specimen/Signika](https://fonts.google.com/specimen/Signika)

**Iosevka -> Alternative to Consolas**  
[https://github.com/be5invis/Iosevka/releases](https://github.com/be5invis/Iosevka/releases)  
The following link is an example of the zip file that contains the fonts in `.ttf` format:  
[https://github.com/be5invis/Iosevka/releases/download/v32.5.0/PkgTTF-Iosevka-32.5.0.zip](https://github.com/be5invis/Iosevka/releases/download/v32.5.0/PkgTTF-Iosevka-32.5.0.zip)

# Installing Fonts on Linux

Many older guides recommend copying Windows fonts to the personal `~/.fonts` directory.  
This **still works in 2025**, but the Fontconfig configuration file in Debian 12:

`/etc/fonts/fonts.conf`

clearly states:

```bash
<dir prefix="xdg">fonts</dir>
<!-- the following element will be removed in the future -->
<dir>~/.fonts</dir>
```

![](https://blogger.googleusercontent.com/img/a/AVvXsEizJKqIR0EABs9Adxy82JnefqzQaC_4UfN0ymDV4Pqr4IkBVoDycNYVY14F4Z53rgbkbZhQaSLZYLHQ03JWPixHhGMy_Yj_A7l2B-VprbbkBPBRFCSrEeb6nMXyq7P8rppyg1SiAKSUZjpz7o-UROxj_fbfGCpWc3ZLDImXiMLUB2chSYIoc225HnlJohc=s16000-rw)

This means `~/.fonts` **will be removed in the future**, and the recommended location according to the **XDG Base Directory** standard is:

```text
~/.local/share/fonts
```

So if you install fonts only for your own user account, it is better to start using that recommended location.

## Install Fonts Only for Your User (Without Touching the System)

To install fonts only for your own user account, you can place them in the recommended directory:

```text
~/.local/share/fonts
```

> **Note:** The `~` symbol represents your home directory, for example `/home/youruser/`.

### 1. Create the Directory Automatically (Quick Method)

Open a terminal and run:

```bash
mkdir -p ~/.local/share/fonts
```

This command creates the full path if needed.

- The `-p` option makes it **create any missing directories** without failing if they already exist.

### 2. Create the Directory Manually (Without Using the Terminal)

If you prefer to do it graphically:

1. Open your **file manager**.
2. Press `Ctrl + H` to show **hidden directories**. In Linux, directories that start with a dot `.` are hidden.
3. If the `.local` directory does not exist, create it:
   Right click -> **Create folder** -> type `.local`
4. Inside `.local`, create another directory called `share`.
5. Inside `share`, create another directory called `fonts`.

The final path should look like this:

```text
/home/youruser/.local/share/fonts
```

### 3. Copy the Fonts

Copy all the Windows font files (`.ttf` or `.otf`) and paste them into that directory. You can create subdirectories inside `fonts` if you want to organize them, for example `windows`, `personal`, and so on.

* * *

### Advantages of This Method

- You do not need administrator privileges.
- The fonts apply only to your user account. Other users on the system will not see them.
- This is the currently recommended method. The old `~/.fonts` directory still works, but it is marked for future removal.

## Installing Fonts System-Wide

If the computer has **multiple users** and all of them need the Windows fonts, they should be installed **for the whole system**.

### Where Do System Fonts Go?

System fonts on Linux are stored in:

`/usr/share/fonts/truetype/`

You can create a new directory there, for example:

`/usr/share/fonts/truetype/windows`

and paste all Windows fonts into it.

### How to Copy Fonts Without Using the Terminal

To move files into that directory you need administrator privileges. There are several graphical ways to do it:

#### 1. Using **Krusader**

**a.)** Install Krusader if you do not already have it:

```bash
sudo apt install krusader
```

**b.)** Run Krusader as superuser:

```bash
sudo krusader
```

**c.)** Browse to the directory where you keep the Windows fonts and copy them.

**d.)** Open a new tab with `Ctrl + T`, go to `/usr/share/fonts/truetype/`, create the `windows` directory, and paste the fonts there.  
*(You can also use the other panel instead of opening a new tab.)*

#### 2. Using **Double Commander (GTK or QT)**

**a.)** Install Double Commander, if available in the repositories:

```bash
sudo apt install doublecmd-gtk
```

or, if you use KDE Plasma or LXQt:

```bash
sudo apt install doublecmd-qt
```

**b.)** Run Double Commander with superuser privileges:

```bash
sudo doublecmd-gtk
```

or:

```bash
sudo doublecmd-qt
```

**c.)** Copy the fonts to `/usr/share/fonts/truetype/windows`.

## Tips for Using a File Manager as Superuser

- **Be very careful** not to delete or move operating system files or directories. If you remove or move something critical, the system may stop working and you may need to reinstall it.
- **Do not open your personal files (images, documents, etc.)** from a file manager running as superuser. The program that opens those files may inherit superuser privileges and change file ownership, which can prevent you from accessing them later from your normal user account.
- **Close the file manager when you are done using it as superuser.** Leaving it open can be dangerous, because if you come back later and forget it is still running with administrator privileges, you could delete or move something important without realizing it.

## Refresh the Font Cache (Optional)

After copying the fonts, it is recommended to refresh the font cache:

```bash
sudo fc-cache -fv
```

### Verify the Installation

Open a program such as LibreOffice, GIMP, or Inkscape and check whether the newly added fonts appear.

### When Do You Actually Need `fc-cache -fv`?

1. When you install fonts in non-standard directories, such as one you created manually or one that is not detected automatically.
2. When you run automated scripts or installations without an active graphical session, for example on servers or in mass deployments.
3. When a specific program does not detect the new font even after restarting it.
4. When you have problems with corrupted fonts, stale cache, or conflicts, and need to rebuild the entire font cache.

### A Bit of History

For a long time, the de facto place to install user-level fonts was:

- `~/.fonts`, meaning a `.fonts` directory inside your home directory

This method worked well and was the most widely documented one in distributions such as Debian and Ubuntu before 2010. Many old tutorials, and still many current ones in 2025, continue to recommend that path.

* * *

### What Changed?

Starting with the **XDG specifications** (X Desktop Group), distributions began to move toward a more standardized structure for user files. In that structure:

- User data is stored in `~/.local/share/`
- Therefore, **per-user fonts** are installed in:

```text
~/.local/share/fonts
```

This change was adopted gradually, and **modern `fontconfig` versions, such as the one shipped with Debian 12**, automatically recognize and monitor that path as a valid font location.

## Optional: Install a GUI to Manage Fonts

If you want to view, enable, or disable fonts more easily, install **Fontmatrix**:

```bash
sudo apt install fontmatrix
```

Then open it from the menu and review your installed fonts.

If the fonts do not look right, you should adjust the visible font settings.

Click:

**Edit > Preferences**

Click:

**Display > Default font size**

and set, for example:

**10**

This number is only an example and depends on how the fonts look on your monitor. Click Close, then close Fontmatrix and open it again to see the change.

You can also see my tutorial:

**Install FontMatrix and configure it on Debian 12**  
[https://facilitarelsoftwarelibre.blogspot.com/2025/02/instalar-fontmatrix-y-configurarlo-en-debian-12.html](https://facilitarelsoftwarelibre.blogspot.com/2025/02/instalar-fontmatrix-y-configurarlo-en-debian-12.html)

* * *

## Additional Advice

- If you share documents with Windows users, use Windows fonts when necessary to make sure the files open correctly on another computer. For example, if someone is writing a thesis and needs to share files with other students, or if you are preparing a graphic design file such as an `.svg` converted to PDF and you will send it to a print shop. For any file that will be opened on another computer, make sure the font is available there as well, or carry the font files on a USB drive and install them on that computer so the document can be displayed correctly.

# References

**Linux Font Equivalents to Popular Web Typefaces | Jon Christopher**  
[https://jonchristopher.us/blog/linux-font-equivalents-to-popular-web-typefaces/](https://jonchristopher.us/blog/linux-font-equivalents-to-popular-web-typefaces/)

**How do I install fonts?**  
[how-do-i-install-fonts](https://askubuntu.com/questions/3697/how-do-i-install-fonts)

**Add an extra font for individual users**  
[fonts-user.html.es](https://help.gnome.org/admin/system-admin-guide/stable/fonts-user.html.es)

**Font configuration (Spanish)**  
[Font_configuration_%28Español%29](https://wiki.archlinux.org/title/Font_configuration_%28Español%29)
