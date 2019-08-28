# able-test
### Description
This repository presents a simple problem to be solved by new ABLE candidates that want to contribute
to the ABLE project. Even though it has been specifically designed for this purpose, it has common
aspects with work being currently done in the ABLE desktop application. Apart from being a coding problem,
this exercise will be evaluated from other perspectives such as code cleanliness, code structure, 
code documentation, git flow, ...
### The problem
Using PyQt5, the candidate should create a simple window with a pushbutton in the middle.
When this pushbutton is pressed, a popup window should open prompting the user on whether they want
to close the application or not. The same popup window should open when the Windows close button or 
Alt+F4 are pressed. These are the basic functionalities the app should have. If the candidate feels
like going further, some extra features have also been listed.
### System requirements
* Windows machine
* [Python 3.x](https://www.python.org/) installed
* [PyQt5](https://pypi.org/project/PyQt5/) installed

### What will be evaluated
* **The functionality and performance of the code:** The code should work and no unexpected behaviour
should occur. This means, no sudden crashes regardless of how the user interacts with the app.
* **Cleanliness of the code:** the code should be well structured and it should be understandable by 
the evaluators. For us, it is better to write some extra lines or longer variable names if this let's 
another developer contribute easier and faster. 
* **Scalability of the architecture:** even though the exercise may seem simple, it should be resolved as it was
the first step of a much bigger project, considering other developers will contribute in the future. 
In this way, MVC architectures are highly welcomed.
* **Documentation:** the code should be well documented following any of the documentation standards
for Python.
* **The procedures followed to contribute in the git repository:** [this link](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/)
perfectly describes what would be a clean contribution to an external repository. The contributing branch
should be **branched from develop**. Follow a [git-flow](https://datasift.github.io/gitflow/IntroducingGitFlow.html).
### Basic functionalities
1. A simple window like the following should be created at startup:

   ![Alt text](/media/basic_layout.PNG "Basic Layout")
   * Background color: #2a2a2a (RGB: 42, 42, 42)
   * Button background color: #535353 (RGB: 83, 83, 83)
   * Window size at creation: 300x300.
   * Window minimum size restricted to 200x200. No restriction on maximum size. It should be resizable.
   * Button size 100x100.
   * Button text: white, bold and size 16 px.
   * Button should always be centered on window, regardless of how the user resizes or moves the window
   on the screen.
2. When the button is pressed, a popup message like the following should appear:

   ![Alt text](/media/popup_basic.PNG "Basic popup")
   * Popup background color: #2a2a2a (RGB: 42, 42, 42)
   * Buttons background color: #535353 (RGB: 83, 83, 83)
   * If right after showing the popup message, the user hits Enter, the popup message should just hide and nothing else should happen.
   * If the user clicks anything but the Yes button, the popup message should just hide and leave the main window visible.
   * If, on the other hand, the user presses Yes, then the app should close immediately.
3. The same popup message should appear when trying to close the app in any other way: Windows close button, Alt+F4, ...
#### Extra features
- Show ABLE logo in both the top bar and the task bar of the main window. The logo can be found in the *media* folder.

   ![Alt text](/media/able_logos_top_task.PNG "ABLE logos")
- Replace the button by a exit button and make it responsive to hover and press. All necessary icons are in the *media* folder.

   ![Alt text](/media/custom_button.gif "Custom button")
- Show ABLE logo in the top bar of the popup message.

   ![Alt text](/media/popup_able_logo.PNG "ABLE logo in popup bar")
- Replace information icon by the exit icon.

   ![Alt text](/media/popup_exit_icon.PNG "Exit icon in popup")
- Change cursor to pointing hand when hovering button

   ![Alt text](/media/custom_button.gif "Custom button")
